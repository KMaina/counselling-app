from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ValidationError
from .models import *
from tempus_dominus.widgets import  DateTimePicker



class CounsellorSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(CounsellorSignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', "email", 'password1', 'password2']:
            self.fields[fieldname].help_text = None


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_counsellor = True
        if commit:
            user.save()
        return user


class ClientSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(ClientSignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', "email", 'password1', 'password2']:
            self.fields[fieldname].help_text = None


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        return user


class EditForm(forms.ModelForm):
    time = forms.DateTimeField(widget=DateTimePicker(), required=False)
    group = forms.ModelChoiceField(required=False,queryset=SupportGroup.objects ,empty_label=None)
    link = forms.CharField(required=False)
    class Meta:
        model = Client
        fields = ['medication', 'group', 'time', 'link']


class CreateGroup(forms.ModelForm):
    class Meta:
        model = SupportGroup
        fields = ['name', 'description']

        
class AddClientForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_client=True), empty_label=None)
    class Meta:
        model = Client
        fields = ['user', 'issue']
