# Generated by Django 4.1 on 2022-08-22 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_remove_feijoada_testando_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanhamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='quentinha',
            name='acompanhamentos',
            field=models.BooleanField(default=True),
        ),
    ]
