import logging
from django.shortcuts import render
from django.views import View


from product.models import Category, Color, Deal, Discount, Offer, Product, ProductVariation, Rating, Size, SubCategory
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import permissions,status, generics
from rest_framework.decorators import APIView
from django.views.decorators.csrf import csrf_exempt
from product.permissions import IsOwnerOrReadOnly
from product.serializers import CategorySerializer, ColorSerializer, DealSerializer, DiscountSerializer, OfferSerializer, ProductSerializer, ProductVariationSerializer, RatingSerializer, SizeSerializer, SubCategorySerializer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework import viewsets
# Create your views here.
logger = logging.getLogger(__name__)
class category(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class category_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class subcategory(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class subcategory_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
   
@csrf_exempt
def color(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        colors = Color.objects.all()
        serializer =ColorSerializer(colors, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ColorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    


@csrf_exempt
def color_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        color = Color.objects.get(pk=pk)
    except Color.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ColorSerializer(color)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ColorSerializer(color, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        color.delete()
        return HttpResponse(status=204)

@csrf_exempt
def size(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        size = Size.objects.all()
        serializer =SizeSerializer(size, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ColorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def size_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        size = Size.objects.get(pk=pk)
    except Size.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SizeSerializer(size)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SizeSerializer(size, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        size.delete()
        return HttpResponse(status=204)

class DiscountViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DiscountViewSet_detail(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class OfferViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class OfferViewSet_detail(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class DealViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DealViewSet_detail(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    logger.debug('Attempting to connect to API')
    queryset = Product.objects.all()
    if queryset == []:
        logger.warning('Queryset is empty! Please fill it')
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductViewSet_detail(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    logger.debug('Attempting to connect to API')
    queryset = Product.objects.all()
    if queryset == []:
        logger.warning('Queryset is empty! Please fill it')
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    

class ProductVariationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = ProductVariation.objects.all()
    serializer_class = ProductVariationSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductVariationViewSet_detail(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = ProductVariation.objects.all()
    serializer_class = ProductVariationSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class rating(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class rating_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]





class SearchProduct(APIView):
    def get(self, request, format=None):
        
        cat = Product.objects.all()
        if request.path == '/product/search/Men/':
            logger.debug('Searching for Men products')
            cat = Product.men_objects.all()
            if cat.exists():
                logger.info('Found products for Men')
            else:
                logger.info('Oops not found products for Men') 
        elif request.path == '/product/search/Women/':
            logger.debug('Searching for Women products')
            cat = Product.women_objects.all()
            if cat.exists():
                logger.info('Found products for Women')
            else:
                logger.info('Oops not found  products for Women') 
        elif request.path == '/product/search/active/':
            logger.debug('Searching for active products')
            cat = Product.active_objects.all()
            if cat.exists():
                logger.info('Found active products')
            else:
                logger.info('Oops not found active products')
        elif request.path == '/product/search/onsale/':
            logger.debug('Searching for onSale products')
            cat = Product.onSale_objects.all()
            if cat.exists():
                logger.info('Found onSale products')
            else:
                logger.info('Oops not found onSale products')
               
        else:
            pass
        serializer = ProductSerializer(cat, many =True)
        
        return JsonResponse(serializer.data, safe =False)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SearchProductVariation(APIView):
    def get(self, request, format=None):
        
        cat = ProductVariation.objects.all()
        if request.path == '/product/search/cheap/':
            logger.debug('Searching for cheap products')
            cat = ProductVariation.cheap_objects.all()
            if cat.exists():
                logger.info('Found cheap products')
            else:
                logger.info('Oops not found cheap products')
        elif request.path == '/product/search/expensive/':
            logger.debug('Searching for expensive products')
            cat = ProductVariation.expensive_objects.all()
            if cat.exists():
                logger.info('Found expensive products')
            else:
                logger.info('Oops not found expensive products')
        elif request.path == '/product/search/best/':
            logger.debug('Searching for best products')
            cat = ProductVariation.objects.all().filter(product_ratings__gte=4)
            if cat.exists():
                logger.info('Found best products')
            else:
                logger.info('Oops not found best products')
        else:
            pass
        serializer = ProductVariationSerializer(cat, many =True)
        
        return JsonResponse(serializer.data, safe =False)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]










