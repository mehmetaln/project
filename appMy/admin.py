from django.contrib import admin

from appMy.models import *
from appUser.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

   


 
# class UsermyInline(admin.StackedInline):
#     model =Usermy
#     max_num =1
#     can_delete =False
    
# class CustomUser(UserAdmin):
#     inlines =[UsermyInline,]


admin.site.unregister(User)
admin.site.register(User,CustomUser)