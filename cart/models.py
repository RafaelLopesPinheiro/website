from pyexpat import model
from django.db import models
from products.models import Quentinha

# Create your models here.
class Order(models.Model):
    ## add user here 
    user = models.CharField(max_length=50, blank=True)
    qnty = models.IntegerField(default=1)
    item = models.CharField(max_length=100)
    # acomps = models.CharField(max_length=200, blank=True)
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
        ('Not Confirmed', 'Not Confirmed'),
        ('Confirmed', 'Confirmed'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    # customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    user = models.CharField(max_length=150, null=True)
    items = models.ManyToManyField(Order, related_name='item_orders')
    product = models.ForeignKey(Quentinha, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=150, null=True, choices=STATUS, default='Not Confirmed')
    

class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=250, null=True)
    device = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=25, null=True)
    