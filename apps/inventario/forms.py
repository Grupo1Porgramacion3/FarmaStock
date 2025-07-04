from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Medicamento, Categoria, Presentacion

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'dosis', 'presentacion', 'categoria', 'descripcion', 
                  'codigo', 'precio', 'stock_actual', 'stock_minimo', 'fecha_vencimiento']
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-6 mb-0'),
                Column('dosis', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('presentacion', css_class='form-group col-md-6 mb-0'),
                Column('categoria', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'descripcion',
            Row(
                Column('codigo', css_class='form-group col-md-4 mb-0'),
                Column('precio', css_class='form-group col-md-4 mb-0'),
                Column('fecha_vencimiento', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('stock_actual', css_class='form-group col-md-6 mb-0'),
                Column('stock_minimo', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )
    
    def clean(self):
        cleaned_data = super().clean()
        # Validación personalizada: el stock actual no puede ser negativo
        stock_actual = cleaned_data.get('stock_actual')
        if stock_actual is not None and stock_actual < 0:
            self.add_error('stock_actual', 'El stock no puede ser negativo')
        
        # Validación personalizada: el precio debe ser mayor que cero
        precio = cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            self.add_error('precio', 'El precio debe ser mayor que cero')
        
        return cleaned_data
