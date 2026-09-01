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
        seleccion = validar_seleccion(seleccion, estacionamientos)

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
def ver_estado(seleccion, estacionamientos):
    estado = estacionamientos[1][seleccion]

    posibilidades = ["disponible", "ocupado", "fuera de servicio"]

    estado = posibilidades[estado - 1]

    return estado

def ver_horario(seleccion, horarios):
    print("Lunes:", mostrar_horario(horarios[seleccion][0]))
    print("Martes:", mostrar_horario(horarios[seleccion][1]))
    print("Miércoles:", mostrar_horario(horarios[seleccion][2]))
    print("Jueves:", mostrar_horario(horarios[seleccion][3]))
    print("Viernes:", mostrar_horario(horarios[seleccion][4]))
    print("Sábado:", mostrar_horario(horarios[seleccion][5]))
    print("Domingo:", mostrar_horario(horarios[seleccion][6]))

def mostrar_horario(horario):
    if horario is True:
        return "24 horas"

    if horario is False:
        return "Cerrado"

    return horario[0] + " - " + horario[1]

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

# 2. Modificación
def elegir_modificar():
    '''permite al usuario elegir un valor a modificar y llama a unestadoa función para verificar si el input es válido'''
    print("Elige valor a modificar: ")
    print("1. Nombre")
    print("2. Estado")
    print("3. Dirección")
    print("4. Espacios")
    print("5. Horario")
    print("6. Cancelar")

    eleccion = int(input())
    eleccion = validar_modificar(eleccion)

    return eleccion

def validar_modificar(eleccion):
    while eleccion < 1 or eleccion > 6:
        eleccion = int(input("Error, opción inválida, vuelva a elegir una opción: "))

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

# 2.6 Horario
def edit_horario(seleccion, horarios):

    dias = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    ]

    print("Seleccione el día:")
    
    for i in range(len(dias)):
        print(str(i + 1) + ". " + dias[i])

    dia = int(input("Ingrese una opción: "))
    dia = validar_dia(dia)

    dia -= 1

    horario = horarios[seleccion][dia]

    print("Horario actual:", mostrar_horario(horario))

    print()
    print("1. Horario normal")
    print("2. 24 horas")
    print("3. Cerrado")

    tipo = int(input("Seleccione el tipo de horario: "))
    tipo = validar_tipo_horario(tipo)

    if tipo == 1:
        horarios[seleccion][dia] = tipo_horario_1()

    elif tipo == 2:
        horarios[seleccion][dia] = True

    else:
        horarios[seleccion][dia] = False

    print("Modificación realizada.")
    print("Nuevo horario:", mostrar_horario(horarios[seleccion][dia]))

def tipo_horario_1():
    hora_apertura = int(input("Ingrese hora de apertura: "))
    hora_apertura = validar_hora(hora_apertura)

    minuto_apertura = int(input("Ingrese minutos de apertura: "))
    minuto_apertura = validar_minuto(minuto_apertura)

    hora_cierre = int(input("Ingrese hora de cierre: "))
    hora_cierre = validar_hora(hora_cierre)

    minuto_cierre = int(input("Ingrese minutos de cierre: "))
    minuto_cierre = validar_minuto(minuto_cierre)

    if hora_cierre * 60 + minuto_cierre <= hora_apertura * 60 + minuto_apertura:
        print("Error: el horario de cierre debe ser posterior al de apertura.")
        return tipo_horario_1()

    return [str(hora_apertura) + ":" + str(minuto_apertura), str(hora_cierre) + ":" + str(minuto_cierre)]

def validar_tipo_horario(tipo):

    while tipo < 1 or tipo > 3:
        tipo = int(input("Error, ingrese una opción válida: "))

    return tipo

def validar_dia(dia):

    while dia < 1 or dia > 7:
        dia = int(input("Error, ingrese un día válido: "))

    return dia

def validar_hora(hora):
    while hora < 0 or hora > 23:
        hora = int(input("Error, ingrese una hora válida: "))

    return hora

def validar_minuto(minuto):
    while minuto < 0 or minuto > 59:
        minuto = int(input("Error, ingrese un minuto válido: "))

    return minuto

# 3. Creación
def crear_estacionamiento(estacionamientos, horarios):
    print("Crear nuevo estacionamiento:")
    estacionamientos[0].append(crear_nombre())
    estacionamientos[1].append(crear_estado())
    estacionamientos[2].append(crear_direccion())
    estacionamientos[3].append(crear_espacios())

    horarios.append(crear_horarios())

def crear_nombre():
    nombre = input("Ingrese nombre: ")

    nombre = validar_nombre(nombre)

    return nombre

def validar_nombre(nombre):
    while nombre == "":
        nombre = input("Error, el nombre no puede estar vacio, ingrese nuevamente: ")

    return nombre

def crear_estado():
    estado = int(input("Ingrese el estado actual (1. Disponible, 2. Ocupado, 3. Fuera de servicio): "))

    estado = validar_cambio_estado(estado)

    return estado

def crear_direccion():
    direccion = input("Ingrese la dirección: ")

    direccion = validar_direccion(direccion)

    return direccion

def validar_direccion(direccion):
    while direccion == "":
        direccion = input("Error, la dirección no puede estar vacia, ingrese nuevamente: ")

        return direccion

def crear_espacios():
    espacios = int(input("Ingrese la capacidad actual: "))

    espacios = validar_positivos(espacios)

    return espacios

def crear_horarios():
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
        tipo = int(input("Seleccione el tipo de horario para " + dia + ": "))
        tipo = validar_tipo_horario(tipo)

        if tipo == 1:
            horarios.append(tipo_horario_1())

        elif tipo == 2:
            horarios.append(True)

        else:
            horarios.append(False)

    return horarios

'''
#PRUEBA PROGRAMA
estacionamientos = [
    [None, "Parking del sol", "Estacione Recoleta"],  # 0 Nombre
    [None, 1, 2],                                     # 1 Estado
    [None, "Av. 123", "Calle 123"],                   # 2 Dirección
    [None, 100, 24]                                   # 3 Espacios
    ] #(columna 0 no incluida)

horarios = [None,
    [
        ["07:00", "20:00"],  # Lunes
        ["07:00", "20:00"],  # Martes
        ["07:00", "20:00"],  # Miércoles
        ["07:00", "20:00"],  # Jueves
        ["07:00", "20:00"],  # Viernes
        ["08:00", "18:00"],  # Sábado
        False                # Domingo cerrado
    ],
    [
        True,                # Lunes 24 horas
        True,                # Martes 24 horas
        True,                # Miércoles 24 horas
        True,                # Jueves 24 horas
        True,                # Viernes 24 horas
        True,                # Sábado 24 horas
        True                 # Domingo 24 horas
    ]]#str=Horario, False=cerrado, True=24hs. el largo de cada lista es de 7 por los dias de la semana

seleccion = elegir_estacionamiento(estacionamientos)

for i in range(1, len(estacionamientos[1])):
    print("'" + str(estacionamientos[0][i]) + "' se encuentra " + str(ver_estado(i, estacionamientos)) + ".")
'''