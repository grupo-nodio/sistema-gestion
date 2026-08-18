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
def mostrar_estacionamientos(estacionamientos):
    print("Estacionamientos disponibles: ")

    for i in range(1, len(estacionamientos[0])):
        print("Opción " + str(i) + ": " + str(estacionamientos[0][i]))

def elegir_estacionamiento(estacionamientos):
    mostrar_estacionamientos(estacionamientos)

    seleccion = int(input("Seleccione un estacionamiento: "))

    while estacionamientos[1][seleccion] != 1:
        seleccion = int(input("El estacionamiento '" + str(estacionamientos[0][seleccion]) + "' no se encuentra disponible, ingrese otro: "))

    print("'" + str(estacionamientos[0][seleccion]) + "' seleccionado.")
    return seleccion

def ver_estado(seleccion, estacionamientos):
    estado = estacionamientos[1][seleccion]

    if estado == 1:
        print(str(estacionamientos[0][seleccion]) + " se encuentra disponible.")
    elif estado == 2:
        print(str(estacionamientos[0][seleccion]) + " se encuentra ocupado.")
    else:
        print(str(estacionamientos[0][seleccion]) + " se encuentra fuera de servicio.")

estacionamientos = [[None, "Parking del sol", "Estacione Recoleta"], [None, 1, 2], [None, "Av. 123", "Calle 123"], [None, 100, 24], [None, 300, 2000], [None, "12:30", "14:25"], [None, "18:00", "20:00"], [None, 10000, 23400]] #(columna 0 no incluida)

seleccion = elegir_estacionamiento(estacionamientos)

for i in range(1, len(estacionamientos[1])):
    ver_estado(i, estacionamientos)