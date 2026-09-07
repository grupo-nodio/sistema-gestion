import re

# ------------------------------------------------------------- 1. VALIDACIONES -----------------------------------------------------------

# Se usa en validar_seleccion, validar_modificar, validar_cambio_estado, validar_positivos, validar_tipo_horario, validar_dia, elegir_estacionamiento, elegir_modificar, edit_estado, edit_espacios, edit_horario, crear_estado, crear_espacios, crear_horarios, eliminar_estacionamiento
def pedir_numero(mensaje):
    '''Solicita un valor al usuario y verifica con Regex que solo contenga números.'''
    valor = input(mensaje)
    
    while not re.match(r"^\d+$", valor):
        valor = input("Error, debe ingresar únicamente números. " + mensaje)
        
    # Como ya validamos que son números, podemos convertirlo a int() de forma segura
    return int(valor)

# Se usa en elegir_estacionamiento
def validar_seleccion(seleccion, estacionamientos):
    '''se llama a la funcion para validar si el rango es correcto'''
    seleccion = seleccion

    while seleccion < 1 or seleccion >= len(estacionamientos[0]):
        print("La opción ingresada no es válida.")
        seleccion = pedir_numero("Seleccione un estacionamiento: ")

    return seleccion

# Se usa en elegir_modificar
def validar_modificar(eleccion):
    '''se llama a la funcion para validar si la eleccion es alguna de las permitidas'''
    while eleccion < 1 or eleccion > 6:
        eleccion = pedir_numero("Error, opción inválida, vuelva a elegir una opción: ")

    return eleccion

# Se usa en edit_estado, crear_estado
def validar_cambio_estado(cambio):
    '''se valida si el estado elegido es correcto(1-3)'''
    while cambio < 1 or cambio > 3:
        cambio = pedir_numero("Opción no válida, ingrese un nuevo estado: ")

    return cambio

# Se usa en edit_espacios, crear_espacios
def validar_positivos(cambio):
    '''identifica si el numero es mayor a 0 y pide volverlo a ingresar si no lo es'''
    while cambio <= 0:
        cambio = pedir_numero("Error, debe ser un número mayor a 0. Ingrese nuevamente: ")

    return cambio

# Se usa en edit_horario, crear_horarios
def validar_tipo_horario(tipo):
    '''se valida si el tipo de horario elegido es correcto(1-3)'''
    while tipo < 1 or tipo > 3:
        tipo = pedir_numero("Error, ingrese una opción válida: ")

    return tipo

# Se usa en edit_horario
def validar_dia(dia):
    '''se valida si es un dia de la semana valido(1-7)'''
    while dia < 1 or dia > 7:
        dia = pedir_numero("Error, ingrese un día válido: ")

    return dia

# Se usa en tipo_horario_1 (las siguientes 3)
def validar_formato_hora(horario_str):
    '''Verifica que la cadena cumpla exactamente con el formato HH:MM (ej. 08:30) [8].'''
    # Clase 4: ^ (inicio), \d{2} (dos dígitos), : (dos puntos), \d{2} (dos dígitos), $ (fin) [8, 11]
    patron = r"^\d{2}:\d{2}$"
    return re.match(patron, horario_str)

def validar_horario(horario_str):
    '''Valida lógicamente las horas (00-23) y minutos (00-59) extrayéndolos con rebanado [9].'''
    # Clase 3: Usamos rebanado para extraer horas y minutos [9, 10]
    hora = int(horario_str[0:2])
    minuto = int(horario_str[3:5])
    return 0 <= hora <= 23 and 0 <= minuto <= 59
 
def validar_cierre(apertura, cierre):
    '''Valida con rebanado que la hora de cierre sea lógicamente posterior a la de apertura [9].'''
    hora_ap = int(apertura[0:2])
    min_ap = int(apertura[3:5])
    
    hora_ci = int(cierre[0:2])
    min_ci = int(cierre[3:5])
    
    # Convertimos a minutos totales para comparar lógicamente de manera sencilla
    total_min_apertura = hora_ap * 60 + min_ap
    total_min_cierre = hora_ci * 60 + min_ci
    
    return total_min_cierre > total_min_apertura

# Se usa en crear_nombre 
def validar_nombre(nombre):
    '''Valida que el nombre use caracteres permitidos y no sea exclusivamente numérico.'''
    patron = r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s]+$"
    
    # Validamos: que coincida con el patrón Y que el string no esté compuesto solo por números
    while not (re.match(patron, nombre) and not nombre.isdigit()):
        nombre = input("Error, el nombre debe contener al menos una letra y no tener símbolos. Ingrese nuevamente: ")

    return nombre

