from django.db import models
from products.models import Quentinha, Bebida
# Create your models here.
class Order(models.Model):
    ## add user here 
    order_id = models.CharField(max_length=25, null=True)
    user = models.CharField(max_length=50, blank=True)
    qnty = models.IntegerField(default=1)
    item_ordered = models.ForeignKey(Quentinha, null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    observation = models.CharField(max_length=250, blank=True)

    acomps_1 = models.CharField(max_length=100)
    acomps_2 = models.CharField(max_length=100, blank=True)
    acomps_3 = models.CharField(max_length=100, blank=True)
    acomps_4 = models.CharField(max_length=100, blank=True)
        
    def __str__(self):
        return self.order_id or self.user
    
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

    user = models.CharField(max_length=150, null=True)
    items = models.ManyToManyField(Order)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=150, null=True, choices=STATUS, default='Not Confirmed')
    bebida_choices = models.ManyToManyField(Bebida, blank=True)
    
     
    
    @property
    def get_total_sum(self):
        total = 0
        for i in self.items.all():
            total += i.get_sum      

        for i in self.bebida_choices.all():
            total += i.get_sum
            
        return total

    
    def __str__(self):
        return self.user
    
    
    


PAYMENT_CHOICES = [
    ('D','Dinheiro'),
    ('CD', 'Cartão de Debito'),
    ('CC', 'Cartão de Crédito')
]


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    device = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15)
    payment = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    cart_activity = models.ManyToManyField(Cart)
    
    
    def __str__(self):
        return self.name or self.phone
