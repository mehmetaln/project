
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
    
    
    
    
    
  # USER
  path('registerPage/', registerPage, name="registerPage")
  
  
] + static (settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
