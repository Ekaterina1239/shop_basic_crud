from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', register, name='register'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
]
