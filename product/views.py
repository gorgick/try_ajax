from django.shortcuts import render

from .cart import Cart
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'product/base.html', {'products': products})


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product/product_detail.html', {'product': product})


def cart_view(request):
    cart = Cart(request)
    return render(request, 'product/cart-view.html', {'cart': cart})
