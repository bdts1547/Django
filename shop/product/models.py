from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(default="", max_length=100)
    slug = models.CharField(max_length=100, default="")
    desc = models.TextField(default="")
    active = models.BooleanField(default=True)


class Product(models.Model):
    title = models.CharField(max_length=255, default="")
    desc = models.TextField(default="")
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="")
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(default=0)
    

