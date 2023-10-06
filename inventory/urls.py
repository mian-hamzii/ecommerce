from django.urls import path
from . import views

urlpatterns = [
    path('vendor-list', views.VendorList.as_view(), name='vendor-list'),
    path('create-vendor', views.CreateVendor.as_view(), name='create-vendor'),
    path('stock-list', views.StockList.as_view(), name='stock-list'),
    path('create-stock', views.CreateStock.as_view(), name='create-stock'),
]
