from django.contrib import admin
from django.urls import path
from .views import  login, signup
from .views.index import Index

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', signup.signup, name='signup'),
    path('login', login.Login.as_view(), name='login'),
]
