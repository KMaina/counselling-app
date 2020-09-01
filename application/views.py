from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import CreateView
from .decorators import client_required, counsellor_required
from django.contrib.auth import login
from .models import *
from .forms import *


def home(request):
    if request.user.is_authenticated:
        if request.user.is_counsellor:
            return redirect('counsellor_home')
    
    return render(request, 'index.html')


def join(request):
    if request.user.is_authenticated:
        if request.user.is_counsellor:
            return redirect('counsellor_home')
        else:
            return redirect('client_home')
    return render(request, 'choice.html')


class SignUpView(TemplateView):
    template_name = 'signup.html'


#client views
class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'django_registration/registration_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('client_home')

def client_home(request):
    return render(request, 'client/index.html')

def counsel(request):
    return render(request, 'counsellor/counsellors_list.html')

def client_med(request):
    medication = Client.objects.all()
    return render(request, 'counsellor/client-med.html', {'medication':medication})

def client(request):
    return render (request, 'client/client.html')

#counsellor views
class CounsellorSignUpView(CreateView):
    model = User
    form_class = CounsellorSignUpForm
    template_name = 'django_registration/registration_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'counsellor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('counsellor_home')

@counsellor_required
def counsellor_home(request):
    return render(request, 'counsellor/home.html')

@counsellor_required
def support_group(request):
    return render(request, 'counsellor/support_group.html')

@counsellor_required
def client_group(request):
    client = Client.objects.all()
    return render(request, 'counsellor/client_group.html', {"client": client})
def edit(request, id):
    current_user = request.user
    client = Client.objects.get(user=id)
    dr = Counsellor.objects.get(user=current_user.id)
    if request.method == 'POST':
       form = EditForm(request.POST)
       if form.is_valid():
           edit = form.save(commit=False)
           edit.user = client.user
           edit.counsellor = dr
           edit.save()
       return redirect('display')
    else:
       form = EditForm()
    return render(request, 'counsellor/counsellor_edit.html',{"form":form})

def display(request):
    sessions = Client.objects.filter(counsellor=request.user.id).all()
    return render(request, 'counsellor/client-med.html',{'sessions':sessions})
  
