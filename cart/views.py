from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Cart, Order
from products.models import Quentinha
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

# Create your views here.
def cart_view(request, *args, **kwargs):
    object = Quentinha.objects.all()
    orders = Order.objects.get(user=request.user.id)
    context = {'object': object}
    return render(request, "cart.html", context)


class CartView(LoginRequiredMixin, ListView):
    template_name="cart.html"
    queryset = Order.objects.all()
    # queryset = Order.order_by('-date_created')
        
    # def get(self, request):
    #     queryset = Cart.objects.filter(user=request.user)
    #     return queryset
    