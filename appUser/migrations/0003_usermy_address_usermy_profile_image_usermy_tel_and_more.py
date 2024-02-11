# Generated by Django 5.0.2 on 2024-02-11 10:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0002_remove_usermy_address_remove_usermy_profile_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usermy',
            name='address',
            field=models.TextField(blank=True, default=0, verbose_name='Adres'),
        ),
        migrations.AddField(
            model_name='usermy',
            name='profile_image',
            field=models.ImageField(default='appMy/static/image/images.png', max_length=200, upload_to='profil', verbose_name='Profil Resmi'),
        ),
        migrations.AddField(
            model_name='usermy',
            name='tel',
            field=models.CharField(default='-', max_length=50, verbose_name='Telefon'),
        ),
        migrations.AddField(
            model_name='usermy',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
    ]