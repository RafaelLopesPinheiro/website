
from distutils.command.clean import clean
import imp
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, FormView, CreateView, TemplateView
from .models import Acompanhamentos, Quentinha, Extra, Bebida, Feijoada
from .forms import Acompanha_Form, Book_form
from django.utils.functional import LazyObject as _
from cart.models import Cart, Order
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
    
    
    
@login_required
def product_create_view(request, id):
    form = Book_form(request.POST or None)
    object = Quentinha.objects.get(id=id)
    context = {
        'form': form,
        'object': object,
    }
    
    if request.method == "POST":
        form = Book_form(request.POST)
        
        if form.is_valid() and form.cleaned_data:
            print(form.cleaned_data.get('acompanhamentos'))
            Order.objects.create(user=request.user, acomps=form.cleaned_data,
                                 acomps_1=form.cleaned_data, item=object)
            return render (request, "cart.html", context)
        else:
            print(form.errors)
            
            
    return render (request, "product_detail.html", context)





 ## FINISH_ORDER ## 
from django.contrib.sessions.models import Session
import json
@csrf_exempt
def product_create_view2(request, id): #id
    object = Acompanhamentos.objects.all()
    item_id = Quentinha.objects.get(id=id)
    context = {
        'object': object,
        'item': item_id,
    }

    print(item_id)
    
    if request.method == "POST":
        received_json = json.loads(request.body)
        clean_order = [j for j in received_json if j['amount'] != '0']
        # clean_order = [dict([a, int(x)] for a, x in b.items() if a == 'amount') for b in clean_order]
          
                                 
        print('-='*20)
        
        # THIS ONE ONLY WORK WITH GET TO UPDATE ITEMS ON CART 
        customer_cart = Cart.objects.get(id=request.user.id)
        # customer_cart.items.set([105])  
        print(customer_cart)
        
        
        ## THIS ONLY WORK WITH FILTER 
        
        Cart.objects.filter(id=request.user.id).update(status='Confirmed') 
        
        
        Order.objects.create(user=request.user.id, acomps_1=clean_order[0],item=item_id )# item=item_id )
        for i,j in enumerate(clean_order):    
            if(i == 1):
                Order.objects.filter(user=request.user.id, item=item_id).update(acomps_2 = j)
            elif(i == 2):
                Order.objects.filter(user=request.user.id, item=item_id).update(acomps_3 = j)
            elif(i == 3):
                Order.objects.filter(user=request.user.id, item=item_id).update(acomps_4 = j)
        print('-='*20)
        
        
        ## CREATE CART AND ADD FIRST ITEMS SELECTED ## 
        # teste = Cart.objects.get(id=request.user.id)
        # teste.items.set([56,57])
        # print(Cart.objects.filter(id=request.user.id))

        ## NEED TO CREATE CART OBJECT FIRST THEN ADD ORDER TO THE CART ##
        
        return render (request, 'cart.html', context)    
    
    ## GETTING USER ID FROM SESSION TO CREATE A CART RELATED ## 
    s = Session.objects.get(pk='bn3v446cxq92sf3t33tvk75j3c7u4wks')
    s1 = Session.objects.get(pk='e4jtqmr1urk0c45wlhh1sg7d4or038tr')
    # print(s.get_decoded())
    # print(s1.get_decoded())    
    if '_auth_user_hash' in s.get_decoded():
        idn = s.get_decoded()['_auth_user_id']
        # print(f'your user is: {idn}')
            
    return render (request, "finish_order.html", context)

