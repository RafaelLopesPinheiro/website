# Generated by Django 4.1 on 2022-08-23 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_remove_quentinha_acompanhamentos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quentinha',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
