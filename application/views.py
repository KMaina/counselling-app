from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import CreateView
from .decorators import client_required, counsellor_required
from django.contrib.auth import login, authenticate
from .models import *
from .forms import *
from .forms import ClientSignUpForm,CounsellorSignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def home(request):
    if request.user.is_authenticated:
        if request.user.is_counsellor:
            return redirect('counsellor_home')
        else:
            return redirect('client_home')
    
    return render(request, 'index.html')


def articles(request):
    return render(request, 'article.html')


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

def ClientSignUpForm(request):
    if request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = ClientSignUpForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

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

def CounsellorSignUpForm(request):
    if request.method == 'POST':
        form =  CounsellorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form =  CounsellorSignUpForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

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

def group_list(request):
    groups = SupportGroup.objects.all()
    return render(request, 'counsellor/group_list.html', {'groups':groups})


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