# Generated by Django 4.1 on 2022-09-26 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_remove_cart_acomps_remove_cart_acomps_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='idn',
        ),
    ]
