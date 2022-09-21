
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
            Cart.objects.create(user=request.user, acomps=form.cleaned_data, item=Quentinha.objects.get(id=id))
            return render (request, "cart.html", context)
        else:
            print(form.errors)
            
            
    return render (request, "product_detail.html", context)



class BebidasView(ListView):
    template_name = 'bebidas.html'
    queryset = Bebida.objects.all()
    print(queryset)



from collections import defaultdict
import json
@csrf_exempt
def product_create_view2(request, ): #id
    form = Book_form(request.POST or None)
    object = Acompanhamentos.objects.all()
    context = {
        'form': form,
        'object': object,
    }

    if request.method == "POST":
        # form = Book_form(request.POST)
        # print('asdwaswa')
        # if form.is_valid() and form.cleaned_data:
        #     print(form.cleaned_data.get('acompanhamentos'))
        #     Cart.objects.create(user=request.user, acomps=form.cleaned_data,
        #                         )# item=Quentinha.objects.get(id=id))
        #     return render (request, "cart.html", context)
        # else:
        #     print(form.errors)
        
        received_json = json.loads(request.body)
        clean_data = []
        if received_json:
            for j in received_json:
                if j['amount'] != 0:
                    clean_data.append(j)
        print(clean_data)
            
            
    return render (request, "finish_order.html", context)

