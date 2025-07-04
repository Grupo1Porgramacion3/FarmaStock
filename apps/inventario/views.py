from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db import models
from .models import Medicamento, Categoria, Presentacion, MovimientoInventario
from .forms import MedicamentoForm

class MedicamentoListView(ListView):
    model = Medicamento
    template_name = 'inventario/medicamento_list.html'
    context_object_name = 'medicamentos'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Filtrar por búsqueda si existe
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda) | \
                      queryset.filter(codigo__icontains=busqueda)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_medicamentos'] = Medicamento.objects.count()
        context['medicamentos_bajo_stock'] = Medicamento.objects.filter(
            stock_actual__lte=models.F('stock_minimo')).count()
        return context

class MedicamentoDetailView(DetailView):
    model = Medicamento
    template_name = 'inventario/medicamento_detail.html'
    context_object_name = 'medicamento'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener los últimos 5 movimientos del medicamento
        context['movimientos'] = MovimientoInventario.objects.filter(
            medicamento=self.object).order_by('-fecha')[:5]
        return context

class MedicamentoCreateView(CreateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'inventario/medicamento_form.html'
    success_url = reverse_lazy('inventario:medicamento_list')
    
    def form_valid(self, form):
        # Guardar el stock inicial antes de crear el medicamento
        stock_inicial = form.instance.stock_actual
        
        response = super().form_valid(form)
        
        # Crear un movimiento de entrada inicial si hay stock, pero sin actualizar el stock nuevamente
        if stock_inicial > 0:
            # Crear el movimiento directamente en la base de datos sin activar el signal
            MovimientoInventario.objects.create(
                medicamento=form.instance,
                tipo='ENTRADA',
                cantidad=stock_inicial,
                usuario=self.request.user,
                nota='Stock inicial al crear el medicamento'
            )
            
            # Restaurar el stock original ya que el MovimientoInventario lo duplicó
            Medicamento.objects.filter(pk=form.instance.pk).update(stock_actual=stock_inicial)
            # Actualizar el objeto en memoria también
            form.instance.stock_actual = stock_inicial
            
        # Mostrar mensaje de éxito
        messages.success(self.request, f'Medicamento {form.instance.nombre} registrado correctamente')
        return response

class MedicamentoUpdateView(UpdateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'inventario/medicamento_form.html'
    success_url = reverse_lazy('inventario:medicamento_list')
    
    def form_valid(self, form):
        # Guardar el stock anterior para comparar
        stock_anterior = self.get_object().stock_actual
        stock_nuevo = form.instance.stock_actual
        
        response = super().form_valid(form)
        
        # Si cambió el stock, registrar un movimiento
        if stock_nuevo != stock_anterior:
            diferencia = stock_nuevo - stock_anterior
            tipo = 'ENTRADA' if diferencia > 0 else 'SALIDA'
            
            # Crear el movimiento
            MovimientoInventario.objects.create(
                medicamento=form.instance,
                tipo=tipo,
                cantidad=abs(diferencia),
                usuario=self.request.user,
                nota=f'Ajuste de stock al editar el medicamento'
            )
            
            # Restaurar el stock correcto ya que el MovimientoInventario lo modificó
            Medicamento.objects.filter(pk=form.instance.pk).update(stock_actual=stock_nuevo)
            # Actualizar el objeto en memoria también
            form.instance.stock_actual = stock_nuevo
        
        messages.success(self.request, f'Medicamento {form.instance.nombre} actualizado correctamente')
        return response

class MedicamentoDeleteView(DeleteView):
    model = Medicamento
    template_name = 'inventario/medicamento_confirm_delete.html'
    success_url = reverse_lazy('inventario:medicamento_list')
    context_object_name = 'medicamento'
    
    def delete(self, request, *args, **kwargs):
        medicamento = self.get_object()
        messages.success(request, f'Medicamento {medicamento.nombre} eliminado correctamente')
        return super().delete(request, *args, **kwargs)
