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

# 1. Mostrar información
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
        seleccion = validar_seleccion

    print("'" + str(estacionamientos[0][seleccion]) + "' seleccionado.")
    return seleccion

def validar_seleccion(seleccion, estacionamientos):
    '''se llama a la funcion para validar si el rango es correcto'''
    seleccion = seleccion

    while seleccion < 1 or seleccion >= len(estacionamientos[0]):
        print("La opción ingresada no es válida.")
        seleccion = int(input("Seleccione un estacionamiento: "))

    return seleccion

# Ver información uno por uno
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

# 2. Modificación
def elegir_modificar():
    '''permite al usuario elegir un valor a modificar y llama a una función para verificar si el input es válido'''
    print("Elige valor a modificar: ")
    print("1. Nombre")
    print("2. Estado")
    print("3. Dirección")
    print("4. Espacios")
    print("5. Precio")
    print("6. Horario")
    print("7. Ganancias")
    print("8. Cancelar")

    eleccion = int(input())

    eleccion = validar_modificar(eleccion)

    return eleccion

def validar_modificar(eleccion):
    while eleccion < 1 or eleccion > 8:
        eleccion = int(input("Error, opción inválida, vuelva a elegir una opción: "))

    return eleccion

def modificar(seleccion, estacionamientos):
    '''llama a una funcion para que el usuario elija que modificar para luego llamar a la funcion que modifique el valor solicitado'''
    eleccion = elegir_modificar()
    opciones = [edit_nombre, edit_estado, edit_direccion, edit_espacios, edit_precio, edit_horario, edit_ganancias]

    if eleccion == 8:
        print("Modificación cancelada.")
    else:
        opciones[eleccion - 1](seleccion, estacionamientos)

# 2.1 Nombre
def edit_nombre(seleccion, estacionamientos):
    print("Nombre actual: " + str(estacionamientos[0][seleccion]))
    cambio = input("Ingrese un nuevo nombre: ")

    estacionamientos[0][seleccion] = cambio

# 2.2 Estado
def edit_estado(seleccion, estacionamientos):
    print("Estado actual de '" + str(estacionamientos[0][seleccion]) + "': " + str(ver_estado(seleccion, estacionamientos)))
    print("\n1. Disponible \n2. Ocupado \n3. Fuera de servicio")
    cambio = int(input("Ingrese un nuevo estado: "))

    cambio = validar_cambio_estado(cambio)
    
    estacionamientos[1][seleccion] = cambio
    print("Modificación realizada. El nuevo estado es: " + str(ver_estado(seleccion, estacionamientos)))

def validar_cambio_estado(cambio):
    while cambio < 1 or cambio > 3:
        cambio = int(input("Opción no válida, ingrese un nuevo estado: "))

    return cambio

# 2.3 Dirección
def edit_direccion(seleccion, estacionamientos):
    print("Dirección actual de '" + str(estacionamientos[0][seleccion]) + "': " + str(estacionamientos[2][seleccion]))
    cambio = input("Ingrese una nueva dirección: ")

    estacionamientos[2][seleccion] = cambio
    print("Modificación realizada. La nueva dirección es: " + str(estacionamientos[2][seleccion]))

# 2.4 Espacios
def edit_espacios(seleccion, estacionamientos):
    print("Espacio actual de '" + str(estacionamientos[0][seleccion]) + "': " + str(estacionamientos[3][seleccion]))
    cambio = int(input("Ingrese una nueva capacidad de espacio: "))

    cambio = validar_positivos(cambio)
    
    estacionamientos[3][seleccion] = cambio
    print("Modificación realizada. La nueva capacidad es: " + str(estacionamientos[3][seleccion]))

def validar_positivos(cambio):
    while cambio <= 0:
        cambio = int(input("Error, debe ser un número mayor a 0. Ingrese nuevamente: "))

    return cambio

# 2.5 Precio
def edit_precio(seleccion, estacionamientos):
    print("Precio actual de '" + str(estacionamientos[0][seleccion]) + "': $" + str(estacionamientos[4][seleccion]))
    cambio = int(input("Ingrese una nuevo precio: "))

    cambio = validar_positivos(cambio)
    
    estacionamientos[4][seleccion] = cambio
    print("Modificación realizada. El nuevo precio es $" + str(estacionamientos[4][seleccion]))

# 2.6 Horario
def edit_horario(seleccion, estacionamientos):
    print("Horario actual de " + str(estacionamientos[0][seleccion]) + ": de " + str(estacionamientos[5][seleccion]) + " a " + str(estacionamientos[6][seleccion]) + "hs")

    hora1 = input("Ingrese nueva hora de apertura (sin minutos), o Enter para mantener: ")

    if hora1 != "":
        hora1 = int(hora1)
        hora1 = validar_hora(hora1)

        minuto1 = int(input("Ingrese nuevos minutos de apertura: "))
        minuto1 = validar_minuto(minuto1)

        estacionamientos[5][seleccion] = str(hora1) + ":" + str(minuto1)
    else:
        # Obtener la hora y minuto actuales
        hora1 = int(estacionamientos[5][seleccion].split(":")[0])
        minuto1 = int(estacionamientos[5][seleccion].split(":")[1])

    hora2 = input("Ingrese nueva hora de cierre (sin minutos), o Enter para mantener: ")

    if hora2 != "":
        hora2 = int(hora2)
        hora2 = validar_hora(hora2)

        minuto2 = int(input("Ingrese nuevos minutos de cierre: "))
        minuto2 = validar_minuto(minuto2)

        if hora2 * 60 + minuto2 <= hora1 * 60 + minuto1:
            print("Error: el horario de cierre debe ser posterior al de apertura.")
            edit_horario(seleccion, estacionamientos)
            return

        estacionamientos[6][seleccion] = str(hora2) + ":" + str(minuto2)

    print("Modificación realizada.")
    print("Nuevo horario: " + str(estacionamientos[5][seleccion]) + " - " + str(estacionamientos[6][seleccion]))

def validar_hora(hora):
    while hora < 0 or hora > 23:
        hora = int(input("Error, ingrese una hora válida: "))

    return hora

def validar_minuto(minuto):
    while minuto < 0 or minuto > 59:
        minuto = int(input("Error, ingrese un minuto válido: "))

    return minuto

# 2.7 Ganancias
def edit_ganancias(seleccion, estacionamientos):
    print("Precio actual de '" + str(estacionamientos[0][seleccion]) + "': $" + str(estacionamientos[7][seleccion]))
    cambio = int(input("Ingrese un numero positivo para sumar o negativo para restar: "))
    
    estacionamientos[7][seleccion] += cambio
    print("Modificación realizada. La nueva ganancia es $" + str(estacionamientos[7][seleccion]))

estacionamientos = [[None, "Parking del sol", "Estacione Recoleta"], [None, 1, 2], [None, "Av. 123", "Calle 123"], [None, 100, 24], [None, 300, 2000], [None, "12:30", "14:25"], [None, "18:00", "20:00"], [None, 10000, 23400]] #(columna 0 no incluida)

seleccion = elegir_estacionamiento(estacionamientos)

for i in range(1, len(estacionamientos[1])):
    print("'" + str(estacionamientos[0][i]) + "' se encuentra " + str(ver_estado(i, estacionamientos)) + ".")