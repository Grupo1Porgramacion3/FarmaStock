from django.contrib import admin
from .models import Categoria, Presentacion, Medicamento, MovimientoInventario

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Presentacion)
class PresentacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dosis', 'presentacion', 'categoria', 'codigo', 'precio', 'stock_actual', 'fecha_vencimiento')
    list_filter = ('categoria', 'presentacion')
    search_fields = ('nombre', 'codigo')
    date_hierarchy = 'fecha_creacion'

@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = ('medicamento', 'tipo', 'cantidad', 'fecha', 'usuario')
    list_filter = ('tipo', 'fecha')
    search_fields = ('medicamento__nombre', 'nota')
    date_hierarchy = 'fecha'
