from django.db import models
from product.models import Product


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Stock(models.Model):
    date = models.DateTimeField(auto_now=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()