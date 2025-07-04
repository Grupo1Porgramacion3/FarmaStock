from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

class Presentacion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Presentación'
        verbose_name_plural = 'Presentaciones'
        ordering = ['nombre']

class Medicamento(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    dosis = models.CharField(max_length=100, verbose_name='Dosis')
    presentacion = models.ForeignKey(Presentacion, on_delete=models.PROTECT, verbose_name='Presentación')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Categoría')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    codigo = models.CharField(max_length=50, unique=True, verbose_name='Código')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    stock_actual = models.IntegerField(default=0, verbose_name='Stock Actual')
    stock_minimo = models.IntegerField(default=5, verbose_name='Stock Mínimo')
    fecha_vencimiento = models.DateField(verbose_name='Fecha de Vencimiento')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    
    def __str__(self):
        return f"{self.nombre} - {self.dosis}"
    
    def necesita_reposicion(self):
        return self.stock_actual <= self.stock_minimo
    
    def esta_por_vencer(self):
        # Considera que está por vencer si faltan menos de 90 días
        dias_para_vencer = (self.fecha_vencimiento - timezone.now().date()).days
        return dias_para_vencer <= 90
    
    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        ordering = ['nombre']

class MovimientoInventario(models.Model):
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
    ]
    
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, verbose_name='Medicamento')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, verbose_name='Tipo de Movimiento')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Usuario')
    nota = models.TextField(blank=True, verbose_name='Nota')
    
    def __str__(self):
        return f"{self.get_tipo_display()} de {self.medicamento.nombre} - {self.cantidad} unidades"
    
    def save(self, *args, **kwargs):
        # Actualizar el stock del medicamento
        if self.tipo == 'ENTRADA':
            self.medicamento.stock_actual += self.cantidad
        else:  # SALIDA
            self.medicamento.stock_actual -= self.cantidad
        
        self.medicamento.save()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Movimiento de Inventario'
        verbose_name_plural = 'Movimientos de Inventario'
        ordering = ['-fecha']
