from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Cart, Order
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def cart_view(request):
    
    return render(request, "cart.html", {})


class CartView(LoginRequiredMixin, ListView):
    template_name="cart.html"
    queryset = Order.objects.all()
    # queryset = Order.order_by('-date_created')
    
    # def get(self, request):
    #     queryset = Cart.objects.filter(user=request.user)
    #     return queryset
    
    