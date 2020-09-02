from . import views
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$', views.home, name='index'),
    url(r'^join/$', views.join, name='join'),
    url(r'^counsellors/list/$', views.counsel, name='counsellor_list'),

    #client urls
    url(r'^clients/home/$', views.client_home, name='client_home'),
    url(r'^clients/chat/$', views.chat, name='chat'),
    
    #counsellor urls
    url(r'^counsellors/home/$', views.counsellor_home, name='counsellor_home'),
    url(r'^counsellors/support_group/$', views.support_group, name='c_group'),

    url(r'^counsellors/client_med/$', views.client_med, name='client_med'),
    url(r'^counsellors/contact/$', views.contact, name='contact'),
    url(r'^edit/(\d+)/$', views.edit, name='edit'),
    url(r'^counsellors/client_data/$', views.display, name='display'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
