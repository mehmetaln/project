# Generated by Django 4.2.7 on 2024-01-30 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
