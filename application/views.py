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

def edit(request):
    current_user = request.user
    if request.method == 'POST':
       form = EditForm(request.POST)
       
       if form.is_valid():
          
           edit = form.save(commit=False)
           edit.user = current_user
           edit.save()
           print('its works')
       return redirect('index')
    else:
       form = EditForm()
    return render(request, 'counsellor/counsellor_edit.html',{"form":form})

def display(request):
    sessions = Client.objects.all()
    return render(request, 'client/sessions.html',{'sessions':sessions})
  