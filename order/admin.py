from django.contrib import admin

from order.models import Order, OrderItem, WishItem

# Register your models here.
admin.site.register(WishItem)
admin.site.register(OrderItem)
admin.site.register(Order)