# Se usa en crear_direccion
def validar_direccion(direccion):
    '''valida que la direccion ingresada contenga al menos numero y/o letra'''
    while not re.match(r"^[\w\s]+$", direccion):
        direccion = input("Error, dirección inválida o vacía. Ingrese nuevamente: ")

    return direccion



# ------------------------------------------------------------- 2. CREACIÓN -------------------------------------------------------------

def crear_estacionamiento(estacionamientos, horarios):
    '''llama a todas las funciones necesarias para la creacion del estacionamiento'''
    print("Crear nuevo estacionamiento:")
    estacionamientos[0].append(crear_nombre())
    estacionamientos[1].append(crear_estado())
    estacionamientos[2].append(crear_direccion())
    estacionamientos[3].append(crear_espacios())
    estacionamientos[4].append(estacionamientos[3][-1])

    horarios.append(crear_horarios())

def crear_nombre():
    nombre = input("Ingrese nombre: ")

    nombre = validar_nombre(nombre)

    return nombre

def crear_estado():
    estado = pedir_numero("Ingrese el estado actual (1. Disponible, 2. Ocupado, 3. Fuera de servicio): ")
    estado = validar_cambio_estado(estado)
    return estado

def crear_direccion():
    direccion = input("Ingrese la dirección: ")

    direccion = validar_direccion(direccion)

    return direccion

def crear_espacios():
    espacios = pedir_numero("Ingrese la capacidad actual: ")
    espacios = validar_positivos(espacios)
    return espacios

def crear_horarios():
    '''crea los horarios haciendo elegir entre horario, 24 horas o cerrado por día de la semana'''
    horarios = []

    dias = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    ]

    print("1. Horario normal")
    print("2. 24 horas")
    print("3. Cerrado")
    print()

    for dia in dias:
        tipo = pedir_numero("Seleccione el tipo de horario para " + dia + ": ")
        tipo = validar_tipo_horario(tipo)

        if tipo == 1:
            horarios.append(tipo_horario_1())

        elif tipo == 2:
            horarios.append(True)

        else:
            horarios.append(False)

    return horarios



# ----------------------------------------------------- 3. VISUALIZACIÓN Y CONSULTAS -----------------------------------------------------

def mostrar_informacion(seleccion, estacionamientos, horarios):
    '''llama a todas las funciones que muestran la informacion del estacionamiento'''
    ver_nombre = lambda seleccion, estacionamientos: estacionamientos[0][seleccion]
    ver_direccion = lambda seleccion, estacionamientos: estacionamientos[2][seleccion]
    ver_espacios = lambda seleccion, estacionamientos: estacionamientos[3][seleccion]

    print("Nombre:", ver_nombre(seleccion, estacionamientos))
    print("Estado:", ver_estado(seleccion, estacionamientos))
    print("Dirección:", ver_direccion(seleccion, estacionamientos))
    print("Espacios:", ver_espacios(seleccion, estacionamientos))

    print("Horarios:")
    ver_horario(seleccion, horarios)

def mostrar_estacionamientos(estacionamientos):
    '''Muestra la lista de los estacionamientos usando map().'''
    print("Estacionamientos en la base de datos: ")

    # Medimos el largo de la lista nombres para obtener la cantidad real de estacionamientos
    indices = range(1, len(estacionamientos[0])) 
    
    # [0][i] para el nombre y [2][i] para la dirección
    list(map(lambda i: print(f"Estacionamiento {i}: '{estacionamientos[0][i]}' - Dirección: {estacionamientos[2][i]}"), indices))

def ver_estacionamientos_disponibles(estacionamientos):
    '''Filtra y muestra únicamente los estacionamientos con estado 1 usando filter() y map().'''
    indices = range(1, len(estacionamientos[0])) # Usamos el largo de la fila 0

    disponibles = list(filter(lambda i: estacionamientos[1][i] == 1, indices))

    print("\nEstacionamientos Libres/Disponibles:")
    if len(disponibles) == 0:
        print("No hay estacionamientos disponibles en este momento.")
    else:
        # [0][i] para el nombre y [2][i] para la dirección
        list(map(lambda i: print(f"- '{estacionamientos[0][i]}' en {estacionamientos[2][i]}"), disponibles))

def elegir_estacionamiento(estacionamientos):
    '''Permite seleccionar cualquier estacionamiento existente para administrarlo, sin restringir por su estado actual.'''
    mostrar_estacionamientos(estacionamientos)

    # Usamos pedir_numero para evitar errores si ingresan letras
    seleccion = pedir_numero("Seleccione un estacionamiento: ")

    # Solo validamos que el número esté dentro del rango de estacionamientos creados
    seleccion = validar_seleccion(seleccion, estacionamientos)

    print("'" + str(estacionamientos[0][seleccion]) + "' seleccionado.")
    return seleccion

