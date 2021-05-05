from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from store.models.product import Product
from store.models.category import Category
from store.models.processor import Processor
from store.models.gpu import GPU
from store.models.costumer import Costumer
from django.views import View

class Login(View):
    def get(self, request):
        return render(request,'login.html')
    def post(self , request):

        error_message = None
        email = request.POST.get('email')
        password = request.POST.get('password')
        costumer =Costumer.get_costumer_by_email(email)
        if costumer:
            if password == costumer.password:
                request.session['costumer'] = costumer.id
                
                return redirect('homepage')
            else:
                error_message = "Email or password Invalid"

        else:
            error_message = 'Email or Password Invalid '

        print(email,password)
        return render(request,'login.html',{'error':error_message})

def logout(request):
    request.session.clear()
    return redirect('login')