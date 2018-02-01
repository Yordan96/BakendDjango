from django.shortcuts import render
from rest_framework import generics
from .models import Pregunta, Comentario
from .serializers import PreguntaSerializer, ComentarioSerializer
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# Create your views here.
class PreguntaList(generics.ListCreateAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj= get_object_or_404(
        queryset,
        pk= self.kwargs['pk'],
        )
        return obj
    def perform_create(self, serializer):
        serializer.save(autor=User.objects.get())
    class Meta:
        ordering = ('created_date',)

class ComentarioList(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj= get_object_or_404(
        queryset,
        pk= self.kwargs['pk'],
        )
        return obj
    def perform_create(self, serializer):
        serializer.save(autor=User.objects.get())
