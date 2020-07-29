from django.contrib import admin

# Register your models here.
from .models import Product,BookComment,Popularpost,Author,Sahitya

admin.site.register((Product,BookComment,Popularpost,Author,Sahitya))