# Generated by Django 4.0.4 on 2022-05-31 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0006_alter_vehiculo_modelo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('vehiculo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='familia.vehiculo')),
                ('marca_celular', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
            ],
            bases=('familia.vehiculo',),
        ),
    ]
