from django.urls import reverse
from django.views.generic import ListView, CreateView

from inventory.form import StockCreateForm, VendorCreateForm
from inventory.models import Vendor, Stock


class VendorList(ListView):
    model = Vendor
    template_name = 'templates/stock/vendor-list.html'


class CreateVendor(CreateView):
    model = Vendor
    form_class = VendorCreateForm

    def get_success_url(self):
        return reverse('vendor-list')


class StockList(ListView):
    model = Stock
    template_name = 'templates/stock/stock-list.html'


class CreateStock(CreateView):
    model = Stock
    form_class = StockCreateForm

    def form_valid(self, form):
        resp = super(CreateStock, self).form_valid(form)
        product = self.object.product
        product.quantity = product.quantity + self.object.quantity
        product.save()
        return resp

    def get_success_url(self):
        return reverse('stock-list')
