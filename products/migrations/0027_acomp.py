# Generated by Django 4.1 on 2022-08-27 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_order_acompanhamentos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acomp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acomps', models.CharField(choices=[('ARROZ_BRANCO', 'Arroz Branco'), ('MACARRAO', 'Macarrão'), ('FEIJAO_PRETO', 'Feijão Preto')], default='', max_length=100)),
            ],
        ),
    ]
