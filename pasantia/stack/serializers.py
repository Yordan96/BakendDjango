from . models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields = ('id','username')

class PreguntaSerializer(serializers.HyperlinkedModelSerializer):
     autor= serializers.StringRelatedField()
     class Meta:
         model =  Pregunta
         fields = ('autor','titulo','descripcion')


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    autor= serializers.StringRelatedField()
    #pregunta= serializers.StringRelatedField()
    class Meta:
        model =  Comentario
        fields = ('comentario','pregunta','correcta','autor')

class BotoSerializer(serializers.HyperlinkedModelSerializer):
    autor= serializers.StringRelatedField()
    comentario= serializers.StringRelatedField()
    class Meta:
        model = Boto
        fields = ('comentario','botos','autor')
