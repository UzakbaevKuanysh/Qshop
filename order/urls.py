from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from order import views
app_name = 'order'

urlpatterns = [
  path('', views.order.as_view()),
  path('<int:pk>/', views.order_detail.as_view()),
  path('orderitem/', views.orderitem.as_view()),
  path('orderitem/<int:pk>/', views.orderitem_detail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)