def ver_estado(seleccion, estacionamientos):
    '''Devuelve en forma de string el estado del estacionamiento.'''
    estado = estacionamientos[1][seleccion]

    posibilidades = ["disponible", "ocupado", "fuera de servicio"]

    estado = posibilidades[estado - 1]

    return estado

def ver_horario(seleccion, horarios):
    '''muestra el horario de cada día de la semana'''
    print("Lunes:", mostrar_horario(horarios[seleccion][0]))
    print("Martes:", mostrar_horario(horarios[seleccion][1]))
    print("Miércoles:", mostrar_horario(horarios[seleccion][2]))
    print("Jueves:", mostrar_horario(horarios[seleccion][3]))
    print("Viernes:", mostrar_horario(horarios[seleccion][4]))
    print("Sábado:", mostrar_horario(horarios[seleccion][5]))
    print("Domingo:", mostrar_horario(horarios[seleccion][6]))

def mostrar_horario(horario):
    '''Devuelve en forma de string el horario del estacionamiento'''
    if horario is True:
        return "24 horas"

    if horario is False:
        return "Cerrado"

    return horario[0] + " - " + horario[1]



# ------------------------------------------------------------- 4. MODIFICACIÓN -------------------------------------------------------------

def elegir_modificar():
    '''permite al usuario elegir un valor a modificar y llama a una función para verificar si el input es válido'''
    print("Elige valor a modificar: ")
    print("1. Nombre")
    print("2. Estado")
    print("3. Dirección")
    print("4. Espacios")
    print("5. Horario")
    print("6. Cancelar")

    eleccion = pedir_numero("Selección: ")
    eleccion = validar_modificar(eleccion)

    return eleccion

def modificar(seleccion, estacionamientos, horarios):
    '''llama a una funcion para que el usuario elija que modificar para luego llamar a la funcion que modifique el valor solicitado'''
    eleccion = elegir_modificar()
    opciones = [edit_nombre, edit_estado, edit_direccion, edit_espacios, edit_horario]

    if eleccion == 6:
        print("Modificación cancelada.")
    elif eleccion == 5:
        opciones[eleccion - 1](seleccion, horarios)
    else:
        opciones[eleccion - 1](seleccion, estacionamientos)

def edit_nombre(seleccion, estacionamientos):
    print("Nombre actual: " + str(estacionamientos[0][seleccion]))
    cambio = input("Ingrese un nuevo nombre: ")
    cambio = validar_nombre(cambio)

    estacionamientos[0][seleccion] = cambio

def edit_estado(seleccion, estacionamientos):
    print("Estado actual de '" + str(estacionamientos[0][seleccion]) + "': " + str(ver_estado(seleccion, estacionamientos)))
    print("\n1. Disponible \n2. Ocupado \n3. Fuera de servicio")
    cambio = pedir_numero("Ingrese un nuevo estado: ")
    cambio = validar_cambio_estado(cambio)
    
    estacionamientos[1][seleccion] = cambio
    print("Modificación realizada. El nuevo estado es: " + str(ver_estado(seleccion, estacionamientos)))

def edit_direccion(seleccion, estacionamientos):
    print("Dirección actual de '" + str(estacionamientos[0][seleccion]) + "': " + str(estacionamientos[2][seleccion]))
    cambio = input("Ingrese una nueva dirección: ")
    cambio = validar_direccion(cambio)

    estacionamientos[2][seleccion] = cambio
    print("Modificación realizada. La nueva dirección es: " + str(estacionamientos[2][seleccion]))

def edit_espacios(seleccion, estacionamientos):
    '''Permite editar la capacidad total o la disponible. Si la nueva cantidad de espacios totales es menor que la cantidad de espacios disponibles, se actualiza la disponibilidad para que coincida con el nuevo total.'''
    print("="*60)
    print("1. Espacio total")
    print("2. Espacio disponible")

    eleccion = pedir_numero("Seleccione una opción: ")
    
    while eleccion not in [1, 2]:
        eleccion = pedir_numero("Error, debe elegir una opción disponible: ")

    if eleccion == 1:
        print("Espacio actual de '" + str(estacionamientos[0][seleccion]) + "': " + str(estacionamientos[3][seleccion]))
        cambio = pedir_numero("Ingrese una nueva capacidad de espacio: ")
        cambio = validar_positivos(cambio)

        estacionamientos[3][seleccion] = cambio

        if cambio < estacionamientos[4][seleccion]:
            estacionamientos[4][seleccion] = cambio
            print("La capacidad disponible era mayor al cambio de capacidad total, por lo que esta se ajustó al mismo valor.")
        print("Modificación realizada. La nueva capacidad es: " + str(estacionamientos[3][seleccion]))

    else:
        print("Espacio disponible de '" + str(estacionamientos[0][seleccion]) + "': " + str(estacionamientos[4][seleccion]))
        cambio = pedir_numero("Ingrese la nueva capacidad disponible: ")
        cambio = validar_positivos(cambio)

        while cambio > estacionamientos[3][seleccion]:
            cambio = pedir_numero("Error, la capacidad disponible no debe ser mayor a la capacidad total: ")
            cambio = validar_positivos(cambio)

        estacionamientos[4][seleccion] = cambio
        print("Modificación realizada. La nueva capacidad disponible es: " + str(estacionamientos[4][seleccion]))

