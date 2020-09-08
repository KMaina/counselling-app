"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('application.urls')),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup/$', views.SignUpView.as_view(), name='signup'),
    path('accounts/register/client/', views.ClientSignUpView.as_view(), name='client_signup'),
    path('accounts/register/counsellor/', views.CounsellorSignUpView.as_view(), name='counsellor_signup'),
    path('activate_doc/<uidb64>/<token>/', views.CounsellorActivate.as_view(), name='activate'),
    path('activate_pat/<uidb64>/<token>/', views.ClientActivate.as_view(), name='activate'),
]
