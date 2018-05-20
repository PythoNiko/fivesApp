from django.conf.urls import url, include
from . import views

app_name = 'emter'

urlpatterns = [
    url(r'^enter/$', views.index, name='index'),
    url(r'^login/$', views.index, name='login'),
    url(r'^register/$', views.index, name='register'),
]