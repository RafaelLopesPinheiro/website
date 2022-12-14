# Generated by Django 4.1 on 2022-10-03 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0015_remove_order_acompanhamentos_cart_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('device', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
