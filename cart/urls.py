from django.contrib import admin
from django.urls import path
from .views import cart_view, CartView

app_name='cart'
urlpatterns = [
    path('cart/', CartView.as_view(),  name='cart'),
]