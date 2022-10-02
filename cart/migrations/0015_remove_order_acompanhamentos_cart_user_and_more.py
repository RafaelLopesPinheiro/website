# Generated by Django 4.1 on 2022-09-30 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_remove_cart_cart_remove_order_acompanhamentos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(related_name='item_orders', to='cart.order'),
        ),
    ]
