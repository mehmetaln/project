# Generated by Django 5.0.2 on 2024-02-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0008_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='text',
            field=models.TextField(blank=True, default=0, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default=0, max_length=150, verbose_name='Başlık'),
        ),
    ]
