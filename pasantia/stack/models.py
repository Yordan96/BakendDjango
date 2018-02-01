from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Pregunta(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    created_date = models.DateTimeField(
                default=timezone.now)
    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    comentario = models.CharField(max_length=255)
    #pregunta = models.ForeignKey(Pregunta)
    pregunta = models.CharField(max_length=255)
    correcta = models.BooleanField(default=False)
    autor = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(
                default=timezone.now)
    def __str__(self):
        return self.comentario

class Boto(models.Model):
    comentario = models.ForeignKey(Comentario)
    botos = models.IntegerField(blank=True, null=True,default=0)
    autor = models.ForeignKey('auth.User')
