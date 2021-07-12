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

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        costumer = request.session.get('costumer')
        cart = request.session.get('cart')
        products = Product.get_products_by_ids(list(cart.keys()))
        print(address,phone,costumer,cart , products)
        for product in products:
            order = Order(costumer = Costumer(id = costumer),
                            product= product,
                            price = product.price,
                            address = address,
                            phone = phone,
                            quantity= cart.get(str(product.id)))
            order.save()
            request.session['cart'] = {} 
        print(request.POST)
        return redirect('cart')