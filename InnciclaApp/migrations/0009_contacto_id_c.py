# Generated by Django 3.2.12 on 2022-05-26 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InnciclaApp', '0008_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='id_c',
            field=models.CharField(default='1', max_length=30),
        ),
    ]