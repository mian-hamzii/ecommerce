from django.contrib.auth.models import User
from django.db import models

CHOICES = (
    ("available", "Available"),
    ("not available", "Not Available")
)


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='images')
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=CHOICES)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    description = models.CharField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)