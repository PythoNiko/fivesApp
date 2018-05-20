from django.conf.urls import url
from . import views

app_name = 'fives'

urlpatterns = [
    # /fives/
    url(r'^$', views.index, name='index'),

    # /fives/findapitch
    url(r'^findapitch/$', views.findapitch, name='findapitch'),
]

