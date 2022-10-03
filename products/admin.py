from django.contrib import admin
from .models import Acompanhamentos, Bebida, Quentinha, Feijoada, Extra
from cart.models import Customer

# Register your models here.
admin.site.register(Quentinha)
admin.site.register(Feijoada)
admin.site.register(Bebida)
admin.site.register(Extra)
admin.site.register(Acompanhamentos)
admin.site.register(Customer)
