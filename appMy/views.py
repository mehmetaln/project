from django.shortcuts import render, redirect
from appUser.models import *
from appMy.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail # bu fonksiyonu mail göndermek için kullanıyoruz views kısmında
from project.settings import EMAIL_HOST_USER # settingsden çektigimiz host kısmımız bunu send mail içerisinde kullanacağız
from django.db.models import Count # Bir karekteri kaç kez yazdıgımıza dair sorgular yapmmıza yarar
from django.db.models import Q # ve bağlacını kullanmamıza yarar baızyerlerde



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
    query = request.GET.get("query")
    print("Arama Sorgusu:", query)
    if query:
        products_list = products_list.filter(Q(title__icontains=query))
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

def detailPage(request,pid):
    product_detail = Product.objects.filter(id = pid)
    people_img = People.objects.all().order_by("?")
    saglik_list = Saglik.objects.all()
    comment_list = Comment.objects.filter(product = product_detail.first())
    
    
    if request.method == "POST":
        text = request.POST.get("text")
        submit = request.POST.get("submit")
        if product_detail.exists():
            product = product_detail.first()
            comment = Comment(text = text, product =product_detail.first(), user = request.user)
            comment.save()
    
    
    
    context = {
        "product_detail":product_detail,
        "people_img":people_img[:4],
        "saglik_list":saglik_list,
        "comment_list":comment_list,
    }
    return render(request,"detail.html",context)




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER

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
            'host_password': 'rvvoomrymvntzdgo',
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


