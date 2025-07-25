# Generated by Django 4.2.4 on 2025-07-03 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('dosis', models.CharField(max_length=100, verbose_name='Dosis')),
                ('descripcion', models.TextField(blank=True, verbose_name='Descripción')),
                ('codigo', models.CharField(max_length=50, unique=True, verbose_name='Código')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('stock_actual', models.IntegerField(default=0, verbose_name='Stock Actual')),
                ('stock_minimo', models.IntegerField(default=5, verbose_name='Stock Mínimo')),
                ('fecha_vencimiento', models.DateField(verbose_name='Fecha de Vencimiento')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.categoria', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Medicamento',
                'verbose_name_plural': 'Medicamentos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Presentación',
                'verbose_name_plural': 'Presentaciones',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='MovimientoInventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('ENTRADA', 'Entrada'), ('SALIDA', 'Salida')], max_length=10, verbose_name='Tipo de Movimiento')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('nota', models.TextField(blank=True, verbose_name='Nota')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.medicamento', verbose_name='Medicamento')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Movimiento de Inventario',
                'verbose_name_plural': 'Movimientos de Inventario',
                'ordering': ['-fecha'],
            },
        ),
        migrations.AddField(
            model_name='medicamento',
            name='presentacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.presentacion', verbose_name='Presentación'),
        ),
    ]
