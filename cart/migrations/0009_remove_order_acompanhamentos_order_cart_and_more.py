# Generated by Django 4.1 on 2022-09-25 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_cart_acomps_1_cart_acomps_2_cart_acomps_3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cart.cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='acomps',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
