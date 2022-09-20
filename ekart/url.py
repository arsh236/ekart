from ekart import views
from django.urls import path
from rest_framework.routers import DefaultRouter
r=DefaultRouter()
r.register('catagorees',views.CatagoryView)

urlpatterns=[




]+r.urls