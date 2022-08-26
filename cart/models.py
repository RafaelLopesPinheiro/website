from django.db import models

# Create your models here.
class Cart(models.Model):
    adrres = models.CharField(max_length=70)