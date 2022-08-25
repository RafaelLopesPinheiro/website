
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView, FormView, CreateView
from .models import Acompanhamentos, Quentinha, Product, Bebida, Feijoada
from .forms import QuentinhaForm, Acompanha_Form, Book_form
from django.utils.functional import LazyObject as _
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
    print(form_class)
    def get_object(self):
        id_ = self.kwargs.get("id") ## ID of Quentinha
        return get_object_or_404(Quentinha, id=id_)


    
    

class BookView(FormView):
    template_name = 'product_detail.html'
    form_class = Book_form
    success_url = '/'

    def form_valid(request, form):
        return super().form_valid(form)


    

def product_create_view(request, id):
    form = Book_form(request.POST or None)
    successs_url = 'home.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id") ## ID of Quentinha
        return get_object_or_404(Quentinha, id=id_)    
    
    
    
    object = Quentinha.objects.get(id=1)
    
    if request.POST:
        if form.is_valid():
            form.save()
        return render(request, successs_url)
    context = {
        'form': form,
        'object': object
    }
    
    return render (request, "product_detail.html", context)



class BebidasView(ListView):
    template_name = 'bebidas.html'
    queryset = Bebida.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Bebida, id=id)



