from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ValidationError
from .models import *


class CounsellorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_counsellor = True
        if commit:
            user.save()
        return user


class ClientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        return user