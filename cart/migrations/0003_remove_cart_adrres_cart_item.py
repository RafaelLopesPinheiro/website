# Generated by Django 4.1 on 2022-09-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='adrres',
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
