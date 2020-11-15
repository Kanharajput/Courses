from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('form', views.form,name = 'form'),
    path('login',views.login ,name = "login"),
    path('logout' , views.logout ,name = "logout")
]
