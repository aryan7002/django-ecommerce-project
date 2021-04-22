from django.contrib import admin
from django.urls import path
from .views import index, login, signup

urlpatterns = [
    path('', index.index, name='homepage'),
    path('signup', signup.signup, name='signup'),
    path('login', login.Login.as_view(), name='login'),
]
