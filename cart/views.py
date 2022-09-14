from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Cart
# Create your views here.

def cart_view(request, *args, **kwargs):
    return render(request, "cart.html", {})


class CartView(ListView):
    template_name="cart.html"
    queryset = Cart.objects.all()
    