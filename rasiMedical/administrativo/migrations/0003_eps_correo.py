# Generated by Django 3.2.6 on 2023-10-10 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0002_eps'),
    ]

    operations = [
        migrations.AddField(
            model_name='eps',
            name='correo',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
