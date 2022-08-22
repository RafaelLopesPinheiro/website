from django.contrib import admin
from django.urls import path
from .views import BebidasView, QuentinhasListView, home_view, product_detail_view, FeijoadaView, QuentinhaDetailView


app_name='products'
urlpatterns = [
    path('feijoadas/', FeijoadaView.as_view(), name='feijoada-list'),
    path('quentinhas/', QuentinhasListView.as_view(), name='quentinha-list'),
    path('quentinhas/<int:id>', QuentinhaDetailView.as_view(), name='quentinha-detail'),   
    path('bebidas/', BebidasView.as_view(), name='bebidas'),
    path('products/',QuentinhasListView.as_view(), name='product-list'),
    path('products/<int:id>', product_detail_view, name='product-detail'),
]