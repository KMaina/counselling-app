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
        else:
            return redirect('client')
    
    return render(request, 'index.html')


def articles(request):
    return render(request, 'article.html')


def join(request):
    if request.user.is_authenticated:
        if request.user.is_counsellor:
            return redirect('counsellor_home')
        else:
            return redirect('client')
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
        return redirect('client')

def counsel(request):
    return render(request, 'counsellor/counsellors_list.html')

@client_required
def client(request):
    current_user = request.user
    client = Client.objects.filter(user=current_user.id)
    return render (request, 'client/client.html', {'client':client})

def contact(request):
    return render(request, 'counsellor/counsellor-contact.html')

def chat(request, id):
    current_user = request.user
    client = Client.objects.get(user=current_user.id)
    grp = SupportGroup.objects.get(id=id)
    messages = Discussion.objects.filter(group=id).all()
    if request.method == 'POST':
        form = Forum(request.POST)
        if form.is_valid():
            discuss = form.save(commit=False)
            discuss.sender = client
            discuss.group = grp
            discuss.save()
        return redirect('client')
    else:
        form = Forum()
    return render(request, 'client/chat.html', {'form':form, 'client':client, 'messages':messages})


def change(request, id):
    current_user = request.user
    client = Client.objects.get(user=id)
    if request.method == 'POST':
        form = ChangeDoctor(request.POST)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = client.user
            edit.save()
        return redirect('client')
    else:
        form = ChangeDoctor()
    return render(request, 'client/change_doctor.html',{"form":form})


def book(request, id):
    current_user = request.user
    client = Client.objects.get(user=id)
    dr = client.counsellor
    if request.method == 'POST':
        form = Appointment(request.POST)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = client.user
            edit.counsellor = dr
            edit.save()
        return redirect('client')
    else:
        form = Appointment()
    return render(request, 'client/appointment.html',{"form":form})


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
        person = User.objects.get(id=user.id)
        Counsellor.objects.create(user=person)
        login(self.request, user)
        return redirect('counsellor_home')

@counsellor_required
def counsellor_home(request):
    return render(request, 'counsellor/home.html')

@counsellor_required
def support_group(request):
    if request.method == 'POST':
        form = CreateGroup(request.POST)
        if form.is_valid():
            create=form.save(commit=False)
            create.save()
        return redirect('group_list')
    else:
        form=CreateGroup()
    return render(request, 'counsellor/support_group.html', {'form':form})


@counsellor_required
def group_list(request):
    groups = SupportGroup.objects.all()
    return render(request, 'counsellor/group_list.html', {'groups':groups})


@counsellor_required
def client_group(request):
    client = Client.objects.all()
    return render(request, 'counsellor/client_group.html', {"client": client})


@counsellor_required
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


@counsellor_required
def display(request):
    sessions = Client.objects.filter(counsellor=request.user.id).all()
    return render(request, 'counsellor/client-med.html',{'sessions':sessions})


@counsellor_required
def addclient(request):
    current_user = request.user
    dr = Counsellor.objects.get(user=current_user.id)
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            add = form.save(commit=False)
            add.counsellor = None
            add.counsellor = dr
            add.save()
        return redirect('display')
    else:
        form = AddClientForm()
    return render(request, 'counsellor/add_client_form.html',{"form":form})


@counsellor_required
def delete_group(request, id):
    grp = SupportGroup.objects.filter(id=id)
    grp.delete()
    return redirect('group_list')


@counsellor_required
def edit_group(request, id):
    grp = SupportGroup.objects.get(id=id)
    if request.method == 'POST':
        form = EditGroup(request.POST)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.id = id
            edit.save()
        return redirect('group_list')
    else:
        form = EditGroup()
    return render(request, 'counsellor/edit_group.html', {'form':form})

def profile(request):
    client = request.user.client
    form = ClientProfileForm(instance=client)

    if request.method == 'POST':
        form = ClientProfileForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'client/profile.html', context)