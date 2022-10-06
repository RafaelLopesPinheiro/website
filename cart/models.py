from django.db import models
from products.models import Quentinha

# Create your models here.
class Order(models.Model):
    ## add user here 
    user = models.CharField(max_length=50, blank=True)
    qnty = models.IntegerField(default=1)
    item_ordered = models.ForeignKey(Quentinha, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    observation = models.CharField(max_length=250, blank=True)

    acomps_1 = models.CharField(max_length=100)
    acomps_2 = models.CharField(max_length=100, blank=True)
    acomps_3 = models.CharField(max_length=100, blank=True)
    acomps_4 = models.CharField(max_length=100, blank=True)
        
    def __str__(self):
        return self.user
    
    @property
    def get_sum(self):
        total = self.item_ordered.price * self.qnty
        return total
    


class Cart(models.Model):
    STATUS = (
        ('Not Confirmed', 'Not Confirmed'),
        ('Confirmed', 'Confirmed'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    # customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    user = models.CharField(max_length=150, null=True)
    items = models.ManyToManyField(Order)
    product = models.ForeignKey(Quentinha, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=150, null=True, choices=STATUS, default='Not Confirmed')
    
    @property
    def get_total_sum(self):
        total = 0
        for i in self.items.all():
            total += i.get_sum
        return total        
    

class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=250, null=True)
    device = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=25, null=True)
    