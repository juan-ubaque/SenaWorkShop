# Generated by Django 4.1.7 on 2023-03-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProductos', '0002_carro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='estado',
            field=models.CharField(choices=[('activo', 'activo'), ('comprado', 'comprado'), ('anulado', 'anulado')], default='activo', max_length=20),
        ),
    ]
