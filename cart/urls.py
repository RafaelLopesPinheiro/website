from django.contrib import admin
from django.urls import path
from .views import FinishView, cart_view, CartView, PhonePage
from django.contrib.auth.decorators import login_required


app_name='cart'
urlpatterns = [
    path('cart/', cart_view,  name='cart'),
    path('phone/', PhonePage, name='phone'),
    path('finish/', FinishView, name='finish'),
    
]