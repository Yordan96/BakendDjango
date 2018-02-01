from django.contrib import admin
from .models import Pregunta,Comentario, Boto
# Register your models here.
admin.site.register(Pregunta)
admin.site.register(Comentario)
admin.site.register(Boto)
