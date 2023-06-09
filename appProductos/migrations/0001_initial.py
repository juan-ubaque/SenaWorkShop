# Generated by Django 4.1.7 on 2023-03-11 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripCategoria', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias de  Productos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('decripcion', models.CharField(max_length=300)),
                ('precioUnitario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('unidad', models.CharField(max_length=10)),
                ('existencia', models.IntegerField()),
                ('imgGrande', models.ImageField(upload_to='productos')),
                ('imgPeque', models.ImageField(upload_to='iconos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProductos.categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
