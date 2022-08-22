from django.db import models
from django.urls import reverse
# Create your models here.
class Quentinha(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    price = models.FloatField()
    
    acompanhamentos = models.BooleanField(default=False)
 
    def get_absolute_url(self):
        return reverse("products:quentinha-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title


class Feijoada(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    price = models.FloatField()
    extras = models.BooleanField(default=False)
    # testando = models.CharField(max_length=15, choices=CHOICES_RANDOM)

    def __str__(self):
        return self.title


class Bebida(models.Model):
    title = models.CharField(max_length=50)
    thumb = models.ImageField()
    price = models.FloatField()

    def __str__(self):
        return self.title


class Acompanhamentos(models.Model):
    CHOICES_ACOMP = [
        ('ARROZ_BRANCO','Arroz'),
        ('MACARRAO','macarrao'),
        ('FEIJAO_PRETO', 'feijao'),
    ]
    acomp_choices = models.BooleanField(choices=CHOICES_ACOMP)



class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title

