from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Cart, Order, Customer
from products.models import Quentinha
from .forms import Phone_data, customer_data
from django.contrib.auth.mixins import LoginRequiredMixin


def cart_view(request):
    object = Quentinha.objects.all()
    try:
        cart = Cart.objects.get(user=request.user.id)
    except:
        cart = Cart.objects.get(user=request.COOKIES['device'])
    
    total_sum = 0
    for obj in cart.items.all():
        total_sum += obj.get_sum

    request.session['cart_id'] = cart.id
    context = {
        'object': object,
        'total': total_sum,
        'cart': cart.items.all()}
    
    return render(request, "cart.html", context)


    
    
## ADD THE SEARCH PASSED FROM PHONE PAGE TO FILTER DE DB IF ALREADY HAVE SOME DATA
def PhonePage(request):
    form = Phone_data(request.POST or None)
    context = {'form': form}
    
    if request.method == 'POST':
        form = Phone_data(request.POST)
        if form.is_valid():
            request.session['phone_numb'] = request.POST['phone']
            csutomer, created = Customer.objects.get_or_create(phone=request.session['phone_numb'])
            return redirect('cart:finish')
    
    return render(request, 'phone_number.html', context)

        
        
    
def FinishView(request):
    user = Customer.objects.get(phone=request.session.get('phone_numb'))
    
    try:
        cart = Cart.objects.get(user=request.user.id)
        cart = cart.items.all()
    except:
        cart = Cart.objects.get(user=request.COOKIES['device'])
        cart = cart.items.all()
    
    
    total_cart = 0
    for val in cart:
        total_cart += val.get_sum
        
        
    try:
        user.device = request.COOKIES['device']
    except:
        pass
    
    
    try:
        form = customer_data(initial={"name": user.name ,"address": user.address})
    except:
        form = customer_data()
    
    
    context = {'form': form ,
               'total': total_cart}
    
    
    cart = Cart.objects.get(user=request.COOKIES['device'])
    print(cart.id)
    
    
    if request.method == "POST":
        form = customer_data(request.POST)
        if form.is_valid():
            # form.save(commit=False)
            try:
                cart = Cart.objects.filter(user=request.COOKIES['device'])
                cart.update(status='Confirmed')
                
                user = Customer.objects.filter(phone=request.session.get('phone_numb'))
                user.update(phone=request.session.get('phone_numb'), name=form.cleaned_data.get('name'),
                            device=request.COOKIES['device'], address=form.cleaned_data.get('address'),
                            payment=form.cleaned_data.get('payment'))
                
                user = Customer.objects.get(phone=request.session.get('phone_numb'))
                cart = Cart.objects.get(user=request.COOKIES['device'])
                user.cart_activity.add(cart)
                
            except:
                Cart.objects.filter(user=request.user.id).update(status='Confirmed' )
                Customer.objects.filter(phone=request.session.get('phone_numb')).update(address=form.cleaned_data.get('address'))
            return render(request, 'thanks.html')
        
        
    return render(request, 'finish_order.html', context)
    