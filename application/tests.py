from django.test import TestCase
from .models import *
from django.urls import path
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.conf import settings

class TestUser(TestCase):
    '''test class for AbstractUser model'''
    def setUp(self):
        self.user = User.objects.create_user(username='Linda', password='LindaMaina123', is_client=True)
        self.user = User.objects.create_user(username='Kay', password='KayLyne123', is_counsellor=True)

    def tearDown(self):
        self.user.delete()

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
        self.user.save()
        self.assertIsInstance(self.user, User)


class TestClient(TestCase):
    '''test class for Client model'''
    def setUp(self):
        self.user = User.objects.create_user(username='Linda', password='LindaMaina123', is_client=True)
        self.user.save()
        self.another_user = User.objects.create_user(username='Doktari', password='DRMaybelle456', is_counsellor=True)
        self.another_user.save()

        self.group = SupportGroup(name='Alcoholics Anonymous')
        self.group.save()

        self.doctor = Counsellor(user=self.another_user)
        self.doctor.save()

        self.client = Client(user=self.user, group=self.group, counsellor=self.doctor)

    def tearDown(self):
        self.user.delete()
        self.another_user.delete()
        self.group.delete()
        self.doctor.delete()

    def test_client_creation(self):
        self.assertIsInstance(self.client, Client)
        self.client.save()
        self.assertIsInstance(self.client, Client)
        self.assertEqual(len(Client.objects.all()), 1)


class TestCounsellor(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Doktari', password='DRMaybelle456', is_counsellor=True)
        self.user.save()
        self.dr = Counsellor(user=self.user)

    def tearDown(self):
        self.user.delete()
        self.dr.delete()

    def test_doctor_creation(self):
        self.dr.save()
        self.assertIsInstance(self.dr, Counsellor)


class TestSupportGroup(TestCase):
    def setUp(self):
        self.group = SupportGroup(name='Suicide Loss Survivors')
        self.group.save()
    
    def tearDown(self):
        self.group.delete()

    def test_creation(self):
        self.assertIsInstance(self.group, SupportGroup)
        self.assertEqual(self.group.name, 'Suicide Loss Survivors')
        self.assertEqual(len(SupportGroup.objects.all()), 1)
    

class TestDiscussion(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Patient', password='Patient456', is_client=True)
        self.user.save()
        self.another_user = User.objects.create_user(username='Doktari', password='DRMaybelle456', is_counsellor=True)
        self.another_user.save()

        self.group = SupportGroup(name='Suicide Loss Survivors')
        self.group.save()

        self.doctor = Counsellor(user=self.another_user)
        self.doctor.save()

        self.client = Client(user=self.user, group=self.group, counsellor=self.doctor)
        self.client.save()

        self.discussion = Discussion(message='some text', sender=self.client, group=self.group)

    def tearDown(self):
        self.user.delete()
        self.group.delete()
        self.client.delete()

    def test_discussion_creation(self):
        self.discussion.save()
        self.assertEqual(len(Discussion.objects.all()), 1)
        self.assertEqual(self.discussion.group, self.client.group)