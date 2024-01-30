# from django.core.mail import send_mail #mail gönderebilmemzi için gerekli  
# from project.settings import EMAIL_HOST_USER 
from django.shortcuts import render, redirect
from appUser.models import *
from appMy.models import *
from django.contrib import messages
from django.contrib.auth.models import User




def indexPage(request):
    category_list =Category.objects.all()
    firstproducts =Product.objects.all()   
    secondproducts =Product.objects.all() 

    context = {
        "category_list":category_list,
        "firstproducts":firstproducts[:4],
        "secondproducts":secondproducts[4:7],
    }
    return render(request,"index.html",context)
