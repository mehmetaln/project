
from django.contrib import admin
from django.urls import path
from appMy.views import *
from appUser.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage, name="indexPage"),
    path('allPage/', allPage, name="allPage"),
    path('blogPage/', blogPage, name="blogPage"),
    path('blogdetailPage/<bid>', blogdetailPage, name="blogdetailPage"),
    path('contactPage/', contactPage, name="contactPage"),
  
    
    
    
    
    
  # USER
  path('registerPage/', registerPage, name="registerPage"),
  path('emailActive/<elink>',emailActive, name='emailActive'),
  path('loginPage/', loginPage, name="loginPage"),
  path('hesapPage/', hesapPage, name="hesapPage"),
  
  
] + static (settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
