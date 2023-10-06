from django.contrib import admin
from inventory.models import Vendor, Stock


# @receiver(pre_save, sender=Stock)
# def qty(sender, instance, **kwargs):
#     product = instance.product
#     product. quantity += instance. quantity
#     product.save()
admin.site.register(Vendor)
admin.site.register(Stock)
