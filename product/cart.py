
class Cart:

    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('session_key')
        if not cart:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product, product_qty):
        product_id = str(product.id)
        product_qty = product_qty
        if product_id not in self.__dict__['cart']:
            self.__dict__['cart'][product_id] = {'qty': product_qty, 'price': str(product.price)}
        self.__dict__['cart'][product_id]['qty'] = product_qty
        self.session.modified = True
        product_amount = product.amount - product_qty
        product.amount = product_amount
        product.save()
