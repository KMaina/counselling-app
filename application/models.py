from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe, escape



class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    medication = models.CharField(max_length=255)
    group = models.ManyToManyField('SupportGroup')
    counsellor = models.ForeignKey('Counsellor', on_delete=models.CASCADE)


class SupportGroup(models.Model):
    name = models.CharField(max_length=255)   