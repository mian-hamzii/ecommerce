from django.urls import path
from . import views

urlpatterns = [
    path('order-list', views.OrderList.as_view(), name='order-list'),
    path('order-detail-list', views.OrderDetailView.as_view(), name='order-detail-list'),
]
