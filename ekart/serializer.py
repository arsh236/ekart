from ekart.models import Catagories,Products,Cart
from rest_framework import serializers

class CatagorySerialiezer(serializers.ModelSerializer):
    is_active=serializers.BooleanField(read_only=True)
    class Meta:
        model=Catagories
        fields=['catagory_name','is_active']

class ProductSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    catagory=serializers.CharField(read_only=True)
    class Meta:
        model=Products
        fields='__all__'
    def validate_price(self,value):
        if value not in range(50,50000):
            raise serializers.ValidationError('invalid price')
        return value

    def create(self,validated_data):
        catagory=(self.context.get("catagory"))
        return Products.objects.create(**validated_data,catagory=catagory)

class CartSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=ProductSerializer(read_only=True)
    created_date=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)

    class Meta:
        model=Cart
        fields="__all__"
    def create(self,validated_data):
         user=self.context.get('user')
         product=self.context.get('product')
         return Cart.objects.create(**validated_data,product=product,user=user)

