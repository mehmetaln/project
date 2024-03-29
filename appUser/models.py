from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Usermy(models.Model):
    user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE, null = True)
    tel = models.CharField(("Telefon"), max_length=50, default = "-")
    address = models.TextField(("Adres"), blank =True,)
    user_active = models.CharField(("Kullancı Dogrulama Linki"), max_length=50, default=0) # Kullanıcya email aracılı ile link göndermek için kullandıgımız kısım

    def __str__(self):
        return self.user.username

    def save(self):
      print("Usermy model save ====== ")
      super().save() #bu kısım usermyda ki degişikleri kaydetmemzie yarıyor mail göndeririken kullanmamız gerebilir 