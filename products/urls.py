from django.contrib import admin
from django.urls import path
from .views import (BebidasView, QuentinhasListView, 
                    FeijoadaView, QuentinhaDetailView, home_view,
                    BookView, product_create_view)


app_name='products'
urlpatterns = [
    path('', home_view, name='home'),
    path('feijoadas/', FeijoadaView.as_view(), name='feijoada-list'),
    path('quentinhas/', QuentinhasListView.as_view(), name='quentinha-list'),
    path('quentinhas/<int:id>', product_create_view, name='quentinha-detail'),   
    path('bebidas/', BebidasView.as_view(), name='bebidas'),
]