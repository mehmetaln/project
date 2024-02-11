from django.shortcuts import render, redirect
from appUser.models import *
from appMy.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail # bu fonksiyonu mail göndermek için kullanıyoruz views kısmında
from project.settings import EMAIL_HOST_USER # settingsden çektigimiz host kısmımız bunu send mail içerisinde kullanacağız



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




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER

@login_required
def contactPage(request):
    if request.method == 'POST':
        # Formdan gelen verileri al
        ad = request.POST.get('ad')
        eposta = request.POST.get('eposta')
        mesaj = request.POST.get('mesaj')

        # E-posta ayarlarını belirle
        email_settings = {
            'use_tls': True,
            'host': 'smtp.gmail.com',
            'port': 587,
            'host_user': EMAIL_HOST_USER,
            'host_password': 'rdkiozsfygwfcscp',
        }

        # E-posta gönderme işlemi
        send_mail(
            'Konu',
            f'Mesaj: {mesaj}\nGönderen: {ad}\nE-posta: {eposta}',
            'from@example.com',
            [EMAIL_HOST_USER],
            fail_silently=False,
            auth_user=email_settings['host_user'],
            auth_password=email_settings['host_password'],
        )

        # İstediğiniz başka bir işlemi gerçekleştirebilirsiniz, örneğin bir teşekkür sayfasına yönlendirme yapabilirsiniz.

    context = {}
    return render(request, "contact.html", context)
