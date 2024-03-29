# Generated by Django 5.0.2 on 2024-02-15 11:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0012_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sepet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adet', models.IntegerField(default=0, verbose_name='Adet')),
                ('toplam', models.FloatField(default=0, verbose_name='Toplam Fiyat')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
