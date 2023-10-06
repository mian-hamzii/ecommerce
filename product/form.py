from django import forms
from product.models import Product, Brand, Category


class ProductCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

    class Meta:
        model = Product
        fields = ['title',
                  'description',
                  'picture',
                  'price',
                  'quantity',
                  'status',
                  'brand',
                  'category']


class BrandCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BrandCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

    class Meta:
        model = Brand
        fields = ['name']


class CategoryCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"

    class Meta:
        model = Category
        fields = ['name']