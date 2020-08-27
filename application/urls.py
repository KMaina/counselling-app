from . import views
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^client_list/', views.client_list, name='client_list')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 
