from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe, escape
from datetime import timedelta



class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_counsellor = models.BooleanField(default=False)



class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    medication = models.CharField(max_length=255, blank=True)
    group = models.ForeignKey('SupportGroup', on_delete=models.CASCADE, null=True)
    counsellor = models.ForeignKey('Counsellor', on_delete=models.CASCADE)
    time = models.DateTimeField(max_length=50, blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)

    def save_client(self):
        self.save()

    def __str__(self):
        return f"{self.user.username}"


class Counsellor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_photo = models.ImageField(default='default_avatar.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"Dr. {self.user.username}"

class SupportGroup(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='group_profiles', default='image.jpg')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

  