from ekart.models import Catagories,Products
from rest_framework import serializers

class CatagorySerialiezer(serializers.ModelSerializer):
    is_active=serializers.BooleanField(read_only=True)
    class Meta:
        model=Catagories
        fields=['catagory_name','is_active']
