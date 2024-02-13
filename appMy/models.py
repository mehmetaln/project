from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class People(models.Model):
    img = models.ImageField(("Başlık"), upload_to="people",)


class Category(models.Model):
    title = models.CharField(("Başlık"), max_length=100, default = 0)    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    title =models.CharField(("Başlık"), max_length=100, default = 0)
    price =models.FloatField(("Fiyat"), default = 0)
    text = models.TextField(("Text"), blank =True, default = 0)
    img = models.ImageField(("İmage"), upload_to="product",default=0)
    oldprice =models.FloatField(("Eski Fiyat"),default = 0)
    
    def __str__(self):
        return self.title
class Blog(models.Model):
    title = models.CharField(("Başlık"), max_length=150, default = 0)
    text = models.TextField(("Text"), blank =True, default = 0)

class Saglik(models.Model):
    img = models.ImageField(("Resim"), upload_to="saglik")
    title = models.CharField(("Baslık"), max_length=150)
    text = models.TextField(("text"))