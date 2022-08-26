from django.contrib import admin
from django.urls import path
from .views import cart_view

app_name='cart'
urlpatterns = [
    path('cart/', cart_view),
]