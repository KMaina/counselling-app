from . import views
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$', views.home, name='index'),
    url(r'^join/$', views.join, name='join'),

    url(r'^articles/$', views.articles, name='articles'),
    url(r'^counsellors/list/$', views.counsel, name='counsellor_list'),

    #client urls
    url(r'^client/$', views.client, name='client'),
    url(r'^group/chat/(\d+)/$', views.chat, name='chat'),
    
    url(r'^change/(\d+)/$', views.change, name='change'),
    url(r'^appointment/(\d+)/$', views.book, name='book'),
    url(r'^profile/$', views.profile, name='profile'),
    #counsellor urls
    url(r'^counsellors/home/$', views.counsellor_home, name='counsellor_home'),
    url(r'^counsellors/support_group/$', views.support_group, name='c_group'),
    url(r'^counsellors/contact/$', views.contact, name='contact'),
    url(r'^edit/(\d+)/$', views.edit, name='edit'),
    url(r'^delete/group(\d+)/$', views.delete_group, name='delete_group'),
    url(r'^edit/group/(\d+)/$', views.edit_group, name='edit_group'),
    url(r'^counsellors/client_data/$', views.display, name='display'),
    url(r'^counsellors/group_list/$', views.group_list, name='group_list'),
    url(r'^addclient/$', views.addclient, name='addclient'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
