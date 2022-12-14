from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, FormView, CreateView, TemplateView
from .models import Acompanhamentos, Quentinha, Extra, Bebida, Feijoada
from .forms import Acompanha_Form, Bebidas_form, Book_form
from django.utils.functional import LazyObject as _
from cart.models import Cart, Order, Customer
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request,"home.html", {})


class FeijoadaView(ListView):
    template_name = "feijoada_list.html"
    queryset = Feijoada.objects.all()


class QuentinhasListView(ListView):
    template_name = 'product_list.html'
    queryset = Quentinha.objects.all()
    

class BebidasView(ListView):
    template_name = 'bebidas.html'
    queryset = Bebida.objects.all()
    print(queryset)
    


def bebidas_detail_view(request, id):
    template_name = 'bebidas_detail.html'
    queryset = Bebida.objects.all()
    form = Bebidas_form(request.POST or None)
    context = {
        'bebidas': queryset,
        'form': form
    }
    
    
    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data['bebidas'])
            device = request.COOKIES['device']            
            cart, created = Cart.objects.get_or_create(user=device)

                    
    
    return render(request, template_name, context)



@csrf_exempt
def product_create_view(request, id):
    """
    Create order with items selected and pass acomps attached to database
    """
    
    object = Acompanhamentos.objects.all()
    item_id = Quentinha.objects.get(id=id)
    context = {
        'object': object,
        'item': item_id,
    }

    if request.method == "POST":
        received_json = json.loads(request.body)
        clean_order = [j for j in received_json if j['amount'] != '0']          
        device = request.COOKIES['device']
        
        
        new_order = Order.objects.create(user=device, item_ordered=item_id, acomps_1=clean_order[0])
        Order.objects.filter(pk=new_order.id).update(order_id= "Order #" + str(new_order.id))


        for i,j in enumerate(clean_order):    
            if(i == 1):
                Order.objects.filter(pk=new_order.id, item_ordered=item_id).update(acomps_2 = j)
            elif(i == 2):
                Order.objects.filter(pk=new_order.id, item_ordered=item_id).update(acomps_3 = j)
            elif(i == 3):
                Order.objects.filter(pk=new_order.id, item_ordered=item_id).update(acomps_4 = j)
                
        
        ## USE SET OR ADD METHOD TO SELECT THE ORDER RELATED WITH THE CART USER ##
        customer_cart, created = Cart.objects.get_or_create(user=device, status='Not Confirmed')
        customer_cart.items.add(new_order.id) 
        
        return redirect('cart:cart')    

            
    return render (request, "product_detail.html", context)

