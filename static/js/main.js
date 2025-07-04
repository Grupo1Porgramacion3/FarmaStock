// Funciones JavaScript para FarmaStock

// Función para inicializar tooltips de Bootstrap
document.addEventListener('DOMContentLoaded', function() {
    // Inicializar tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Inicializar popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-cerrar alertas después de 5 segundos
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);
});

// Función para confirmar eliminación
function confirmDelete(event, itemName) {
    if (!confirm(`¿Está seguro que desea eliminar "${itemName}"?`)) {
        event.preventDefault();
        return false;
    }
    return true;
}

// Función para validar formulario de medicamentos
function validateMedicineForm() {
    var nombre = document.getElementById('id_nombre').value;
    var stock = document.getElementById('id_stock_actual').value;
    var precio = document.getElementById('id_precio').value;
    var fechaVencimiento = document.getElementById('id_fecha_vencimiento').value;
    
    if (!nombre) {
        alert('El nombre del medicamento es obligatorio');
        return false;
    }
    
    if (stock < 0) {
        alert('El stock no puede ser negativo');
        return false;
    }
    
    if (precio <= 0) {
        alert('El precio debe ser mayor que cero');
        return false;
    }
    
    if (!fechaVencimiento) {
        alert('La fecha de vencimiento es obligatoria');
        return false;
    }
    
    return true;
}
