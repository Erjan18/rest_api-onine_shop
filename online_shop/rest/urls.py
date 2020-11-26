from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('orders',OrderView)

urlpatterns = [
    path('products/',ProductView.as_view(),name='product_list'),
    path('pt_orders/',ProductToOrderView.as_view(),name='to_order'),
    path('modify_order/<int:pk>/',UPDOrderView.as_view()),
    path('',include(router.urls))

]