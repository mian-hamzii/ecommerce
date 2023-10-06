from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product-list'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('create-product', views.CreateProduct.as_view(), name='create-product'),
    path('brand-create', views.BrandCreate.as_view(), name='brand-create'),
    path('brand-list', views.BrandList.as_view(), name='brand-list'),
    path('category-create', views.CreateCategory.as_view(), name='category-create'),
    path('category-list', views.CategoryDetail.as_view(), name='category-list'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('save/', views.save, name='save'),
    path("product/<int:pk>/", views.BrandDetailView.as_view(), name="product")
]
