from django.shortcuts import render
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
from django.shortcuts import get_object_or_404
# Create your views here.
class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj= get_object_or_404(
        queryset,
        pk= self.kwargs['pk'],
        )
        return obj
