from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^lista/', postagem, name='home'),
    url(r'^post/(?P<pk>[0-9]+)', postagem_list, name='post'),
]