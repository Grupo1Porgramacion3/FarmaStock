# FarmaStock - Sistema de Gestión de Medicamentos

FarmaStock es un sistema web diseñado para facilitar el control de medicamentos en farmacias, permitiendo gestionar inventario, datos de medicamentos y cantidades de forma intuitiva y funcional.

# Razon:

Este proyecto fue realizado por los siguientes estudiantes de la carrera de desarrollo de software del instituto tecnologico de las americas ITLA:

- Victor Lorenzo Hernandez
- Carlos Gonell
- Francesco Gallo Balma
- Waskar Enriquez Añil
- Ador Santiago
- Carlos Valerio Feliz

# Facilitador:

Facilitado por el maestro: Kelin Tejada Belliard, que gracias a sus contenidos pudimos aprender que programar no solo es tirar codigo, sino, planificacion y organizacion.

## Tecnologías Utilizadas

- Python 3.12
- Django 4.2.4
- SQLite 3
- HTML5, CSS3 y JavaScript
- Bootstrap 5
- Django Crispy Forms 2.0
- Crispy Bootstrap5 0.7



## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual: `python -m venv venv`
3. Activar el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Realizar migraciones: `python manage.py migrate`
6. Crear superusuario: `python manage.py createsuperuser`
7. Iniciar servidor: `python manage.py runserver`

## Funcionalidades Principales

- Gestión de medicamentos (CRUD)
- Control de inventario (entradas/salidas)
- Alertas de stock bajo
- Gestión de usuarios y permisos
- Dashboard con información relevante
