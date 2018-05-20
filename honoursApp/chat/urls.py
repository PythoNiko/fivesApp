from django.conf.urls import url, include
from . import views

app_name = 'chat'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # /chat/chat
    url(r'^chat/$', views.chat, name='chat'),
]