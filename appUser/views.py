from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.db.models import Count
from django.core.mail import send_mail # bu fonksiyonu mail göndermek için kullanıyoruz views kısmında
from project.settings import EMAIL_HOST_USER # settingsden çektigimiz host kısmımız bunu send mail içerisinde kullanacağız
from django.utils.crypto import get_random_string # random string ifadeler getirmemize yarar () parantez içerisnde kaç haneli olmasını istediğimizi yazarız
from appUser.models import *

def loginPage(request):
    
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username = username , password = password)
        if user:
            login(request,user)
            messages.success(request,"Giriş Başarılı")
            return redirect("indexPage")
        else:
            messages.error(request, "Kullanıcı adı veya şifreniz yanlış")
    context = {}

    return render(request,"user/login.html", context)


def registerPage(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
    
        if fname and lname and email and username and password:
            if not User.objects.filter(username = username).exists(): 
                random_link =get_random_string(44)  # random linkimizin string kısmı 
                emaillink = "http://"+request.get_host()+"/emailActive/"+random_link #request.get_host methodu bize girişli olan kullanıcın host bilgilerini verir
                user = User.objects.create_user(first_name =fname, last_name = lname, username=username, email = email, password=password)
                user.is_active = False # kullanıcıyı oluştur ama aktif hale getirme diyoruz bu kısımda maili onayladıktan sonra aktif hale getireceğiz 
                user.save() # userı kaydet ama tabi aktif olarak degil yapmıza saglar

                
                usermy = Usermy(user =user, user_active =random_link) # Usermy içerisinde ki objeşleri buradaki viewsde lazım olan yerlere eşitliyoruz
                usermy.save() # usermy kısmına kaydediyoruz burada oneöli olan useravtivite
                
                send_mail(  # Bu kısmda ise mesajımızı düzenleyioruz  
                "Kayıdı tamamlamak için mailenize gelen linki onaylayınız", # Buraya başlık veya konu gelicek
                f"Lütfen email hesabınızı onaylayınız: {emaillink}", # Bu kısım mailde gözükecek Kısım
                EMAIL_HOST_USER, # Settingsden çektiğimiz olmassa olmaz host kısmız 
                [email], # Burası ilgili olan kullanıcın maili
                fail_silently=False, # bunu boşver
                )
                messages.success(request,"Kayıt işlemlerinin tamamlanması için lütfen maila adresinizi onaylayınjz")
            else:
                messages.error(request,"Bu Kullanıcı Adı ile kayıtlı bir üye var.")
        else:
            messages.error(request,"Tüm Alanları Doldurunuz")



    context={}
    return render(request, "user/register.html",context)

def emailActive(request,elink): # Bu ksımda maile bir gelen link onaylandıgını kontrol edecegiz e link değişkeni urlden geliyor
     # Eğer verilen 'elink' değeriyle eşleşen bir Usermy objesi varsa
    if Usermy.objects.filter(user_active = elink).exists(): # Bizim hali hazırda user_Active kısmını kontrol ediyoruz
        # Bu objeyi al
        myuser = Usermy.objects.get(user_active = elink) # burada user_Actşveye elink degişkenimiz tanımlıyoruz 
        #İlgili kullanıcının is_active özelliğini True olarak ayarla
        myuser.user.is_active = True # bu kısımda mailonaylandıktan sonra bu kısmı true çeviriyoruz
        # Kullanıcı değişikliklerini kaydet
        myuser.user.save() # burada tekrar kaydeiyoruz activesi true olacak şekilde 
        messages.success(request, "Emailiniz başarı ile Onaylandı")
    else:
        messages.error(request, "Geçersiz onay")
        
    return redirect("loginPage")  




def hesapPage(request):
    context = {}
    return render(request, "user/hesap.html", context)

# def logoutUser(request):
#     logout(request)
#     return redirect("indexPage")