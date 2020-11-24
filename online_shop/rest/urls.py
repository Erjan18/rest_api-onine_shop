from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('products/',ProductView.as_view(),name='product_list'),
    path('orders/',OrderView.as_view(),name='order_list'),
    path('pt_orders/',ProductToOrderView.as_view(),name='to_order'),
    path('modify_order/<int:pk>/',UPDOrderView.as_view()),


]