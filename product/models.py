from distutils.command.upload import upload
from math import ceil, floor, modf
from msilib.schema import Class
from django.contrib.auth.models import User
import re
from django.db import models
import os
from django.utils.text import slugify

from utils.validators import validate_category, validate_owner
# Create your models here.
def category_image(instance,filename):
    upload_to = '{}_files/'.format(instance.name)
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}_image.{}'.format(instance.name,ext)
    return os.path.join(upload_to, filename)
class Category(models.Model):
    name = models.CharField(max_length =100, validators = [validate_category])
    image = models.ImageField(upload_to = category_image)
    owner = models.ForeignKey('auth.User',related_name='category', on_delete=models.CASCADE, null=True, validators=[validate_owner])
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs)
    

def subcategory_image(instance, filename):
    upload_to = '{}_files/{}/'.format(instance.category.name,instance.name)
    ext = filename.split('.')[-1]
    #get filename
    if instance.name:
        filename = '{}_image.{}'.format(instance.name,ext)
    return os.path.join(upload_to, filename)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=subcategory_image, null=True, blank=True)

    def __str__(self):
        return str(self.category.name) + ' - ' + str(self.name)

class Color(models.Model):
    name = models.CharField(max_length=100)
    colorCode = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Size(models.Model):
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcategorySizes')
    size = models.CharField(max_length=100)

    def __str__(self):
        return str(self.subCategory.name) + ' - ' + str(self.size)
class Discount(models.Model):
    name = models.CharField(max_length=250)
    discount = models.PositiveIntegerField()

    def __str__(self):
        return self.name
def offer_image(instance, filename):
    upload_to = 'Offer_Files/'
    ext = filename.split('.')[-1]
    if instance.name:
        filename = '{}.{}'.format(instance.name,ext)
    return os.path.join(upload_to, filename)

class Offer(models.Model):
    name = models.CharField(max_length=250)
    discount = models.PositiveIntegerField()
    image = models.ImageField(upload_to =offer_image, null=True,blank=True)

    def __str__(self):
        return self.name
def deal_image(instance, filename):
    upload_to = 'Deal_Files/'
    ext = filename.split('.')[-1]
    if instance.name:
        filename = '{}.{}'.format(instance.name,ext)
class Deal(models.Model):
    name = models.CharField(max_length=250)
    discount = models.PositiveIntegerField()
    image = models.ImageField(upload_to = deal_image, null=True, blank=True)

    def __str__(self):
        return self.name

def product_image(instance, filename):
    upload_to = '{}_files/{}'.format(instance.category.name,instance.subCategory.name)
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name,ext)
    return os.path.join(upload_to,filename)
class OnSaleProduct(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(onSale = True )
class ActiveProduct(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active = True )
class MenProduct(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category = 6 )

class WomenProduct(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(category = 7 )


class Product(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    owner = models.ForeignKey('auth.User',related_name='products', on_delete=models.CASCADE, null=True)
    onSale_objects = OnSaleProduct()
    active_objects = ActiveProduct()
    men_objects = MenProduct()
    women_objects = WomenProduct()
    objects = models.Manager()
    category = models.ForeignKey(Category, on_delete= models.CASCADE,related_name='categoryProducts')
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcategoryproducts')
    gender = models.CharField(max_length=1, choices = GENDERS, default='M')
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length = 350, null = True, blank=True)
    feauture1 = models.CharField(max_length=250,null=True,blank=True,default='lorem')
    feauture2 = models.CharField(max_length=250,null=True,blank=True,default='lorem')
    feauture3 = models.CharField(max_length=250,null=True,blank=True,default='lorem')
    feauture4 = models.CharField(max_length=250,null=True,blank=True,default='lorem')
    feauture5 = models.CharField(max_length=250,null=True,blank=True,default='lorem')
    onSale = models.BooleanField(default = False)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE,null=True, blank=True)
    active = models.BooleanField(default = True)
    image = models.ImageField(upload_to = product_image, null=True)
    def __str__(self):
        return self.name
    def getGender(self):
        return self.get_gender_display()
    

    

                            







def product_variation_image(instance, filename):
    upload_to = '{}_files/{}/{}_variations/'.format(instance.product.category.name,
    instance.product.subCategory.name,
    instance.product.subCategory.name)
    ext = filename.split('.')[-1]
    #get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name,ext)
    return os.path.join(upload_to, filename)
class CheapPriceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price__lte=3000)
class ExpensivePriceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(price__gte=20000)
class ProductVariation(models.Model):
    owner = models.ForeignKey('auth.User',related_name='productvariation', on_delete=models.CASCADE, null=True)
    objects = models.Manager()
    expensive_objects = ExpensivePriceManager()
    cheap_objects = CheapPriceManager()
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name='product_variations')
    slug = models.CharField(max_length=350, null=True, blank=True)
    itemNumber = models.PositiveIntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to=product_variation_image, null=True, blank=True)
    image2 = models.ImageField(upload_to=product_variation_image, null=True, blank=True)
    image3 = models.ImageField(upload_to=product_variation_image, null=True, blank=True)
    image4 = models.ImageField(upload_to=product_variation_image, null=True, blank=True)
    image5 = models.ImageField(upload_to=product_variation_image, null=True, blank=True)  
    price = models.PositiveIntegerField()
    discountPrice = models.PositiveIntegerField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name

    def number(self):
        count = ProductVariation.objects.count()
        if count == 0:
            return 1
        else:
            last_object = ProductVariation.objects.order_by('-id')[0]
            return last_object.id + 1
    def get_discount_price(self):
        product = self.product
        if product.onSale:
            if product.discount:
                percent = product.discount.discount
            elif product.deal:
                percent = product.deal.discount
            elif product.offer:
                percent = product.offer.discount
            else:
                percent = 0
            price_red = (percent/100) * self.price
            price = self.price - price_red
            return price
        else:
            return self.price
    def save(self, *args, **kwargs):
        if not self.itemNumber:
            self.itemNumber = self.number()
        if not self.name:
            self.name = self.product.get_gender_display() + '-' + self.product.name + '-' + self.color.name + '-' + self.size.size
        if not self.slug:
            self.slug = slugify(self.name)
        self.discountPrice = self.get_discount_price()
        super(ProductVariation, self).save(*args, **kwargs)
class Rating(models.Model):
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE, related_name = 'product_ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_product_ratings')
    rating = models.SmallIntegerField(default = 3)
    review = models.CharField (max_length=80, default = 'Nice product')

    def __str__(self):
        return str(self.product_variation) + ' - ' + str(self.rating)



