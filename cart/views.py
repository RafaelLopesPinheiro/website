from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Cart, Order
from products.models import Quentinha
from .forms import customer_data
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def cart_view(request, *args, **kwargs):
    object = Quentinha.objects.all()
    # orders = Order.objects.get(user=request.user.id).get_sum
    try:
        cart = Cart.objects.get(user=request.user.id)
    except:
        cart = Cart.objects.get(user=request.COOKIES['device'])
    
    total_sum = 0
    for obj in cart.items.all():
        total_sum += obj.get_sum


    context = {
        'object': object,
        'total': total_sum,
        'cart': cart.items.all()}
    
    return render(request, "cart.html", context)


class CartView(LoginRequiredMixin, ListView):
    template_name="cart.html"
    queryset = Order.objects.all()
    # queryset = Order.order_by('-date_created')
        
    # def get(self, request):
    #     queryset = Cart.objects.filter(user=request.user)
    #     return queryset
    
    
    
    
# class FinishView(ListView):
#     template_name = 'finish_order.html'
#     queryset = customer_data()
    

        
        
        
    
def FinishView(request):
    form = customer_data(request.POST or None)
    context = {'form': form }
    
    if request.method == "POST":
        form = customer_data(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return render(request, 'thanks.html')
        
        
    return render(request, 'finish_order.html', context)
    