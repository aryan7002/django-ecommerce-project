from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
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

    error_message = None

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

    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        value = {
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email
        }
        isExist = costumer.isExists()
        if isExist:
            error_message = "Email Already Registered"
        if not error_message:

            costumer.register()
            print(first_name,last_name,phone,email,password)
            return  redirect('homepage')
        else:
            data ={
                'error':error_message,
                'values':value
            }
            return render(request,'signup.html',data)


#Login Page 
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
