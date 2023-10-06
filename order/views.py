from django.views.generic import ListView
from order.models import Order, OrderDetail


class OrderList(ListView):
    model = Order
    template_name = 'templates/order/order-list.html'


class OrderDetailView(ListView):
    model = OrderDetail
    template_name = 'templates/order/order-detail.html'
