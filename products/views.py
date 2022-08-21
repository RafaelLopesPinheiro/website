
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView
from .models import Quentinha, Product, Bebida
from .forms import Quentinha_form, RawProductForm
from django.utils.functional import LazyObject as _
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request,"home.html", {})


class FeijoadaView(ListView):
    template_name = "feijoada_list.html"
    queryset = Product.objects.all()


class QuentinhasListView(ListView):
    template_name = 'product_list.html'
    queryset = Product.objects.all()
    

class QuentinhaDetailView(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)



def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj ,
        "acompanhamentos":['arroz branco', 'feijao preto','macarrao', 'maionese' ],
    }
    return render(request, "product_detail.html", context)


class BebidasView(ListView):
    template_name = 'bebidas.html'
    queryset = Bebida.objects.all()



