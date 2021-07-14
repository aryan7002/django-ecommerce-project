from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from store.models.product import Product
from store.models.category import Category
from store.models.processor import Processor
from store.models.gpu import GPU
from store.models.costumer import Costumer
from store.models.orders import Order
from django.views import View

class OrderView(View):
    def get(self, request):
        costumer = request.session.get('costumer')
        orders = Order.get_orders_by_costumer(costumer)
        print(orders)
        return render(request,'orders.html',{'orders':orders})