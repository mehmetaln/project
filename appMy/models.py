from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



class Category(models.Model):
    title = models.CharField(("Başlık"), max_length=50)    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    title =models.CharField(("Başlık"), max_length=50)
    price =models.FloatField(("Fiyat"))
    text = models.TextField(("Text"), blank =True)
    img = models.ImageField(("İmage"), upload_to="product",default=0)
    
    def __str__(self):
        return self.title