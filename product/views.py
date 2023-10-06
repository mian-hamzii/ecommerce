from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView , DetailView
from django.shortcuts import redirect
from product.cart import Cart
from product.models import Product, Brand, Category
from product.form import ProductCreateForm, BrandCreateForm, CategoryCreateForm


class ProductList(ListView):
    model = Product
    template_name = 'templates/product/product_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['cart_total'] = Cart(self.request).get_total()
        return data

    def get_queryset(self, *args, **kwargs):
        queryset = super(ProductList, self).get_queryset()
        search = self.request.GET.get('product_name')
        if search:
            queryset = Product.objects.filter(title__icontains=search)
        return queryset


class CreateProduct(CreateView):
    model = Product
    form_class = ProductCreateForm

    def get_success_url(self):
        return reverse('product-list')


class BrandList(ListView):
    model = Brand
    template_name = 'templates/product/brand-list.html'

    def get_success_url(self):
        return reverse('product-list', kwargs={'pk': self.object_list.brand.pk})


class BrandDetailView(DetailView):
    model = Brand
    template_name = "templates/order/order-detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['products'] = Product.objects.filter(brand=self.kwargs['pk'])
        return data


class BrandCreate(CreateView):
    model = Brand
    form_class = BrandCreateForm
    template_name = 'product/brand_form.html'

    def get_success_url(self):
        return reverse('brand-list')


class CategoryDetail(ListView):
    model = Category
    template_name = 'templates/product/category-list.html'


class CreateCategory(CreateView):
    model = Category
    form_class = CategoryCreateForm

    def get_success_url(self):
        return reverse('category-list')


def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("product-list")


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("product-list")


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("product-list")


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("product-list")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("product-list")


def save(request):
    cart = Cart(request)
    cart.save_to_database()
    return redirect('product-list')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "templates/registration/register.html"
