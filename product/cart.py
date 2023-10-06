from django.shortcuts import redirect

from order.models import Order, OrderDetail
from product.models import Product


class Cart(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product):
        id = product.id
        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                'product_id': id,
                'name': product.title,
                'quantity': 1,
                'price': str(product.price),
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] = value['quantity'] + 1
                    self.save()
                    break
        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):

        for key, value in self.cart.items():
            if key == str(product.id):
                value['quantity'] = value['quantity'] - 1
                if value['quantity'] < 1:
                    return redirect('cart:cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True

    def get_total(self):
        total_price = 0
        total_items = 0
        for index, product in self.cart.items():
            total_price += product['quantity'] * int(product['price'])
            total_items += product['quantity']
        return {
            'total_price': total_price,
            'total_items': total_items,
        }

    def save_to_database(self):
        prices = self.get_total()
        order = Order(status="Approved", total=prices['total_price'])
        order.save()
        for id, item_detail in self.cart.items():
            product = Product.objects.get(id=id)
            order_detail = OrderDetail()
            order_detail.product = product
            order_detail.order = order
            order_detail.price_each = product.price
            order_detail.discount_price = 0
            order_detail.total_price = product.price * item_detail['quantity']
            order_detail.final_price = order_detail.total_price
            order_detail.quantity = item_detail['quantity']
            product.quantity -= item_detail['quantity']
            order_detail.save()
            product.save()
        self.clear()
