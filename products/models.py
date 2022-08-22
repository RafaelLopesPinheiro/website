from django.db import models
from django.urls import reverse


# Create your models here.
class Acompanhamentos(models.Model):
    acomp_choices = models.CharField(max_length=50)

    def __str__(self):
        return self.acomp_choices


class Quentinha(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    price = models.FloatField()
    acompanhamentos = models.ManyToManyField(Acompanhamentos)


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



class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    price = models.FloatField(null=True, blank=True)
    acompa = models.ManyToManyField(Acompanhamentos)


    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField(max_length=75)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name




class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Quentinha, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=150, null=True, choices=STATUS)
