from django.utils import timezone
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField('date created')
    date_modified = models.DateTimeField('date modified', default=timezone.now())

    def __str__(self):
        return self.name
