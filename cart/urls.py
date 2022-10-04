from django.contrib import admin
from django.urls import path
from .views import cart_view, CartView
from django.contrib.auth.decorators import login_required


app_name='cart'
urlpatterns = [
    path('cart/', CartView.as_view(),  name='cart'),
    path('cart2/', cart_view)
]