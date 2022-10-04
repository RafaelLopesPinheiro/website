
from distutils.command.clean import clean
import imp
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, FormView, CreateView, TemplateView
from .models import Acompanhamentos, Quentinha, Extra, Bebida, Feijoada
from .forms import Acompanha_Form, Book_form
from django.utils.functional import LazyObject as _
from cart.models import Cart, Order, Customer
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import datetime as dt
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request,"home.html", {})


class FeijoadaView(ListView):
    template_name = "feijoada_list.html"
    queryset = Feijoada.objects.all()


class QuentinhasListView(ListView):
    template_name = 'product_list.html'
    queryset = Quentinha.objects.all()
    

class QuentinhaDetailView(DetailView):
    template_name = 'product_detail.html'
    queryset = Quentinha.objects.all()
    form_class = Book_form
    
    def get_object(self):
        id_ = self.kwargs.get("id") ## ID of Quentinha
        return get_object_or_404(Quentinha, id=id_)


class BookView(FormView):
    template_name = 'finish_order.html'
    form_class = Book_form 
    success_url = '/'
    
    def form_valid(request, form):
        return super().form_valid(form)


class BebidasView(ListView):
    template_name = 'bebidas.html'
    queryset = Bebida.objects.all()
    print(queryset)
    

 ## FINISH_ORDER ## 
import json
@csrf_exempt
def product_create_view(request, id): #id
    object = Acompanhamentos.objects.all()
    item_id = Quentinha.objects.get(id=id)
    context = {
        'object': object,
        'item': item_id,
    }

    print('---'*15)
    if request.method == "POST":
        received_json = json.loads(request.body)
        clean_order = [j for j in received_json if j['amount'] != '0']          
        device = request.COOKIES['device']
        
        ## THIS ONE ONLY WORK WITH GET TO UPDATE ITEMS ON CART 
        try: 
            new_order = Order.objects.create(user=request.user.id, item=item_id, acomps_1=clean_order[0])
            device = request.user.id
        except:
            new_order = Order.objects.create(user=device, item=item_id, acomps_1=clean_order[0])
            pass


        for i,j in enumerate(clean_order):    
            if(i == 1):
                Order.objects.filter(user=device, item=item_id).update(acomps_2 = j)
            elif(i == 2):
                Order.objects.filter(user=device, item=item_id).update(acomps_3 = j)
            elif(i == 3):
                Order.objects.filter(user=device, item=item_id).update(acomps_4 = j)
                
        
        ## USE SET OR ADD METHOD TO SELECT THE ORDER RELATED WITH THE CART USER ##
        customer_cart, created = Cart.objects.get_or_create(user=device, status='Not Confirmed')
        customer_cart.items.add(new_order.id) 
        
        return render (request, 'cart.html', context)    

            
    return render (request, "product_detail.html", context)

