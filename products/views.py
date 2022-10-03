
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
    
    
    
# @login_required
# def product_create_view(request, id):
#     form = Book_form(request.POST or None)
#     object = Quentinha.objects.get(id=id)
#     context = {
#         'form': form,
#         'object': object,
#     }
    
#     if request.method == "POST":
#         form = Book_form(request.POST)
        
#         if form.is_valid() and form.cleaned_data:
#             print(form.cleaned_data.get('acompanhamentos'))
#             Order.objects.create(user=request.user, acomps=form.cleaned_data,
#                                  acomps_1=form.cleaned_data, item=object)
#             return render (request, "cart.html", context)
#         else:
#             print(form.errors)

#     return render (request, "product_detail.html", context)




 ## FINISH_ORDER ## 
from django.contrib.auth.base_user import AbstractBaseUser
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
    # print(request.user.customer)
    if request.method == "POST":
        received_json = json.loads(request.body)
        clean_order = [j for j in received_json if j['amount'] != '0']          
                        
        device = request.COOKIES['device']
        ## THIS ONE ONLY WORK WITH GET TO UPDATE ITEMS ON CART 

        try: 
            new_order = Order.objects.create(user=request.user.id, item=item_id)

        except:
            pass
            # device = request.COOKIES['device']
            # customer, created = Customer.objects.get_or_create(device=device)
            
        # customer_cart.items.set([105]) 
        new_order = Order.objects.create(user=device, item=item_id, acomps_1=clean_order[0])

        ## THIS ONLY WORK WITH FILTER 
        # Cart.objects.filter(id=request.user.id).update(status='Confirmed') 
       
       
        # new_order, created = Order.objects.get_or_create(user=request.user.id, item=item_id, acomps_1=clean_order[0])
        for i,j in enumerate(clean_order):    
            if(i == 1):
                Order.objects.filter(user=device, item=item_id).update(acomps_2 = j)
            elif(i == 2):
                Order.objects.filter(user=device, item=item_id).update(acomps_3 = j)
            elif(i == 3):
                Order.objects.filter(user=device, item=item_id).update(acomps_4 = j)
        print('-='*20)
        
        print(new_order.id)
        
        new_order.acomps_1 = clean_order[3]
        
        
        ## CREATE CART AND ADD FIRST ITEMS SELECTED ##  WORKING ! 
        # try:
        #     customer = request.user.id
        #     customer_cart, created = Cart.objects.get_or_create(user=customer)
        #     customer_cart.items.set([new_order.id])
        # except:
        #     customer_cart, created = Cart.objects.get_or_create(user=request.COOKIES['sessionid'])
        #     customer_cart.items.set([new_order.id])
            
            
            
        # customer_cart = Cart.objects.get(user=request.session.session_key)
        # customer_cart.items.add(new_order.id)
        # customer_cart.items.add(169)
        # customer_cart.items.clear()
        # print(customer_cart)
        
        
        return render (request, 'cart.html', context)    
    
    
    ## GETTING USER ID FROM SESSION TO CREATE A CART RELATED ## 

    
    # teste = request.session
    # teste['te'] = {'testando_session': 1231112}
    # print(Session.objects.get(pk='x4xnbgy61p7y4favuginzxxsedgoemme').get_decoded())


    # s = Session.objects.get(pk=request.session.session_key)
    # print(s)
    print('-+-'*15)
    # print(s.get_decoded())  
    # if '_auth_user_hash' in s.get_decoded():
    #     idn = s.get_decoded()['_auth_user_id']
        # print(f'your user is: {idn}')
            
    return render (request, "product_detail.html", context)

