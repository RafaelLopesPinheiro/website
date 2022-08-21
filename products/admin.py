from django.contrib import admin
from .models import Bebida, Quentinha, Feijoada, Product

# Register your models here.
admin.site.register(Quentinha)
admin.site.register(Feijoada)
admin.site.register(Bebida)
admin.site.register(Product)