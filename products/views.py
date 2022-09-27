
from distutils.command.clean import clean
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, FormView, CreateView, TemplateView
from .models import Acompanhamentos, Quentinha, Extra, Bebida, Feijoada
from .forms import Acompanha_Form, Book_form
from django.utils.functional import LazyObject as _
from cart.models import Cart, Order
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
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
    # object = Quentinha.objects.get('id')
    
    def get_object(self):
        id_ = self.kwargs.get("id") ## ID of Quentinha
        return get_object_or_404(Quentinha, id=id_)


    

class BookView(FormView):
    template_name = 'finish_order.html'
    form_class = Book_form 
    success_url = '/'
    
    def form_valid(request, form):
        return super().form_valid(form)
    
    # def get(self, request):
    #     id_ = request.GET.get('id')
    #     return render(request, self.template_name, {'post': get_object_or_404(Quentinha, pk=id_)})


    
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
                                 acomps_1=form.cleaned_data, item=Quentinha.objects.get(id=id))
            return render (request, "cart.html", context)
        else:
            print(form.errors)
            
            
    return render (request, "product_detail.html", context)



class BebidasView(ListView):
    template_name = 'bebidas.html'
    queryset = Bebida.objects.all()
    print(queryset)


from django.conf import settings
import json
@csrf_exempt
def product_create_view2(request, ): #id
    object = Acompanhamentos.objects.all()
    context = {
        'object': object,
    }

    if request.method == "POST":
        received_json = json.loads(request.body)
        clean_order = [j for j in received_json if j['amount'] != '0']
        # clean_order = [dict([a, int(x)] for a, x in b.items() if a == 'amount') for b in clean_order]
                                 
        print('-='*20)
        for i,j in enumerate(clean_order):
            print(j)


        ## CREATE CART AND ADD FIRST ITEMS SELECTED ## 
        teste = Cart.objects.get(id=request.user.id)
        teste.items.set([56,57])
        print(Cart.objects.filter(id=request.user.id))
        
        
        
        
        
        ## NEED TO CREATE CART OBJECT FIRST THEN ADD ORDER TO THE CART ##
        
        # if len(clean_order) > 0:
        #     try:
        #         # GET OBJECT WITH THE SETTINGS PASSED or CREATE ONE 
        #         Order.objects.filter(id=request.user.id).get_or_create(user=request.user,
        #                                                                     acomps_1=clean_order[0])
                
        #         # Order.objects.update(user=request.user.id, acomps_1=clean_order[0], acomps_2=clean_order[1],
        #                             # acomps_3=clean_order[2], acomps_4=clean_order[3])
        #     except IndexError:
        #         pass
            # try:
            #     Order.objects.update_or_create(user=request.user.id, acomps_1=clean_order[0], acomps_2=clean_order[1], acomps_3=clean_order[2])
            # except IndexError:
            #     pass
            # try:
            #     Order.objects.update_or_create(user=request.user, acomps_1=clean_order[0], acomps_2=clean_order[1])
            # except IndexError:
            #     pass  
            # try:
            #     Order.objects.update_or_create(user=request.user, acomps_1=clean_order[0],)
            # except IndexError:
            #     pass    
                
        
        
        
        return render (request, 'cart.html', context)    
            
            
    return render (request, "finish_order.html", context)

