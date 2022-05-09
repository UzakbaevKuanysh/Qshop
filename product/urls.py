from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from product import permissions, views
from product.views import DealViewSet, DealViewSet_detail, DiscountViewSet, DiscountViewSet_detail, OfferViewSet, OfferViewSet_detail, ProductVariationViewSet, ProductVariationViewSet_detail, ProductViewSet, ProductViewSet_detail, SearchProductVariation
app_name = 'product'
discount = DiscountViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
discount_detail = DiscountViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

offer = OfferViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
offer_detail = OfferViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

deal = DealViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
deal_detail = DealViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

product = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
product_detail = ProductViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    
})

productvariation = ProductVariationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
productvariation_detail = ProductVariationViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    
})

urlpatterns = [
  path('', product, name = 'product'),
  path('<int:pk>/', product_detail, name = 'product_detail'),
  path('category/', views.category.as_view()),
  path('category/<int:pk>/', views.category_detail.as_view()),
  path('subcategory/', views.subcategory.as_view()),
  path('subcategory/<int:pk>/', views.subcategory_detail.as_view()),
  path('color/', views.color),
  path('color/<int:pk>/', views.color_detail),
  path('size/', views.size),
  path('size/<int:pk>/', views.size_detail),
  path('discount/', discount, name='discount'),
  path('discount/<int:pk>/', discount_detail, name = 'discount_detail'),
  path('productvariation/', productvariation, name='productvariation'),
  path('productvariation/<int:pk>', productvariation_detail, name='productvariation_detail'),
  path('rating/', views.rating.as_view()),
  path('rating/<int:pk>/', views.rating_detail.as_view()),
  path('search/Men/', views.SearchProduct.as_view()),
  path('search/Women/', views.SearchProduct.as_view()),
  path('search/', views.SearchProduct.as_view()),
  path('search/active/', views.SearchProduct.as_view()),
  path('search/cheap/', views.SearchProductVariation.as_view()),
  path('search/onsale/', views.SearchProduct.as_view()),
  path('search/expensive/', views.SearchProductVariation.as_view()),
  path('search/best/', views.SearchProductVariation.as_view())
  
  

]
urlpatterns = format_suffix_patterns(urlpatterns)