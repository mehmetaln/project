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
    randomproductlist= Product.objects.all().order_by("?")

    context = {
        "category_list":category_list,
        "firstproducts":firstproducts[:4],
        "secondproducts":secondproducts[4:6],
        "randomproductlist":randomproductlist[2:6],  
    }
    return render(request,"index.html",context)

def allPage(request):
    products_list = Product.objects.all()
    context ={
        "product_list":products_list,
    }
    return render(request, "allpage.html", context)

def blogPage(request):
    blog_list = Blog.objects.all()
    randomproductlist= Product.objects.all().order_by("?")    
    
    context = {
        "blog_list":blog_list,
        "randomproductlist":randomproductlist[6:10],  
    }
    return render(request,"blog.html",context)

def blogdetailPage(request,bid):
    blog_list = Blog.objects.filter(id=bid)
    randomproductlist= Product.objects.all().order_by("?")
    
    context= {
        "blog_list":blog_list,
        "randomproductlist":randomproductlist[7:11],
    }
    return render(request, "blogdetail.html", context)
def contactPage(request):
    

    context = {
  

    }
    
    return render(request,"contact.html", context)