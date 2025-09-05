from django.urls import path
from .views import index, product_detail

app_name = 'product'

urlpatterns = [
    path('', index, name='index'),
    path('<str:pk>/', product_detail, name='detail'),
]