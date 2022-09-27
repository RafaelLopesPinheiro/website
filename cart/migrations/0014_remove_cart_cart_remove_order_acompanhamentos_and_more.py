# Generated by Django 4.1 on 2022-09-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_remove_order_acompanhamentos_order_qnty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='cart.order'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('Not Confirmed', 'Not Confirmed'), ('Confirmed', 'Confirmed'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], default='Not Confirmed', max_length=150, null=True),
        ),
    ]