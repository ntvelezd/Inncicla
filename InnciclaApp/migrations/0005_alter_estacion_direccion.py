# Generated by Django 3.2.13 on 2022-05-01 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InnciclaApp', '0004_estacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacion',
            name='direccion',
            field=models.CharField(max_length=200),
        ),
    ]
