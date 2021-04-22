from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.category import Category
from store.models.processor import Processor
from store.models.gpu import GPU
from store.models.costumer import Costumer
from django.views import View


# SignUp Page
def signup(request):
    error_message = None

    postData = request.POST
    first_name = postData.get('firstname')
    last_name = postData.get('lastname')
    phone = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')

    costumer = Costumer(firstname=first_name,
                        lastname=last_name,
                        phone=phone,
                        email=email,
                        password=password)

    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        isExist = costumer.isExists()
        if isExist:
            error_message = "Email Already Registered"
        if not error_message:

            costumer.register()
            print(first_name, last_name, phone, email, password)
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
