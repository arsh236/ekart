from django.shortcuts import render
from ekart.models import Catagories,Products
from ekart.serializer import CatagorySerialiezer,ProductSerializer,CartSerializer
from rest_framework.response import Response
from rest_framework import permissions,authentication
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.decorators import action
# Create your views here.

#localhost:8000/ekart/categories/
class CatagoryView(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CatagorySerialiezer
    queryset = Catagories.objects.all()

##localhost:8000/ekart/categories/{id}/add_product
    @action(methods=["POST"],detail=True)
    def add_product(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cat=Catagories.objects.get(id=id)
        serializer=ProductSerializer(data=request.data,context={"catagory":cat})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

#localhost:8000/ekart/catagories/{id}/get_products
    @action(methods=["GET"],detail=True)
    def get_products(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cat=Catagories.objects.get(id=id)
        prdt=cat.products_set.all()
        serializer=ProductSerializer(prdt,many=True)
        return Response(data=serializer.data)

#localhost:8000/ekart/products/

class ProductView(ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def list(self,request,*args,**kwargs):
        all_products=Products.objects.all()
        serializer=ProductSerializer(all_products,many=True)
        return Response(data=serializer.data)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        prdt=Products.objects.get(id=id)
        serializer=ProductSerializer(prdt,many=False)
        return Response(data=serializer.data)

    #localhost:8000/ekart/products/{id}/add_cart
    @action(methods=["POST"],detail=True)
    def add_cart(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        user=request.user
        prdt=Products.objects.get(id=id)
        serializer=CartSerializer(data=request.data,context={'user':user,'product':prdt})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

