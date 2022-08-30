from django.contrib import admin
from .models import Acomp, Acompanhamentos, Bebida, Customer, Quentinha, Feijoada, Product, Order

# Register your models here.
admin.site.register(Quentinha)
admin.site.register(Feijoada)
admin.site.register(Bebida)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Acompanhamentos)
admin.site.register(Customer)
admin.site.register(Acomp)