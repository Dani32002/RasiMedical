# Generated by Django 3.2.6 on 2023-09-27 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispositivo',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='insumo',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='medicamento',
            name='cantidad',
        ),
    ]
