from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver



class user_type( models.Model):
    is_client = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.is_client == True:
            return self.user + " - is_client"
        else:
            return self.user + " - is_doctor"