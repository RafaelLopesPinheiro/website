from django.contrib import admin
from django.urls import path
from .views import (BebidasView, QuentinhasListView, product_detail_view, 
                    FeijoadaView, QuentinhaDetailView, product_create_view, home_view)


app_name='products'
urlpatterns = [
    path('', home_view, name='home'),
    path('feijoadas/', FeijoadaView.as_view(), name='feijoada-list'),
    path('quentinhas/', QuentinhasListView.as_view(), name='quentinha-list'),
    path('quentinhas/<int:id>', QuentinhaDetailView.as_view(), name='quentinha-detail'),   
    path('bebidas/', BebidasView.as_view(), name='bebidas'),
    path('finish/', product_create_view, name='create-order'),
]