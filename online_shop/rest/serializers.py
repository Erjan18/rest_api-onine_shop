from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id','endpoint']

class ProductToOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductToOorder
        fields = ['id','products','order']

class OrderSerializer(serializers.ModelSerializer):
    endpoint = EndpointSerializer(many=True)
    to_order = ProductToOrderSerializer(many=True,read_only=True)
    class Meta:
        model = Order
        fields = ['id','to_order','start_date','end_date','status','endpoint']


    def create(self,validated_data):
        endpoints = validated_data.pop['endpoint']
        order = Order.objects.create(**validated_data)
        for endpoint in endpoints:
            Address.objects.create(order=order,**endpoint)
        return order

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status',instance.status)
        endpoints = validated_data.pop('endpoint')
        for endpoint in endpoints:
            if endpoint.id not in endpoint:
                endpoint.delete()
                Address.objects.delete(**endpoint)
            Address.objects.update(**endpoint)
        instance.save()
        return instance









