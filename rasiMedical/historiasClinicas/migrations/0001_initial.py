# Generated by Django 3.2.6 on 2023-11-12 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0003_administrador'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntradaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.CharField(max_length=200)),
                ('tratamiento', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor', to='usuario.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.paciente')),
                ('permitidosEnfermera', models.ManyToManyField(to='usuario.Enfermera')),
                ('permitidosFarmaceutico', models.ManyToManyField(to='usuario.Farmaceutico')),
                ('permitidosMedico', models.ManyToManyField(to='usuario.Medico')),
            ],
        ),
    ]
