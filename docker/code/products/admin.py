from django.apps import AppConfig
from django.contrib import admin
from .models import Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)


class CategoryConfig(AppConfig):
    name = "Category"
    verbose_name = "Categories"

