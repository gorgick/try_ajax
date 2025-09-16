from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

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
    products = Product.objects.all()
    return render(request, 'product/cart-view.html', {'cart': cart, 'products': products})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == "post":
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product, product_qty)

        response = JsonResponse({'id': product_id, 'product_qty': product_qty, 'product': product.title})
        return response
