from django.contrib import admin
from django.urls import path
from .views import index,Login, signup

urlpatterns = [
    path('',index, name = 'homepage'),
    path('signup',signup),
    path('login',Login.as_view()),
]
