# Generated by Django 4.1 on 2022-09-15 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_rename_user_cart_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user_name',
            new_name='user',
        ),
    ]
