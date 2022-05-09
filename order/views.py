import genericpath
from typing import Generic
from django.shortcuts import render
from order.models import Order, OrderItem
from django.http import HttpResponse
from order.serializers import OrderItemSerializer, OrderSerializer
from product.models import ProductVariation
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import logging
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import permissions,status, generics
from rest_framework.decorators import APIView

from order.permissions import IsOwnerOrReadOnly




class order(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
class order_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class orderitem(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class orderitem_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]




