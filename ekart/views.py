from django.shortcuts import render
from ekart.models import Catagories,Products
from rest_framework.response import Response
from ekart.serializer import CatagorySerialiezer
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import permissions,authentication

# Create your views here.

class CatagoryView(ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    serializer_class = CatagorySerialiezer
    queryset = Catagories.objects.all()
