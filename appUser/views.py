from django.shortcuts import render



def registerPage(request):
    
    
    
    context={}
    return render(request, "user/register.html",context)

