# Generated by Django 4.1 on 2022-09-25 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_delete_mymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quentinha',
            name='acompanhamentos',
        ),
    ]