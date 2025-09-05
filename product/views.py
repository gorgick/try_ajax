from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'product/base.html', {'products': products})


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product/product_detail.html', {'product': product})