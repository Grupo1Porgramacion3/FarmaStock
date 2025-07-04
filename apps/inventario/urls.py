from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('medicamentos/', views.MedicamentoListView.as_view(), name='medicamento_list'),
    path('medicamentos/<int:pk>/', views.MedicamentoDetailView.as_view(), name='medicamento_detail'),
    path('medicamentos/nuevo/', views.MedicamentoCreateView.as_view(), name='medicamento_create'),
    path('medicamentos/<int:pk>/editar/', views.MedicamentoUpdateView.as_view(), name='medicamento_update'),
    path('medicamentos/<int:pk>/eliminar/', views.MedicamentoDeleteView.as_view(), name='medicamento_delete'),
]
