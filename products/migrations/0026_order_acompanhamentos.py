# Generated by Django 4.1 on 2022-08-23 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_alter_quentinha_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='acompanhamentos',
            field=models.ManyToManyField(to='products.acompanhamentos'),
        ),
    ]
