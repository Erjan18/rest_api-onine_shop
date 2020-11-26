from django.db import models
from register import models as md1

class Product(models.Model):
    types =( ('black','black'),
            ('green','green'))
    name = models.CharField(max_length=50)
    tea_types = models.CharField(max_length=50,choices=types)
    price = models.IntegerField()
    size = models.IntegerField(default=0)
    tastes = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.tea_types

class Address(models.Model):
    endpoint = models.CharField(max_length=100)
    order = models.ForeignKey('Order',on_delete=models.SET_NULL,null=True,related_name='endpoint')

    def __str__(self):
        return self.endpoint

class Order(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True)
    status = models.BooleanField()
    account = models.ForeignKey(md1.Account,on_delete=models.SET_NULL,null=True)

class ProductToOorder(models.Model):
    order = models.ForeignKey('Order',on_delete=models.SET_NULL,null=True,related_name='to_order')
    products = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)





