from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from store.models.product import Product
from store.models.category import Category
from store.models.processor import Processor
from store.models.gpu import GPU
from store.models.costumer import Costumer
from django.views import View

class Cart(View):
    def get(self, request):
        # use this if any error 
        #ids = list(request.session.get('cart').keys())
        #for x in ids:
        #    product = Product.get_all_products_by_id(x)
        #    return render(request,'cart.html',{'product':product})
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_ids(ids)
        print(products)
        return render(request,'cart.html')
    