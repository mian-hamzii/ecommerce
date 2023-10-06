from django import forms
from inventory.models import Stock, Vendor


class StockCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StockCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

    class Meta:
        model = Stock
        fields = ['quantity', 'product', 'vendor']


class VendorCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VendorCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

    class Meta:
        model = Vendor
        fields = ['name', 'address', 'phone', ]



