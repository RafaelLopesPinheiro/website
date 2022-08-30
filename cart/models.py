from django.db import models
from products.models import Acompanhamentos, Quentinha

# Create your models here.
class Cart(models.Model):
    ## add user here 
    user = models.CharField(max_length=50)
    adrres = models.CharField(max_length=70)
    acomps = models.CharField(max_length=100, null=True)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.user
    
    

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    # customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Quentinha, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=150, null=True, choices=STATUS)
    acompanhamentos = models.ManyToManyField(Acompanhamentos)
