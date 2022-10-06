from django.contrib import admin
from django.urls import path
from .views import FinishView, cart_view, CartView
from django.contrib.auth.decorators import login_required


app_name='cart'
urlpatterns = [
    path('cart/', cart_view,  name='cart'),
    path('finish/', FinishView.as_view(), name='finish'),
    
]