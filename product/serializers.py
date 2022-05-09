from rest_framework import serializers
from product.models import Category, Color, Deal, Discount, Offer, Product, ProductVariation, Rating, SubCategory, product_variation_image
from django.contrib.auth.models import User


class CategorySerializer(serializers.Serializer):
    
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    image = serializers.ImageField(required=False) 
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Create and return a new `Todo_List` instance, given the validated data.
        """
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Todo_List` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.owner = validated_data.get('owner', instance.owner)
       
        instance.save()
        return instance


class SubCategorySerializer(serializers.Serializer):
    category = serializers.ReadOnlyField(source='get_category')
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    image = serializers.ImageField(required=False) 
    

    def create(self, validated_data):
        """
        Create and return a new `Todo_List` instance, given the validated data.
        """
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Todo_List` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
       
        instance.save()
        return instance

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name', 'colorCode']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['subCategory', 'size']

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['name', 'discount']

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['name', 'discount', 'image']

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ['name', 'discount', 'image']
class RatingSerializer(serializers.ModelSerializer):
    product_variation = serializers.CharField(source = 'product_variation.name')
    class Meta:
        model = Rating
        fields = ['product_variation', 'user', 'rating', 'review']
class ProductVariationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    product_name = serializers.CharField(source='product.name')
    color_name = serializers.CharField(source = 'color.name')
    product_ratings = RatingSerializer(many = True, read_only = True)
    class Meta:
        model = ProductVariation
        fields = ['product_name', 'slug', 'itemNumber', 'name', 'color_name','size','image1', 
        'image2','image3','image4','image5', 'price', 'discountPrice','stock', 'product_ratings', 'owner']
    def create(self, validated_data):
        product_ratings = validated_data.pop('product_ratings')
        product_rating = ProductVariation.objects.create(**validated_data)
        for rating in product_ratings:
            ProductVariation.objects.create(product_rating, **rating)
        return product_rating
class ProductSerializer(serializers.ModelSerializer):
    product_variations = ProductVariationSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['category', 'subCategory', 'gender', 'name', 'description','feauture1','feauture2', 
        'feauture2','feauture3','feauture4','feauture5', 'onSale', 'offer','discount','deal',
        'active','image', 'product_variations', 'owner']
    









