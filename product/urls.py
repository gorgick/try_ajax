from django.urls import path
from .views import (index, product_detail, cart_view, cart_add, delete_product, gallery)

app_name = 'product'

urlpatterns = [
    path('', index, name='index'),
    path('cart/', cart_view, name='cart-view'),
    path('add/', cart_add, name='add-to-cart'),
    path('delete_product/', delete_product, name='delete-product'),
    path('gallery/', gallery, name='gallery'),
    path('<int:pk>/', product_detail, name='detail'),
]