def edit_horario(seleccion, horarios):
    '''permite modificar un horario de un dia especifico'''

    dias = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    ]

    dia = -1

    while dia != 0:
        print("\nSeleccione el día:")
    
        for i in range(len(dias)):
            print(str(i + 1) + ". " + dias[i])
        print("0. Volver atrás")

        dia = pedir_numero("Ingrese una opción: ")

        if dia != 0:
            opcion = validar_dia(dia)
            dia = opcion  # Mantiene el valor original (1 a 7) para que el while no evalúe 0

            opcion -= 1  # Restamos 1 solo al índice para buscar correctamente en la lista

            horario = horarios[seleccion][opcion]

            print("Horario actual:", mostrar_horario(horario))

            print()
            print("1. Horario normal")
            print("2. 24 horas")
            print("3. Cerrado")

            tipo = pedir_numero("Seleccione el tipo de horario: ") 
            tipo = validar_tipo_horario(tipo)

            if tipo == 1:
                horarios[seleccion][opcion] = tipo_horario_1()

            elif tipo == 2:
                horarios[seleccion][opcion] = True

            else:
                horarios[seleccion][opcion] = False

            print("Modificación realizada.")
            print("Nuevo horario:", mostrar_horario(horarios[seleccion][opcion]))

def tipo_horario_1():
    '''Solicita el ingreso de horario en una sola cadena HH:MM, aplicando todas las validaciones.'''
    apertura = input("Ingrese hora de apertura (Formato HH:MM, ej. 08:30): ")
    while not (validar_formato_hora(apertura) and validar_horario(apertura)):
        apertura = input("Formato o rango incorrecto. Ingrese apertura nuevamente (HH:MM): ")
        
    cierre = input("Ingrese hora de cierre (Formato HH:MM, ej. 22:00): ")
    while not (validar_formato_hora(cierre) and validar_horario(cierre) and validar_cierre(apertura, cierre)):
        print("Error: El cierre debe tener un formato válido y ser posterior a la apertura.")
        cierre = input("Ingrese cierre nuevamente (HH:MM): ")
        
    # Retorna la lista con los dos límites cargados listos para guardar en tu matriz de horarios
    return [apertura, cierre]



# ------------------------------------------------------------- 5. ELIMINACIÓN -------------------------------------------------------------

def eliminar_estacionamiento(estacionamientos, horarios):
    '''Permite eliminar un estacionamiento de la matriz y sus horarios, exigiendo un código de seguridad.'''
    mostrar_estacionamientos(estacionamientos)
    
    if len(estacionamientos[0]) <= 1:
        print("No hay estacionamientos registrados para eliminar.")
        return None

    sel = pedir_numero("Seleccione el número del estacionamiento que desea eliminar: ")
    
    while sel < 1 or sel >= len(estacionamientos[0]):
        print("Opción no válida.")
        sel = pedir_numero("Seleccione un estacionamiento válido: ")

    nombre_a_borrar = estacionamientos[0][sel]
    print(f"\n¡ADVERTENCIA! Está a punto de eliminar el estacionamiento: '{nombre_a_borrar}'")
    
    # Protocolo de seguridad por código
    codigo_seguridad = "BORRAR"
    confirmacion = input(f"Para confirmar la eliminación, escriba exactamente el código '{codigo_seguridad}': ")

    if confirmacion == codigo_seguridad:
        del estacionamientos[0][sel]
        del estacionamientos[1][sel]
        del estacionamientos[2][sel]
        del estacionamientos[3][sel]
        del estacionamientos[4][sel]
        del horarios[sel]
        print(f"Estacionamiento '{nombre_a_borrar}' eliminado correctamente del sistema.")
        return sel # Le avisa al main qué índice se borró
    else:
        print("\n-- OPERACIÓN CANCELADA: El código de confirmación es incorrecto --")
        return None