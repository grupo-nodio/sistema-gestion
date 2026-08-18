# 🅿️ Park Direct

> Sistema de gestión de estacionamientos desarrollado en Python.

## 📌 Sobre el proyecto

**Park Direct** es un sistema de gestión desarrollado como proyecto académico para facilitar la administración interna de uno o varios estacionamientos.

El sistema permite centralizar en un único lugar la información relacionada con clientes, vehículos, estacionamientos, espacios, reservas, ingresos y egresos.

Su objetivo es reemplazar una gestión manual de la información por una solución organizada que permita consultar y administrar las operaciones del estacionamiento de manera rápida y sencilla.

---

## 🎯 Objetivos

El sistema busca facilitar la gestión diaria de un estacionamiento mediante:

- Administración de clientes y vehículos.
- Control de espacios disponibles y ocupados.
- Gestión de reservas.
- Registro de ingresos y egresos.
- Cálculo automático de cobros según el tiempo de permanencia.
- Consultas y búsquedas de información.
- Ordenamiento y filtrado de datos.
- Generación de reportes y estadísticas.
- Consulta del estado general de los estacionamientos.

---

## ⚙️ Funcionalidades

### 👤 Gestión de clientes

Permite registrar, consultar, modificar y eliminar clientes, almacenando información como:

- DNI
- Nombre y apellido
- Teléfono
- Email

### 🚗 Gestión de vehículos

Permite registrar vehículos y asociarlos con sus respectivos clientes.

Se administra información como:

- Patente
- Tipo de vehículo
- Cliente asociado

### 🅿️ Gestión de estacionamientos

Permite administrar uno o varios estacionamientos, incluyendo:

- Identificación del estacionamiento.
- Nombre y dirección.
- Cantidad de espacios.
- Precio por hora.
- Horario de atención.
- Ganancias generadas.

### 📍 Gestión de espacios

Cada estacionamiento cuenta con espacios cuyo estado puede ser:

- 🟢 Libre
- 🔴 Ocupado
- 🟡 Reservado
- ⚫ Fuera de servicio

Esto permite conocer rápidamente la disponibilidad de cada estacionamiento.

### 📅 Gestión de reservas

El sistema permite:

- Crear reservas.
- Consultar reservas.
- Modificar reservas.
- Cancelar reservas.
- Asociar una reserva con un cliente, vehículo y espacio.
- Controlar la disponibilidad antes de realizar una reserva.

### 🚘 Ingresos y egresos

Permite registrar la entrada y salida de vehículos, almacenando:

- Fecha.
- Hora de entrada.
- Hora de salida.
- Tiempo de permanencia.
- Importe abonado.

El sistema calcula el importe correspondiente según el tiempo que el vehículo permaneció estacionado.

### 📊 Reportes y estadísticas

Park Direct permite obtener información sobre el funcionamiento de los estacionamientos, incluyendo:

- Cantidad de vehículos ingresados.
- Ingresos generados.
- Ocupación de espacios.
- Espacios disponibles.
- Información sobre reservas.
- Estado general de los estacionamientos.

---

## 💡 Ejemplo de funcionamiento

Un cliente llega al estacionamiento y solicita un espacio.

1. Se busca al cliente en el sistema o se registra si es nuevo.
2. Se identifica su vehículo.
3. Se consulta la disponibilidad de espacios.
4. Se asigna un espacio libre.
5. Se registra la hora de entrada.
6. El espacio pasa a estado **ocupado**.
7. Al retirarse el vehículo, se registra la hora de salida.
8. El sistema calcula el tiempo de permanencia.
9. Se determina el importe a pagar.
10. Se registra el cobro y el espacio vuelve a quedar **libre**.

El mismo sistema permite realizar reservas y consultar información histórica y estadística.

---

## 🛠️ Tecnologías utilizadas

- 🐍 **Python**
- 🔀 **Git**
- 🐙 **GitHub**

El sistema funciona mediante una **interfaz de consola**, de acuerdo con los requisitos del proyecto académico.