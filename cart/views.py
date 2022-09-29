from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Cart, Order
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# Create your views here.

def cart_view(request, *args, **kwargs):
    return render(request, "cart.html", {})


class CartView(LoginRequiredMixin, ListView):
    template_name="cart.html"
    queryset = Order.objects.all()
    # queryset = Order.order_by('-date_created')
    
    # def get(self, request):
    #     queryset = Cart.objects.filter(user=request.user)
    #     return queryset
    