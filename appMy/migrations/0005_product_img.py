# Generated by Django 4.2.7 on 2024-01-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_alter_product_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=0, upload_to='product', verbose_name='İmage'),
        ),
    ]
