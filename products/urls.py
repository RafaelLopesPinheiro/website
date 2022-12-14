from django.contrib import admin
from django.urls import path
from .views import (BebidasView, QuentinhasListView, 
                    FeijoadaView, bebidas_detail_view, home_view,
                    product_create_view)


app_name='products'
urlpatterns = [
    path('', home_view, name='home'),
    path('feijoadas/', FeijoadaView.as_view(), name='feijoada-list'),
    path('quentinhas/', QuentinhasListView.as_view(), name='quentinha-list'),
    path('quentinhas/<int:id>', product_create_view, name='quentinha-detail'),   
    path('bebidas/', BebidasView.as_view(), name='bebidas'),
    path('bebidas/<int:id>', bebidas_detail_view, name='bebidas-detail')
]