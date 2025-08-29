from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'product/base.html')
