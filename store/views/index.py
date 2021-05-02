from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.category import Category
from store.models.processor import Processor
from store.models.gpu import GPU
from store.models.costumer import Costumer
from django.views import View


# Create your views here.
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity -1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        
        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}

        products = None
        #request.session.get('cart').clear()
        categories = Category.get_all_categories()
        processors = Processor.get_all_processors()
        gpus = GPU.get_all_gpus()

        gpusID = request.GET.get('gpu')
        processorsID = request.GET.get('processor')
        categoryID = request.GET.get('category')

        if categoryID:
            products = Product.get_all_products_by_id(categoryID)
        elif processorsID:
            products = Product.get_all_products_by_processorID(processorsID)
        elif gpusID:
            products = Product.get_all_products_by_gpuID(gpusID)
        else:
            products = Product.get_all_products();

        data = {}
        data['products'] = products
        data['categories'] = categories
        data['processors'] = processors
        data['gpus'] = gpus
        return render(request, 'index.html', data)
