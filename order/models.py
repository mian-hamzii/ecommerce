from django.db import models
from product.models import Product

CHOICES = (
    ('Approved', 'Approved'),
    ('Not Approved', 'Not Approved')
)


class Order(models.Model):
    status = models.CharField(max_length=20, choices=CHOICES, null=True)
    total = models.PositiveIntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price_each = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField()
    discount_price = models.FloatField()
    final_price = models.FloatField()
    total_price = models.FloatField()
