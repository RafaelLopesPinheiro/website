from django.contrib import admin
from .models import Acompanhamentos, Bebida, Quentinha, Feijoada, Extra

# Register your models here.
admin.site.register(Quentinha)
admin.site.register(Feijoada)
admin.site.register(Bebida)
admin.site.register(Extra)
admin.site.register(Acompanhamentos)

