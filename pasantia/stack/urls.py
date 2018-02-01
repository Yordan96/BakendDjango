from django.conf.urls import url
from django.contrib import admin
from stack.views import *
from stack import views



urlpatterns = [
    url(r'^preguntas/', PreguntaList.as_view(), name ='preguntas'),
    url(r'^comentario/', ComentarioList.as_view(), name ='comentario'),
    url(r'^comentario/', ComentarioList.as_view(), name ='boto'),
]
