from django.db import models
import datetime
from .product import Product
from .costumer import Costumer

class Order(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    costumer = models.ForeignKey(Costumer ,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=200 , default='' , blank=True)
    phone = models.CharField(max_length=12 , default='', blank=True)
    date =  models.DateField(default=datetime.datetime.today)
