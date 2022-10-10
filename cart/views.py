from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Cart, Order, Customer
from products.models import Quentinha
from .forms import Phone_data, customer_data
from django.contrib.auth.mixins import LoginRequiredMixin


def cart_view(request, *args, **kwargs):
    object = Quentinha.objects.all()
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
    
    
    
def PhonePage(request):
    form = Phone_data(request.POST or None)
    context = {'form': form}
    
    if request.method == 'POST':
        form = Phone_data(request.POST)
        if form.is_valid():
            
            request.session['phone_numb'] = request.POST['phone']
            print(request.session['phone_numb'])
            phone = request.session['phone_numb']
            customer, created = Customer.objects.get_or_create(phone=phone)
            print(customer)
            return redirect('cart:finish')
    
    return render(request, 'phone_number.html', context)

        
        
        
    
def FinishView(request):
    form = customer_data(request.POST or None)
    context = {'form': form }
    
    phone_numb = request.session.get('phone_numb')
    print('-*'*10)
    print(phone_numb)
    # print(customer_data(phone='(22) 22222-2222'))
    
    if request.method == "POST":
        form = customer_data(request.POST)
        if form.is_valid():
            form.phone = phone_numb
            form.save()
            print(form.cleaned_data)
            return render(request, 'thanks.html')
        
        
    return render(request, 'finish_order.html', context)
    