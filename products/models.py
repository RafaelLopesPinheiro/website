from django.db import models
from django.urls import reverse
from django.shortcuts import render

# Create your models here.
class Acompanhamentos(models.Model):
    acomp_choices = models.CharField(max_length=50)

    def __str__(self):
        return self.acomp_choices


class Quentinha(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    price = models.FloatField(null=True)
    acompanhamentos = models.ManyToManyField(Acompanhamentos)
    thumb = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse("products:quentinha-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title


class Feijoada(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    price = models.FloatField()
    extras = models.BooleanField(default=False)
    thumb = models.ImageField(blank=True)

    def __str__(self):
        return self.title


class Bebida(models.Model):
    title = models.CharField(max_length=50)
    thumb = models.ImageField(blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products:bebidas-detail", kwargs={"id": self.id})
    
    

class Bebidas_choices(models.Model):
    sabor = models.CharField(max_length=50)
    
    def __str__(self):
        return self.sabor
    

class Extra(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    price = models.FloatField(null=True, blank=True)


    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title

