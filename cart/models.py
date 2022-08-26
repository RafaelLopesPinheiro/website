from django.db import models
from products.models import Order
# Create your models here.
class Cart(models.Model):
    adrres = models.CharField(max_length=70)
    orders = models.ManyToManyField(Order)