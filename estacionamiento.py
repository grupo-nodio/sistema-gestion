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
    '''Muestra la lista de los estacionamientos que se encuentran en la base de datos.'''
    print("Estacionamientos disponibles: ")

    for i in range(1, len(estacionamientos[0])):
        print("Opción " + str(i) + ": " + str(estacionamientos[0][i]))

def elegir_estacionamiento(estacionamientos):
    '''Permite seleccionar el estacionamiento, llamando a funciones de verificación y de muestra de opciones'''
    mostrar_estacionamientos(estacionamientos)

    seleccion = int(input("Seleccione un estacionamiento: "))

    seleccion = validar_seleccion(seleccion, estacionamientos)

    while estacionamientos[1][seleccion] != 1:
        seleccion = int(input("El estacionamiento '" + str(estacionamientos[0][seleccion]) + "' no se encuentra disponible, ingrese otro: "))

    print("'" + str(estacionamientos[0][seleccion]) + "' seleccionado.")
    return seleccion

def validar_seleccion(seleccion, estacionamientos):
    '''se llama a la funcion para validar si el rango es correcto'''
    nueva_seleccion = seleccion

    while nueva_seleccion < 1 or nueva_seleccion >= len(estacionamientos[0]):
        print("La opción ingresada no es válida.")
        nueva_seleccion = int(input("Seleccione un estacionamiento: "))

    return nueva_seleccion

def ver_nombre(seleccion, estacionamientos):
    nombre = estacionamientos[0][seleccion]

    return nombre

def ver_estado(seleccion, estacionamientos):
    estado = estacionamientos[1][seleccion]

    if estado == 1:
        estado = "disponible"
    elif estado == 2:
        estado = "ocupado"
    else:
        estado = "fuera de servicio"

    return estado

def ver_direccion(seleccion, estacionamientos):
    direccion = estacionamientos[2][seleccion]

    return direccion

def ver_espacios(seleccion, estacionamientos):
    espacios = estacionamientos[3][seleccion]

    return espacios

def ver_precio(seleccion, estacionamientos):
    precio = "$" + str(estacionamientos[4][seleccion])

    return precio

def ver_horario(seleccion, estacionamientos):
    horario = str(estacionamientos[5][seleccion]) + " - " + str(estacionamientos[6][seleccion])

    return horario

def ver_ganancias(seleccion, estacionamientos):
    ganancias = "$" + str(estacionamientos[7][seleccion])

    return ganancias

def mostrar_informacion(seleccion, estacionamientos):
    '''llama a todas las funciones que muestran la informacion del estacionamiento'''
    print("Nombre:", ver_nombre(seleccion, estacionamientos))
    print("Estado:", ver_estado(seleccion, estacionamientos))
    print("Dirección:", ver_direccion(seleccion, estacionamientos))
    print("Espacios:", ver_espacios(seleccion, estacionamientos))
    print("Precio:", ver_precio(seleccion, estacionamientos))
    print("Horario:", ver_horario(seleccion, estacionamientos))
    print("Ganancias:", ver_ganancias(seleccion, estacionamientos))

def elegir_modificar():
    print("Elige valor a modificar: ")
    print("1. Nombre")
    print("2. Estado")
    print("3. Dirección")
    print("4. Espacios")
    print("5. Precio")
    print("6. Horario")
    print("7. Ganancias")

    eleccion = int(input())

    return eleccion

def modificar(seleccion, estacionamientos):
    eleccion = elegir_modificar() #CONTINUAR

estacionamientos = [[None, "Parking del sol", "Estacione Recoleta"], [None, 1, 2], [None, "Av. 123", "Calle 123"], [None, 100, 24], [None, 300, 2000], [None, "12:30", "14:25"], [None, "18:00", "20:00"], [None, 10000, 23400]] #(columna 0 no incluida)

seleccion = elegir_estacionamiento(estacionamientos)

for i in range(1, len(estacionamientos[1])):
    print("'" + str(estacionamientos[0][i]) + "' se encuentra " + str(ver_estado(i, estacionamientos)) + ".")