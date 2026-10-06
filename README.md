---

# 🅿️ Park Direct

Sistema de gestión de estacionamientos desarrollado en Python mediante una interfaz de consola.

## 📌 Sobre el proyecto

Park Direct es un sistema de gestión desarrollado como proyecto académico para facilitar la administración interna de uno o múltiples estacionamientos.
El sistema permite centralizar la información a través de una base de datos en memoria (utilizando matrices y listas paralelas), organizando clientes, vehículos, reservas, ocupación en tiempo real y cobros.
Su objetivo es reemplazar la gestión manual por una solución automatizada, estructurada en diferentes módulos interconectados, garantizando la integridad de los datos mediante validaciones lógicas y expresiones regulares (Regex).

## 🎯 Objetivos

El sistema busca facilitar la gestión diaria mediante:

* Administración centralizada de múltiples estacionamientos y sus horarios.


* Control de clientes (altas, bajas lógicas y modificaciones).


* Gestión de vehículos vinculados directamente al DNI de los propietarios.


* Control dinámico de la capacidad de espacios disponibles y ocupados.


* Gestión de reservas manuales con validación de fechas y horarios.


* Cálculo automático de tarifas según el tipo de vehículo y las horas de permanencia.


* Generación de reportes y estadísticas utilizando paradigmas de programación funcional.



## ⚙️ Funcionalidades Principales

### 🏢 Gestión de Estacionamientos

Permite administrar una red de estacionamientos, controlando:

* Identificación, nombre y dirección.


* Estados operativos (1. Disponible, 2. Ocupado, 3. Fuera de servicio).


* Control de espacios (capacidad total y actualización de capacidad actual disponible).


* Horarios de atención configurables por día de la semana (Normal, 24 horas o Cerrado).



### 👤 Gestión de Usuarios (Clientes)

Módulo basado en listas paralelas que permite:

* **Alta y Modificación:** Registro validado de Nombre, Apellido, DNI (8 dígitos exactos), Teléfono y Email.


* **Bajas lógicas y Reactivación:** Los usuarios no se eliminan permanentemente; cambian de estado Activo ('A') a Inactivo ('B'), permitiendo ser reactivados sin perder su historial.



### 🚗 Gestión de Vehículos

* Validación estricta de patentes (formatos de Argentina y Mercosur).


* Categorización por tipos permitidos: Motos, Autos y Camionetas.


* Asociación obligatoria de cada vehículo con el DNI de un usuario previamente registrado en el sistema.



### 📅 Gestión de Reservas

* Creación, modificación, consulta y cancelación de reservas.


* Validación inteligente del calendario (años, meses, días bisiestos) y franjas horarias.


* **Control de disponibilidad:** Al confirmar una reserva, se descuenta automáticamente un lugar de la capacidad actual del estacionamiento seleccionado, y al cancelarse, el lugar vuelve a liberarse.



### 💲 Tarifas y Cobros

El sistema calcula el importe correspondiente identificando de forma automática el tipo de vehículo mediante su patente:

* Motos: $2.500 / hora.


* Autos: $4.000 / hora.


* Camionetas: $6.000 / hora.



### 📊 Reportes y Estadísticas

Mediante el uso de funciones de orden superior (`map`, `filter`, `reduce` y funciones `lambda`), el sistema emite reportes en tiempo real sobre:

* Cantidad de estacionamientos registrados y su disponibilidad operativa.


* Logística de espacios ocupados diferenciando vehículos estándar (autos/motos) y grandes (camionetas).


* Capacidad actual unificada de toda la red.



## 💡 Flujo de Trabajo (Panel Administrador)

1. El administrador inicia el sistema y selecciona un estacionamiento de la red para trabajar sobre él.


2. Registra un nuevo usuario (Cliente) validando su DNI y correo.


3. Ingresa el vehículo del cliente, el cual queda atado a su DNI.


4. Genera una reserva de espacio. El sistema verifica que haya capacidad disponible antes de confirmar y descuenta el cupo.


5. Al finalizar la estadía, el administrador ingresa la duración en el módulo de tarifas, ingresa la patente, y el sistema calcula el cobro automáticamente.



## 🛠️ Tecnologías utilizadas

* **Python 3:** Lenguaje principal.
* *Módulo `re`:* Implementación de Expresiones Regulares para validación de datos (emails, patentes, teléfonos, nombres).


* *Programación Funcional:* Uso de `map`, `filter` y `reduce` en visualización y estadísticas.




* **Git y GitHub:** Control de versiones.
