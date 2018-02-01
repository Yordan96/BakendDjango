from django.conf.urls import url
from django.contrib import admin
from productos.views import *

urlpatterns = [
    url(r'^productos/', ProductoList.as_view(), name ='productos'),
]
