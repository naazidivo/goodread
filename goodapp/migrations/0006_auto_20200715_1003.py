# Generated by Django 3.0.7 on 2020-07-15 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goodapp', '0005_auto_20200715_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcomment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodapp.Product'),
        ),
        migrations.AlterField(
            model_name='bookcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
