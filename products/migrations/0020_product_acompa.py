# Generated by Django 4.1 on 2022-08-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_order_customer_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='acompa',
            field=models.ManyToManyField(to='products.acompanhamentos'),
        ),
    ]