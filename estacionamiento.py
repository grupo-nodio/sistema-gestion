import re, json

# --------------------------------------------------- 1. VALIDACIONES Y MANEJO DE ARCHIVOS -------------------------------------------------

# Se usa en validar_modificar, validar_cambio_estado, validar_positivos, validar_tipo_horario, validar_dia, elegir_estacionamiento, elegir_modificar, edit_estado, edit_espacios, edit_horario, crear_espacios, crear_horarios, eliminar_estacionamiento
def pedir_numero(mensaje):
    '''Solicita un valor al usuario y verifica con try si se puede converir en entero.'''
    while True:
        valor = input(mensaje)

        try:
            return int(valor)
        except ValueError:
            print("Error, debe ingresar únicamente números.")

# Se usa en elegir_modificar
def validar_modificar(eleccion):
    '''se llama a la funcion para validar si la eleccion es alguna de las permitidas'''
    while eleccion < 1 or eleccion > 6:
        eleccion = pedir_numero("Error, opción inválida, vuelva a elegir una opción: ")

    return eleccion

# Se usa en edit_estado
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
    '''Valida lógicamente las horas (00-23) y exige minutos estrictamente en 00 o 30.'''
    hora = int(horario_str[0:2])
    minuto = int(horario_str[3:5])
    return 0 <= hora <= 23 and minuto in {0, 30}
 
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

