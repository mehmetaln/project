# Generated by Django 5.0.2 on 2024-02-09 07:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usermy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(default='-', max_length=50, verbose_name='Telefon')),
                ('address', models.TextField(blank=True, verbose_name='Adres')),
                ('profile_image', models.ImageField(default='appMy/static/image/images.png', max_length=200, upload_to='profil', verbose_name='Profil Resmi')),
                ('user_active', models.CharField(default=0, max_length=50, verbose_name='Kullancı Dogrulama Linki')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]