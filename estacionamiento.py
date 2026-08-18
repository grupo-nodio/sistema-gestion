'''
🅿️ Gestión de estacionamientos

Permite administrar uno o varios estacionamientos, incluyendo:

- Identificación del estacionamiento. (indice de la columna)
- Estado (1 libre, 2 ocupado/lleno, 3 fuera de servicio)
- Nombre y dirección. (string)
- Cantidad de espacios. (int)
- Precio por hora. (int en AR$)
- Horario de atención. (string de horario de apertura + horario de cerrrada en formato de 24 hs.)
- Ganancias generadas. (int en AR$)

### 📍 Gestión de espacios

Cada estacionamiento cuenta con espacios cuyo estado puede ser:

- 🟢 Libre
- 🔴 Ocupado
- 🟡 Reservado
- ⚫ Fuera de servicio

Esto permite conocer rápidamente la disponibilidad de cada estacionamiento.
'''

#estacionamientos = [[][None, "Parking del sol", "Estacione Recoleta"][]["Av. 123", "Calle 123"][100, 24][300, 2000]["12:30", "14:25"]["18:00", "20:00"]] (columna y fila 0 no incluida)

def elegir_estacionamiento(estacionamientos):
    print("Estacionamientos disponibles")
    seleccion = int(input("Seleccione un estacionamiento: "))

    while estacionamientos[2][seleccion] != 1:
        seleccion = int(input("El estacionamiento", estacionamientos[1][seleccion], "no se encuentra disponible, ingrese otro: "))