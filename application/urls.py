from . import views
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^index/$', views.index, name='index'),
    url(r'^counsellor/$', views.counsellorhome, name='counsellorhome'),

    #client urls
    url(r'^clients/home/$', views.client_home, name='client_home'),
    
    #counsellor urls
    url(r'^counsellors/home/$', views.counsellor_home, name='counsellor_home'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
