from django.contrib import admin

from appMy.models import *
from django.contrib.auth.models import User


   
admin.site.register(Category)
admin.site.register(Product)

