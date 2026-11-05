# 🅿️ Park Direct

Sistema de gestión de estacionamientos desarrollado en Python mediante una interfaz de consola.

## 📌 Sobre el proyecto

Park Direct es un sistema de gestión desarrollado como proyecto académico para facilitar la administración interna de uno o múltiples estacionamientos.
El sistema permite centralizar la información a través de una base de datos local basada en archivos **JSON**, organizando de forma eficiente clientes, vehículos, reservas, ocupación en tiempo real y cobros mediante el uso de diccionarios.
Su objetivo es reemplazar la gestión manual por una solución automatizada, estructurada en diferentes módulos interconectados, garantizando la integridad de los datos mediante validaciones lógicas y expresiones regulares (Regex).

## 🎯 Objetivos

El sistema busca facilitar la gestión diaria mediante:

* Administración centralizada de múltiples estacionamientos y sus horarios.
* Persistencia de datos en tiempo real en formato JSON para evitar la pérdida de información.
* Control de clientes (altas, bajas lógicas, modificaciones y reactivaciones).
* Gestión de vehículos vinculados directamente al DNI de los propietarios.
* Control dinámico de la capacidad de espacios disponibles y ocupados.
* Gestión de reservas manuales con validación de fechas, horarios y emisión de tickets.
* Cálculo automático de tarifas según el tipo de vehículo, horas de permanencia y aplicación de descuentos.
* Generación y exportación de reportes y estadísticas en archivos de texto (TXT).

## ⚙️ Funcionalidades Principales

### 🏢 Gestión de Estacionamientos
Permite administrar una red de estacionamientos, controlando:
* Identificación, nombre y dirección.
* Estados operativos (1. Disponible, 2. Ocupado, 3. Fuera de servicio).
* Control dinámico de espacios (la capacidad disponible se ajusta automáticamente con las reservas).
* Horarios de atención configurables por día de la semana (Normal, 24 horas o Cerrado).

### 👤 Gestión de Usuarios (Clientes)
Módulo basado en diccionarios anidados que permite:
* **Alta y Modificación:** Registro validado de Nombre, Apellido, DNI (8 dígitos exactos), Teléfono y Email.
* **Bajas lógicas y Reactivación:** Los usuarios no se eliminan permanentemente; cambian de estado Activo ('A') a Inactivo ('B'), permitiendo ser reactivados sin perder su historial.

### 🚗 Gestión de Vehículos
* Validación estricta de patentes mediante Regex (formatos de Argentina y Mercosur).
* Categorización por tipos permitidos: Motos, Autos y Camionetas.
* Asociación obligatoria de cada vehículo con el DNI de un usuario previamente registrado en el sistema.

### 📅 Gestión de Reservas
* Creación, modificación, consulta, cancelación y recuperación de reservas.
* Validación inteligente del calendario y franjas horarias (00 o 30 minutos).
* **Control de disponibilidad:** Al confirmar una reserva, se descuenta automáticamente un lugar de la capacidad actual; al cancelarse,