# Manejo de Archivos JSON
def guardar_estacionamiento(archivo_json, datos):
    '''reemplaza los datos antiguos del archivo JSON con los nuevos del diccionario en Python'''
    with open(archivo_json, 'w', encoding= 'UTF-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def cargar_estacionamiento(archivo_json):
    '''carga el diccionario desde el archivo JSON, si no existe crea el archivo e inicializa el diccionario'''
    try:
        with open(archivo_json, 'r', encoding= 'UTF-8') as f:
            datos_json = json.load(f)

        datos_convertidos = {}

        for clave, valor in datos_json.items():
            if int(clave) <= 0:
                raise ValueError

            datos_convertidos[int(clave)] = valor

        return datos_convertidos

    except (json.JSONDecodeError, ValueError, AttributeError):
        decision = input(f"Error: {archivo_json} debe sobreescribirse ya que no cumple con las condiciones de diccionario con indices naturales positivos consecutivos. ¿Desea continuar?: ")

        if decision.lower() in ('y', 'yes', 's', 'si'):
            datos_iniciales = {}
            guardar_estacionamiento(archivo_json, datos_iniciales)
            return datos_iniciales
        
        else:
            print(f"Se inicializara con un diccionario vacío en memoria, en caso de querer utilizar el programa, deberá cambiar de fichero o renombrar su '{archivo_json}'")
            return {}

    except FileNotFoundError:
        datos_iniciales = {}
        guardar_estacionamiento(archivo_json, datos_iniciales)
        return datos_iniciales

# ------------------------------------------------------------- 2. CREACIÓN -------------------------------------------------------------

def crear_estacionamiento(estacionamientos, archivo_json):
    '''Crea un estacionamiento con áreas y capacidad indicada por el administrador.'''
    print("Crear nuevo estacionamiento:")

    nuevo_id = max(estacionamientos.keys(), default=0) + 1

    nombre = crear_nombre()
    direccion = crear_direccion()
    sectores = crear_sectores()

    print("Sume la capacidad de todas las áreas que tienen lugares.")
    capacidad_total = pedir_numero("Capacidad total del estacionamiento: ")
    capacidad_total = validar_positivos(capacidad_total)

    horarios = crear_horarios()

    estacionamientos[nuevo_id] = {
        "nombre": nombre,
        "estado": 1,
        "direccion": direccion,
        "capacidad_total": capacidad_total,
        "capacidad_actual": capacidad_total,
        "horarios": horarios,
        "sectores": sectores
    }

    guardar_estacionamiento(archivo_json, estacionamientos)
    print(f"Estacionamiento '{nombre}' creado con éxito.")

def crear_nombre():
    nombre = input("Ingrese nombre: ")

    nombre = validar_nombre(nombre)

    return nombre

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

    dias = (
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    )

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

def mostrar_informacion(seleccion, estacionamientos):
    '''Muestra los datos y el primer sector con espacios disponibles.'''
    ver_nombre = lambda seleccion, estacionamientos: estacionamientos[seleccion]['nombre']
    ver_direccion = lambda seleccion, estacionamientos: estacionamientos[seleccion]['direccion']
    ver_espacios = lambda seleccion, estacionamientos: estacionamientos[seleccion]['capacidad_total']

    print("Nombre:", ver_nombre(seleccion, estacionamientos))
    print("Estado:", ver_estado(seleccion, estacionamientos))
    print("Dirección:", ver_direccion(seleccion, estacionamientos))
    print("Espacios:", ver_espacios(seleccion, estacionamientos))
    print("Espacios disponibles:", estacionamientos[seleccion]["capacidad_actual"])

    print("Horarios:")
    ver_horario(seleccion, estacionamientos)

    ver_sector_disponible(seleccion, estacionamientos)

def mostrar_estacionamientos(estacionamientos):
    '''Itera sobre las claves (IDs) y valores del diccionario.'''
    print("Estacionamientos en la base de datos: ")
    
    activos = {k: v for k, v in estacionamientos.items() if v["nombre"] != "ELIMINADO"}
    
    if not activos:
        print("No hay estacionamientos activos.")
    else:
        for id_est, datos in activos.items():
            print(f"Estacionamiento {id_est}: '{datos['nombre']}' - Dirección: {datos['direccion']}")

def elegir_estacionamiento(estacionamientos):
    '''Permite seleccionar cualquier estacionamiento existente para administrarlo, sin restringir por su estado actual.'''
    mostrar_estacionamientos(estacionamientos)

    while True:
        try:
            # Usamos pedir_numero para evitar errores si ingresan letras
            seleccion = pedir_numero("Seleccione un estacionamiento: ")

            if seleccion < 0 or estacionamientos[seleccion]['nombre'] == "ELIMINADO":
                raise KeyError

            print("'" + str(estacionamientos[seleccion]['nombre']) + "' seleccionado.")
            return seleccion
        except KeyError:
            print("Error: La opción ingresada no es válida o el estacionamiento ya no existe.")

def ver_estado(seleccion, estacionamientos):
    '''Devuelve en forma de string el estado del estacionamiento.'''
    estado = estacionamientos[seleccion]['estado']

    posibilidades = ("disponible", "ocupado", "fuera de servicio")

    estado = posibilidades[estado - 1]

    return estado

def ver_horario(seleccion, estacionamientos):
    '''muestra el horario de cada día de la semana'''
    print("Lunes:", mostrar_horario(estacionamientos[seleccion]['horarios'][0]))
    print("Martes:", mostrar_horario(estacionamientos[seleccion]['horarios'][1]))
    print("Miércoles:", mostrar_horario(estacionamientos[seleccion]['horarios'][2]))
    print("Jueves:", mostrar_horario(estacionamientos[seleccion]['horarios'][3]))
    print("Viernes:", mostrar_horario(estacionamientos[seleccion]['horarios'][4]))
    print("Sábado:", mostrar_horario(estacionamientos[seleccion]['horarios'][5]))
    print("Domingo:", mostrar_horario(estacionamientos[seleccion]['horarios'][6]))

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

def modificar(seleccion, estacionamientos, archivo_json):
    '''llama a una funcion para que el usuario elija que modificar para luego llamar a la funcion que modifique el valor solicitado'''
    eleccion = elegir_modificar()
    opciones = (edit_nombre, edit_estado, edit_direccion, edit_espacios, edit_horario)

    if eleccion == 6:
        print("Modificación cancelada.")
    else:
        opciones[eleccion - 1](seleccion, estacionamientos)
        guardar_estacionamiento(archivo_json, estacionamientos)

def edit_nombre(seleccion, estacionamientos):
    print("Nombre actual: " + str(estacionamientos[seleccion]['nombre']))
    cambio = input("Ingrese un nuevo nombre: ")
    cambio = validar_nombre(cambio)

    estacionamientos[seleccion]['nombre'] = cambio

def edit_estado(seleccion, estacionamientos):
    datos = estacionamientos[seleccion]

    print(f"Estado actual de '{datos['nombre']}': {ver_estado(seleccion, estacionamientos)}")
    print("\n1. Disponible\n2. Ocupado\n3. Fuera de servicio")

    estado_valido = False

    while not estado_valido:
        cambio = pedir_numero("Ingrese un nuevo estado: ")
        cambio = validar_cambio_estado(cambio)

        if cambio == 1 and datos["capacidad_actual"] == 0:
            print("No puede estar disponible sin espacios libres.")
        elif cambio == 2 and datos["capacidad_actual"] > 0:
            print("No puede estar ocupado si todavía hay espacios libres.")
        else:
            datos["estado"] = cambio
            estado_valido = True

    print("Modificación realizada. El nuevo estado es:", ver_estado(seleccion, estacionamientos))

def edit_direccion(seleccion, estacionamientos):
    datos = estacionamientos[seleccion]

    print(f"Dirección actual de '{datos['nombre']}': {datos['direccion']}")
    cambio = input("Ingrese una nueva dirección: ")
    datos["direccion"] = validar_direccion(cambio)

    print(f"Modificación realizada. La nueva dirección es: {datos['direccion']}")

def edit_espacios(seleccion, estacionamientos):
    estacionamiento = estacionamientos[seleccion]
    sector = elegir_sector_final(estacionamiento["sectores"])

    if sector is None:
        return

    print(f"Área seleccionada: {sector['nombre']}")
    print("1. Capacidad total del área")
    print("2. Espacios disponibles en el área")

    eleccion = pedir_numero("Seleccione una opción: ")

    while eleccion not in (1, 2):
        eleccion = pedir_numero("Seleccione 1 o 2: ")

    if eleccion == 1:
        nueva_capacidad = pedir_numero("Nueva capacidad total del área: ")
        nueva_capacidad = validar_positivos(nueva_capacidad)

        sector["capacidad_total"] = nueva_capacidad

        if sector["capacidad_actual"] > nueva_capacidad:
            sector["capacidad_actual"] = nueva_capacidad

    else:
        disponibles = pedir_numero(
            f"Espacios disponibles en el área (0 a {sector['capacidad_total']}): "
        )

        while disponibles < 0 or disponibles > sector["capacidad_total"]:
            print("La cantidad debe estar entre 0 y la capacidad del área.")
            disponibles = pedir_numero(
                f"Espacios disponibles en el área (0 a {sector['capacidad_total']}): "
            )

        sector["capacidad_actual"] = disponibles

    print("Actualice los totales del estacionamiento según todas sus áreas.")

    total = pedir_numero("Capacidad total del estacionamiento: ")
    total = validar_positivos(total)

    disponibles = pedir_numero("Espacios disponibles en el estacionamiento: ")

    while disponibles < 0 or disponibles > total:
        print("Los disponibles deben estar entre 0 y la capacidad total.")
        disponibles = pedir_numero(
            "Espacios disponibles en el estacionamiento: "
        )

    estacionamiento["capacidad_total"] = total
    estacionamiento["capacidad_actual"] = disponibles

    if estacionamiento["estado"] != 3:
        estacionamiento["estado"] = 1 if disponibles > 0 else 2

    print(f"Capacidad total del estacionamiento: {total}")
    print(f"Espacios disponibles en el estacionamiento: {disponibles}")

def edit_horario(seleccion, estacionamientos):
    '''permite modificar un horario de un dia especifico'''

    dias = (
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    )

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

            horario = estacionamientos[seleccion]['horarios'][opcion]

            print("Horario actual:", mostrar_horario(horario))

            print()
            print("1. Horario normal")
            print("2. 24 horas")
            print("3. Cerrado")

            tipo = pedir_numero("Seleccione el tipo de horario: ") 
            tipo = validar_tipo_horario(tipo)

            if tipo == 1:
                estacionamientos[seleccion]['horarios'][opcion] = tipo_horario_1()

            elif tipo == 2:
                estacionamientos[seleccion]['horarios'][opcion] = True

            else:
                estacionamientos[seleccion]['horarios'][opcion] = False

            print("Modificación realizada.")
            print("Nuevo horario:", mostrar_horario(estacionamientos[seleccion]['horarios'][opcion]))

def tipo_horario_1():
    '''Solicita el ingreso de horario en el mismo día en intervalos de media hora.'''
    print("Nota: El horario debe iniciar y terminar en el mismo día. Minutos permitidos: 00 o 30.")
    apertura = input("Ingrese hora de apertura (Formato HH:MM, ej. 08:30): ")
    
    # Prohibimos "23:30" como apertura, porque el cierre no podría ser mayor en el mismo día
    while not (validar_formato_hora(apertura) and validar_horario(apertura) and apertura != "23:30"):
        apertura = input("Formato incorrecto o no hay margen de cierre (Máximo 23:00). Ingrese apertura nuevamente: ")
        
    cierre = input("Ingrese hora de cierre (Formato HH:MM, ej. 22:00): ")
    
    while not (validar_formato_hora(cierre) and validar_horario(cierre) and validar_cierre(apertura, cierre)):
        print("Error: El cierre debe ser posterior a la apertura (Máximo 23:30).")
        cierre = input("Ingrese cierre nuevamente: ")
        
    return (apertura, cierre)

# ------------------------------------------------------------- 5. ELIMINACIÓN -------------------------------------------------------------

def eliminar_estacionamiento(estacionamientos, archivo_json):
    '''Realiza la baja lógica de un estacionamiento.'''
    mostrar_estacionamientos(estacionamientos)

    activos = {
        k: v for k, v in estacionamientos.items()
        if v["nombre"] != "ELIMINADO"
    }

    if not activos:
        print("No hay estacionamientos activos.")
        return None

    sel = elegir_estacionamiento(estacionamientos)
    nombre_a_borrar = estacionamientos[sel]['nombre']

    print(f"\n¡ADVERTENCIA! Está a punto de eliminar el estacionamiento: '{nombre_a_borrar}'")

    codigo_seguridad = "BORRAR"
    confirmacion = input(
        f"Para confirmar la eliminación, escriba exactamente el código '{codigo_seguridad}': "
    )

    if confirmacion == codigo_seguridad:
        estacionamientos[sel]['nombre'] = "ELIMINADO"
        estacionamientos[sel]['estado'] = 3
        estacionamientos[sel]['direccion'] = "N/A"
        estacionamientos[sel]['capacidad_total'] = 0
        estacionamientos[sel]['capacidad_actual'] = 0
        estacionamientos[sel]['horarios'] = [False] * 7
        estacionamientos[sel]['sectores'] = {
            "nombre": "Sectores",
            "subsectores": []
        }

        guardar_estacionamiento(archivo_json, estacionamientos)
        print(f"Estacionamiento '{nombre_a_borrar}' eliminado correctamente del sistema.")
        return sel

    print("\n-- OPERACIÓN CANCELADA: El código de confirmación es incorrecto --")
    return None

# ================= NUEVO BLOQUE RECURSIVIDAD =================

def preguntar_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()

        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False

        print("Responda s o n.")


def crear_sector(padre):
    nombre = validar_nombre(
        input(f"Nombre de un área dentro de {padre}: ")
    )

    if preguntar_si_no(f"¿'{nombre}' contiene áreas más pequeñas? (s/n): "):
        subsectores = [crear_sector(f"'{nombre}'")]

        while preguntar_si_no(
            f"¿Agregar otra área dentro de '{nombre}'? (s/n): "
        ):
            subsectores.append(crear_sector(f"'{nombre}'"))

        return {
            "nombre": nombre,
            "subsectores": subsectores
        }

    capacidad = pedir_numero(f"Capacidad total de '{nombre}': ")
    capacidad = validar_positivos(capacidad)

    return {
        "nombre": nombre,
        "capacidad_total": capacidad,
        "capacidad_actual": capacidad
    }


def crear_sectores():
    sectores = {
        "nombre": "Sectores",
        "subsectores": [crear_sector("este estacionamiento")]
    }

    while preguntar_si_no(
        "¿Agregar otra área principal al estacionamiento? (s/n): "
    ):
        sectores["subsectores"].append(
            crear_sector("este estacionamiento")
        )

    return sectores

def elegir_sector_final(sector):
    while "subsectores" in sector:
        hijos = sector["subsectores"]

        if not hijos:
            print("No hay áreas para seleccionar.")
            return None

        print(f"\nÁreas dentro de '{sector['nombre']}':")

        numero = 1
        for hijo in hijos:
            if "subsectores" in hijo:
                tipo = "contiene otras áreas"
            else:
                tipo = "tiene lugares para estacionar"

            print(f"{numero}. {hijo['nombre']} ({tipo})")
            numero += 1

        print("0. Cancelar")
        opcion = pedir_numero("Seleccione un área: ")

        if opcion == 0:
            return None

        if 1 <= opcion <= len(hijos):
            sector = hijos[opcion - 1]
        else:
            print("Opción inválida.")

    return sector

def buscar_sector_disponible(sector, recorrido):
    recorrido = recorrido + (sector["nombre"],)

    if "subsectores" not in sector:
        if sector["capacidad_actual"] > 0:
            return recorrido, sector["capacidad_actual"]

        return None

    for hijo in sector["subsectores"]:
        resultado = buscar_sector_disponible(hijo, recorrido)

        if resultado is not None:
            return resultado

    return None

def ver_sector_disponible(seleccion, estacionamientos):
    datos = estacionamientos[seleccion]

    if datos["estado"] != 1 or datos["capacidad_actual"] <= 0:
        print("No hay áreas disponibles para estacionar.")
        return

    resultado = buscar_sector_disponible(datos["sectores"], ())

    if resultado is None:
        print("No se encontró un área con espacios disponibles.")
        return

    recorrido, disponibles = resultado

    ubicacion = ""
    for nombre in recorrido[1:]:
        if ubicacion == "":
            ubicacion = nombre
        else:
            ubicacion = ubicacion + " → " + nombre

    print(f"Primera área con lugar: {ubicacion} ({disponibles} disponibles)")

def seleccionar_activo(estacionamientos):
    for datos in estacionamientos.values():
        if datos["nombre"] != "ELIMINADO":
            return elegir_estacionamiento(estacionamientos)

    print("No hay estacionamientos activos.")
    return None

def menu_recursividad():
    archivo_json = "estacionamiento.json"
    estacionamientos = cargar_estacionamiento(archivo_json)
    opcion = -1

    while opcion != 0:
        print("\n--- DEMOSTRACIÓN DE RECURSIVIDAD ---")
        print("1. Crear estacionamiento y sectores")
        print("2. Listar estacionamientos")
        print("3. Ver información y sector con lugar")
        print("4. Modificar estacionamiento (opción 4: espacios)")
        print("5. Eliminar estacionamiento")
        print("0. Salir")

        opcion = pedir_numero("Elija una opción: ")

        if opcion == 0:
            print("Fin de la demostración.")

        elif opcion == 1:
            crear_estacionamiento(estacionamientos, archivo_json)

        elif opcion == 2:
            mostrar_estacionamientos(estacionamientos)

        elif opcion in (3, 4):
            seleccion = seleccionar_activo(estacionamientos)

            if seleccion is not None:
                if opcion == 3:
                    mostrar_informacion(seleccion, estacionamientos)
                else:
                    modificar(seleccion, estacionamientos, archivo_json)

        elif opcion == 5:
            eliminar_estacionamiento(estacionamientos, archivo_json)

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    #--------------- MENÚ FINAL RECUSIVIDAD ----------------
    menu_recursividad()