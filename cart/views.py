from django.shortcuts import redirect, render
from django.urls import reverse
# from django.views.generic import ListView, DetailView
from .models import Cart, Order, Customer
from products.models import Quentinha
from .forms import Phone_data, customer_data


def cart_view(request):
    object = Quentinha.objects.all()
    
    # cart = Cart.objects.get(user=request.COOKIES['device'])
    
    try:
        cart = Cart.objects.get(user=request.user.id)
    except:
        cart = Cart.objects.get(user=request.COOKIES['device'])
 
 
    request.session['cart_id'] = cart.id
    context = {
        'object': object,
        'total': cart.get_total_sum,
        'cart_items': cart.items.all(),
        'bebidas': cart.bebida_choices.all(),
        'cart': cart}
    
    return render(request, "cart.html", context)
 
    
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
        
    except:
        cart = Cart.objects.get(user=request.COOKIES['device'])


    try:
        user.device = request.COOKIES['device']
    except:
        pass
    
    
    try:
        form = customer_data(initial={"name": user.name ,"address": user.address})
    except:
        form = customer_data()
    
    
    context = {'form': form ,
               'total': cart.get_total_sum}
    
    
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
    