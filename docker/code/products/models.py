from operator import mod
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dtCreated = models.DateTimeField('date created')
    dtModified = models.DateTimeField('date modified')
