# Generated by Django 3.2.13 on 2022-05-01 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InnciclaApp', '0005_alter_estacion_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacion',
            name='image',
            field=models.CharField(default="{% static 'css/images/floresta.png' %}", max_length=200),
        ),
    ]
