from django.db import models
from django.contrib.auth.models import User
from product.models import ProductVariation
from utils.validators import validate_price, validate_quantity, validate_user
# Create your models here.

class WishItem(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default = 1)
    owner = models.ForeignKey('auth.User',related_name='wishwishitem', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.quantity} of {self.product}"

    def get_item_price(self):
        return self.quantity * self.product.discountPrice

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,validators = [validate_user])
    product = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1,validators = [validate_quantity])
    owner = models.ForeignKey('auth.User',related_name='Orderorderitem', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.quantity} of {self.product}"

    def get_item_price(self):
        return self.quantity * self.product.discountPrice

class Order(models.Model):
    user = models.ForeignKey(User, on_delete  = models.CASCADE,validators = [validate_user])
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default = False)
    delivered = models.BooleanField(default=False)
    name = models.CharField(max_length=250, null=True, blank=True)
    mobile = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    pincode = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True,blank=True,validators = [validate_price])
    quantity = models.SmallIntegerField(null=True, blank=True,validators = [validate_quantity])
    owner = models.ForeignKey('auth.User',related_name='orderorder', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.user.username
    
    def total_amount(self):
        total = 0
        for item in self.item.all():
            total += item.get_item_price()
        return total

    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs)