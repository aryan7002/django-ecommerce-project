from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.processor import Processor
from .models.gpu import GPU
from .models.costumer import Costumer
# Create your views here.

# Index page
def index(request):
    products = None
    categories = Category.get_all_categories()
    processors = Processor.get_all_processors()
    gpus = GPU.get_all_gpus()

    
    gpusID=request.GET.get('gpu')
    processorsID=request.GET.get('processor')
    categoryID=request.GET.get('category')


    if categoryID:
        products = Product.get_all_products_by_id(categoryID)
    elif processorsID:
        products = Product.get_all_products_by_processorID(processorsID)
    elif gpusID:
        products = Product.get_all_products_by_gpuID(gpusID)
    else:
        products = Product.get_all_products();

    data ={}
    data['products']= products
    data['categories'] = categories
    data['processors'] = processors
    data['gpus'] = gpus
    return render(request,'index.html',data)

#SignUp Page
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name =postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        costumer = Costumer(firstname = first_name,
                            lastname = last_name,
                            phone = phone,
                            email = email,
                            password = password)
        costumer.register()
        print(first_name,last_name,phone,email,password)
        return HttpResponse("Signup Sucess")

