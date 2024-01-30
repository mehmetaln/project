# Generated by Django 4.2.7 on 2024-01-30 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('price', models.FloatField(verbose_name='Fiyat')),
                ('text', models.TextField(verbose_name='Text')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.category', verbose_name='kategori')),
            ],
        ),
    ]
