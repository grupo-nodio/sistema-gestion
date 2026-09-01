import re

def pedir_numero(mensaje):
    '''Solicita un valor al usuario y verifica con Regex que solo contenga números.'''
    valor = input(mensaje)
    
    # ^\d+$ significa:
    # ^: inicio de cadena[cite: 1]
    # \d: cualquier dígito numérico[cite: 1]
    # +: una o más veces[cite: 1]
    # $: fin de cadena[cite: 1]
    while not re.match(r"^\d+$", valor):
        valor = input("Error, debe ingresar únicamente números. " + mensaje)
        
    # Como ya validamos que son números, podemos convertirlo a int() de forma segura
    return int(valor)

# 1. Mostrar información
def mostrar_estacionamientos(estacionamientos):
    '''Muestra la lista de los estacionamientos usando map() en lugar de un bucle for tradicional.'''
    print("Estacionamientos en la base de datos: ")
    indices = range(1, len(estacionamientos)) # Evitamos la columna 0 (None)
    
    # map() aplica la función de impresión a cada índice de manera limpia [2]
    list(map(lambda i: print(f"Estacionamiento {i}: '{estacionamientos[i]}' - Dirección: {estacionamientos[4][i]}"), indices))

def ver_estacionamientos_disponibles(estacionamientos):
    '''Filtra y muestra únicamente los estacionamientos con estado Disponible (1) usando filter() y map() [2, 3].'''
    indices = range(1, len(estacionamientos))
    
    # filter() conserva solo los índices cuyo estado en la fila 1 es igual a 1 (Disponible) [3]
    disponibles = list(filter(lambda i: estacionamientos[1][i] == 1, indices))
    
    print("\nEstacionamientos Libres/Disponibles:")
    if len(disponibles) == 0:
        print("No hay estacionamientos disponibles en este momento.")
    else:
        list(map(lambda i: print(f"- '{estacionamientos[i]}' en {estacionamientos[4][i]}"), disponibles))

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
    cambio = pedir_numero("Ingrese un nuevo estado: ")
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
    cambio = pedir_numero("Ingrese una nueva capacidad de espacio: ")
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
    '''Solicita el ingreso de horario en una sola cadena HH:MM, aplicando todas las validaciones.'''
    apertura = input("Ingrese hora de apertura (Formato HH:MM, ej. 08:30): ")
    while not (validar_formato_hora(apertura) and es_horario_valido(apertura)):
        apertura = input("Formato o rango incorrecto. Ingrese apertura nuevamente (HH:MM): ")
        
    cierre = input("Ingrese hora de cierre (Formato HH:MM, ej. 22:00): ")
    while not (validar_formato_hora(cierre) and es_horario_valido(cierre) and es_cierre_posterior(apertura, cierre)):
        print("Error: El cierre debe tener un formato válido y ser posterior a la apertura.")
        cierre = input("Ingrese cierre nuevamente (HH:MM): ")
        
    # Retorna la lista con los dos límites cargados listos para guardar en tu matriz de horarios [12]
    return [apertura, cierre]

def validar_tipo_horario(tipo):

    while tipo < 1 or tipo > 3:
        tipo = int(input("Error, ingrese una opción válida: "))

    return tipo

def validar_dia(dia):

    while dia < 1 or dia > 7:
        dia = int(input("Error, ingrese un día válido: "))

    return dia

def validar_formato_hora(horario_str):
    '''Verifica que la cadena cumpla exactamente con el formato HH:MM (ej. 08:30) [8].'''
    # Clase 4: ^ (inicio), \d{2} (dos dígitos), : (dos puntos), \d{2} (dos dígitos), $ (fin) [8, 11]
    patron = r"^\d{2}:\d{2}$"
    return re.match(patron, horario_str)

def es_horario_valido(horario_str):
    '''Valida lógicamente las horas (00-23) y minutos (00-59) extrayéndolos con rebanado [9].'''
    # Clase 3: Usamos rebanado para extraer horas y minutos [9, 10]
    hora = int(horario_str[0:2])
    minuto = int(horario_str[3:5])
    return 0 <= hora <= 23 and 0 <= minuto <= 59

def es_cierre_posterior(apertura, cierre):
    '''Valida con rebanado que la hora de cierre sea lógicamente posterior a la de apertura [9].'''
    hora_ap = int(apertura[0:2])
    min_ap = int(apertura[3:5])
    
    hora_ci = int(cierre[0:2])
    min_ci = int(cierre[3:5])
    
    # Convertimos a minutos totales para comparar lógicamente de manera sencilla
    total_min_apertura = hora_ap * 60 + min_ap
    total_min_cierre = hora_ci * 60 + min_ci
    
    return total_min_cierre > total_min_apertura

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
    # El patrón ^[\w\s]+$ significa:
    # ^: inicio de cadena
    # [\w\s]: conjunto que acepta caracteres de palabra o espacios
    # +: una o más repeticiones (así evitamos que esté vacío)
    # $: fin de cadena
    while not re.match(r"^[\w\s]+$", nombre):
        nombre = input("Error, nombre inválido (solo se permiten letras, números y espacios). Ingrese nuevamente: ")

    return nombre

def crear_estado():
    estado = pedir_numero("Ingrese el estado actual (1. Disponible, 2. Ocupado, 3. Fuera de servicio): ")
    estado = validar_cambio_estado(estado)
    return estado

def crear_direccion():
    direccion = input("Ingrese la dirección: ")

    direccion = validar_direccion(direccion)

    return direccion

def validar_direccion(direccion):
    # Utilizamos el mismo patrón de validación estructural con re.match()
    while not re.match(r"^[\w\s]+$", direccion):
        direccion = input("Error, dirección inválida o vacía. Ingrese nuevamente: ")

    return direccion

def crear_espacios():
    espacios = pedir_numero("Ingrese la capacidad actual: ")
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