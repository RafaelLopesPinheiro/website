from django.db import models
from products.models import Acompanhamentos, Quentinha

# Create your models here.
class Order(models.Model):
    ## add user here 
    user = models.CharField(max_length=50)
    item = models.CharField(max_length=100)
    acomps = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    observation = models.CharField(max_length=250, blank=True)

    acomps_1 = models.CharField(max_length=100)
    acomps_2 = models.CharField(max_length=100, blank=True)
    acomps_3 = models.CharField(max_length=100, blank=True)
    acomps_4 = models.CharField(max_length=100, blank=True)
    
    
    def __str__(self):
        return self.user
    
    

class Cart(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    # customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    cart = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Quentinha, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=150, null=True, choices=STATUS)
    
