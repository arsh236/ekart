from django.contrib import admin
from ekart.models import Products,Catagories,Cart,Review
# Register your models here.
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Catagories)
admin.site.register(Review)
