from django.contrib import admin
from django.urls import path
from .views import (BebidasView, QuentinhasListView, 
                    FeijoadaView, QuentinhaDetailView, product_create_view, home_view, BookView, acomp_form)


app_name='products'
urlpatterns = [
    path('', home_view, name='home'),
    path('feijoadas/', FeijoadaView.as_view(), name='feijoada-list'),
    path('quentinhas/', QuentinhasListView.as_view(), name='quentinha-list'),
    path('quentinhas/<int:id>', product_create_view, name='quentinha-detail'),   
    path('bebidas/', BebidasView.as_view(), name='bebidas'),
    path('finish/<int:id>', product_create_view, name='create-order'),
    path('finish_order/', BookView.as_view(), name='book-item'),
    path('order_test/', acomp_form, name='save-item'),
]