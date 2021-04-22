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

# Index page
def index(request):
    products = None
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


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):

        error_message = None
        email = request.POST.get('email')
        password = request.POST.get('password')
        costumer = Costumer.get_costumer_by_email(email)
        if costumer:
            if password == costumer.password:
                return redirect('homepage')
            else:
                error_message = "Email or password Invalid"

        else:
            error_message = 'Email or Password Invalid '

        print(email, password)
        return render(request, 'login.html', {'error': error_message})


