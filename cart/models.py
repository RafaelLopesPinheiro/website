from django.db import models
from products.models import Order
# Create your models here.
class Cart(models.Model):
    ## add user here 
    user = models.CharField(max_length=50)
    adrres = models.CharField(max_length=70)
    acomps = models.CharField(max_length=100, null=True)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.user