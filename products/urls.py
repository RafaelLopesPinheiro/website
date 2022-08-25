from django.contrib import admin
from django.urls import path
from .views import (BebidasView, QuentinhasListView, 
                    FeijoadaView, QuentinhaDetailView, product_create_view, home_view, BookView)


app_name='products'
urlpatterns = [
    path('', home_view, name='home'),
    path('feijoadas/', FeijoadaView.as_view(), name='feijoada-list'),
    path('quentinhas/', QuentinhasListView.as_view(), name='quentinha-list'),
    path('quentinhas/<int:id>', QuentinhaDetailView.as_view(), name='quentinha-detail'),   
    path('bebidas/', BebidasView.as_view(), name='bebidas'),
    path('finish/<int:id>', product_create_view, name='create-order'),
    path('book_item/', BookView.as_view(), name='book-item'),
    path('finished/', BookView.as_view(), name='finished'),
]