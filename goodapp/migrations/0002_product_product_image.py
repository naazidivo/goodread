# Generated by Django 3.0.7 on 2020-07-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to='goodapp/images'),
        ),
    ]
