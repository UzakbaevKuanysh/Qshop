from rest_framework import serializers
from order.models import Order, OrderItem
from django.contrib.auth.models import User



class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.CharField(read_only=True,source = 'product.name')
    user = serializers.CharField(read_only=True,source = 'user.username')
    class Meta:
        model = OrderItem
        fields = ['user', 'product', 'quantity']
    
class OrderSerializer(serializers.ModelSerializer):
    
    
    items = OrderItemSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ['user', 'items', 'ordered', 'delivered', 'name', 
        'mobile', 'email','address', 'city', 'pincode', 'price', 'quantity']