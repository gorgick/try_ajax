from django.urls import path
from .views import index, product_detail, cart_view

app_name = 'product'

urlpatterns = [
    path('', index, name='index'),
    path('cart/', cart_view, name='cart-view'),
    path('<str:pk>/', product_detail, name='detail'),
]