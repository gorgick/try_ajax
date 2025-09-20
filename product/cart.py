from decimal import Decimal


class Cart:

    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('session_key')
        if not cart:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def __iter__(self):
        for x in self.cart:
            yield self.cart[x]

    def get_price(self):
        for el in self.__dict__['cart']:
            print((int(self.__dict__['cart'][el]['qty']) * Decimal(self.__dict__['cart'][el]['price'])))
            self.__dict__['cart'][el]['sum_for_amount'] = str(
                int(self.__dict__['cart'][el]['qty']) * Decimal(self.__dict__['cart'][el]['price']))
        print(self.__dict__['cart'])

    def add(self, product, product_qty):
        product_id = str(product.id)
        product_qty = product_qty
        if product_id not in self.__dict__['cart']:
            self.__dict__['cart'][product_id] = {'qty': str(product_qty), 'price': str(product.price),
                                                 'title': product.title}
        else:
            self.__dict__['cart'][product_id]['qty'] = str(
                int(self.__dict__['cart'][product_id]['qty']) + int(product_qty))
        self.session.modified = True
        product_amount = product.amount - int(product_qty)
        product.amount = product_amount
        product.save()

    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.__dict__['cart']:
            print(self.__dict__['cart'][product_id]['qty'])
            product.amount += int(self.__dict__['cart'][product_id]['qty'])
            product.save()
            del self.__dict__['cart'][product_id]
            self.session.modified = True
