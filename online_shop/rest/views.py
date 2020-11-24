from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['price','name']


class OrderView(APIView):

    def get(self,*args,**kwargs):
        orders = Order.objects.all()
        serializers = OrderSerializer(orders,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializers=OrderSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)

class UPDOrderView(APIView):

    def put(self,request,*args,**kwargs):
        order = Order.objects.get(id=kwargs['pk'])
        serializers = OrderSerializer(order,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'data':'seccess'})

    def delete(self,request,*args,**kwargs):
        order = Order.objects.get(id=kwargs['pk'])
        order.delete()
        return Response({'data':'seccess'})


class ProductToOrderView(APIView):

    def get(self,*args,**kwargs):
        orders = ProductToOorder.objects.all()
        serializers = ProductToOrderSerializer(orders,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializers= ProductToOrderSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)


