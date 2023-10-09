# Generated by Django 3.2.6 on 2023-10-03 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('fechaEmision', models.DateField(null=True)),
                ('fechaPago', models.DateField(null=True)),
                ('total', models.IntegerField()),
            ],
        ),
    ]