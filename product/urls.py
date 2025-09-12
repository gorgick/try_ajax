from django.urls import path
from .views import index, product_detail, cart_view, cart_add

app_name = 'product'

urlpatterns = [
    path('', index, name='index'),
    path('cart/', cart_view, name='cart-view'),
    path('add/', cart_add, name='add-to-cart'),
    path('<int:pk>/', product_detail, name='detail'),
]