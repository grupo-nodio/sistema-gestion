
import re
import json
from functools import reduce

def crea_archivo():
    """
    Intenta leer el archivo json, y si no existe, lo crea de cero.
    """

    try:
        with open("Usuarios.json", "r", encoding="utf-8") as archivo:
            return
    except FileNotFoundError:
        with open("Usuarios.json", "w", encoding="utf-8") as archivo:
            archivo.write("{}")


def formato_usuarios_valido(usuarios):
    """Comprueba que el JSON tenga un diccionario con los campos esperados."""
    if type(usuarios) != dict:
        return False

    campos_requeridos = ("nombre", "apellido", "email", "telefono", "estado")
    for datos in usuarios.values():
        if type(datos) != dict:
            return False

        for campo in campos_requeridos:
            if campo not in datos:
                return False

    return True


def cargar_usuarios():
    """Carga el diccionario de usuarios guardado en Usuarios.json."""
    try:
        with open("Usuarios.json", "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

        if not formato_usuarios_valido(usuarios):
            raise ValueError("el archivo debe contener usuarios con todos los campos requeridos")
    except FileNotFoundError:
        return {}
    except (json.JSONDecodeError, ValueError, AttributeError) as error:
        decision = input(
            f"Error: Usuarios.json no tiene el formato esperado ({error}). "
            "¿Desea sobrescribirlo con un diccionario vacío? (y/n): "
        )

        if decision.lower() in ("y", "yes", "s", "si"):
            datos_iniciales = {}
            reiniciar_archivo(datos_iniciales)
            return datos_iniciales

        print("Se usará un diccionario vacío. Corrija Usuarios.json para guardar cambios.")
        return {}

    return usuarios


def validar_nombre(texto):
    """
    Valida que un nombre o apellido tenga un formato en el que no se puedan ingresar numeros.
    """
    patron = r"[A-Za-zÁÉÍÓÚáéíóúÑñ]+(?:[ '-][A-Za-zÁÉÍÓÚáéíóúÑñ]+)*"
    return re.fullmatch(patron, texto)


def validar_email(email):
    """
    Valida que un correo electronico tenga un formato basico valido.
    """
    patron = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    return re.fullmatch(patron, email)

def validar_dni(dni):
    """
    Valida que el DNI tenga exactamente 8 digitos numericos.
    """
    patron = r"\d{8}"
    return re.fullmatch(patron, dni)
    
def lineas():
    """
    Printea una linea divisora en la consola, sirve para que se vea mejor esteticamente
    el programa.
    """
    print("-" * 60)


def pedir_dato_validado(mensaje, validador, mensaje_error):
    """Pide un dato válido; devuelve None si se ingresa -1."""
    while True:
        dato = input(mensaje)
        if dato == "-1":
            return None
        if validador(dato):
            return dato
        print(mensaje_error)


def guardar_json(usuarios):
    """Escribe un diccionario en Usuarios.json."""
    with open("Usuarios.json", "w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, ensure_ascii=False, indent=4)


def reiniciar_archivo(usuarios):
    """Sobrescribe el JSON después de que la persona confirma reiniciarlo."""
    if formato_usuarios_valido(usuarios) == False:
        print("No se pudo reiniciar: los datos iniciales tienen una estructura inválida.")
        return

    guardar_json(usuarios)


def escribir_archivo(usuarios):
    """Guarda usuarios si el archivo existente todavía tiene un formato válido."""
    try:
        with open("Usuarios.json", "r", encoding="utf-8") as archivo:
            datos_existentes = json.load(archivo)
    except FileNotFoundError:
        datos_existentes = {}
    except json.JSONDecodeError:
        print("No se guardaron los cambios: Usuarios.json contiene JSON inválido.")
        return

    if formato_usuarios_valido(datos_existentes) == False:
        print("No se guardaron los cambios: Usuarios.json tiene una estructura inválida.")
        return

    if formato_usuarios_valido(usuarios) == False:
        print("No se guardaron los cambios: los datos de usuarios tienen una estructura inválida.")
        return

    guardar_json(usuarios)


def actualizar_estado_archivo(usuarios, dni, nuevo_estado):
    """Actualiza el estado del usuario y guarda el diccionario en JSON."""
    usuarios[dni]["estado"] = nuevo_estado
    escribir_archivo(usuarios)

def alta(usuarios):
    """
    Solicita y valida datos para registrar un usuario.
    """
    print("CREACION DE USUARIO")
    lineas()

    nombre = pedir_dato_validado(
        "Ingrese su nombre o -1 para cancelar: ", validar_nombre,
        "Nombre invalido. Solo se permiten letras, espacios, guiones y apostrofes.", #Mensaje error
    )
    if nombre is None:
        print("Operacion cancelada.")
        lineas()
        return usuarios

    apellido = pedir_dato_validado(
        "Ingrese su apellido o -1 para cancelar: ", validar_nombre,
        "Apellido invalido. Solo se permiten letras, espacios, guiones y apostrofes.", #Mensaje error
    )
    if apellido is None:
        print("Operacion cancelada.")
        lineas()
        return usuarios

    dni = pedir_dato_validado(
        "Ingrese su DNI o -1 para cancelar: ", validar_dni,
        "DNI INVALIDO, TIENE QUE TENER EXACTAMENTE 8 CARACTERES.", #Mensaje error
    )
    if dni is None:
        print("Operacion cancelada.")
        lineas()
        return usuarios

    while dni in usuarios:
        print("ERROR, EL DNI YA EXISTE, un dni no puede estar duplicado.")
        dni = pedir_dato_validado(
            "Ingrese otro DNI o -1 para cancelar: ", validar_dni,
            "DNI INVALIDO, TIENE QUE TENER EXACTAMENTE 8 CARACTERES.", #Mensaje error
        )
        if dni is None:
            print("Operacion cancelada.")
            lineas()
            return usuarios

    email = pedir_dato_validado(
        "Ingrese eMail o -1 para cancelar: ", validar_email,
        "Correo invalido. Ejemplo valido: nombre@dominio.com", #Mensaje error
    )
    if email is None:
        print("Operacion cancelada.")
        lineas()
        return usuarios

    telefono = pedir_dato_validado(
        "Ingrese telefono (11 o 15 + 8 digitos) o -1 para cancelar: ",
        lambda numero: re.fullmatch(r"(?:11|15)\d{8}", numero),
        "Telefono invalido. Debe comenzar con '11' o '15' seguido de 8 digitos.", #Mensaje error
    )
    if telefono is None:
        print("Operacion cancelada.")
        lineas()
        return usuarios

    usuarios[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "telefono": telefono,
        "estado": "A",
    }

    escribir_archivo(usuarios)
    
    print("--USUARIO CREADO--")
    return usuarios

def formatear_usuario(item):
    #Sirve para convertir cada usuario en una linea de texto antes de imprimirlo, mas que nada esta para tener
    # implementado el map en algun lugar del codigo

    dni, datos = item
    return (
        "Nombre: " + datos["nombre"]
        + " Apellido: " + datos["apellido"]
        + " DNI: " + dni
        + " Mail: " + datos["email"]
        + " Telefono: " + datos["telefono"]
        + " Estado: " + datos["estado"]
    )

def mostrar_usuarios(usuarios):
    """
    Muestra unicamente los usuarios que estan dados de alta.
    """
    if not usuarios:
        print("No hay usuarios")
        lineas()
        return

    usuarios_activos = dict(filter(lambda item: item[1]["estado"] == "A", usuarios.items()))
    lineas_usuarios = list(map(formatear_usuario, usuarios_activos.items()))
    cantidad_activos = reduce(lambda total, _: total + 1, usuarios_activos, 0)

    print("LISTA DE CLIENTES \n")
    for linea_usuario in lineas_usuarios:
        print(linea_usuario)
        lineas()

    if cantidad_activos == 0:
        print("No hay usuario activos")
        lineas()





def baja_usuarios(usuarios):
    """
    Busca un usuario activo por DNI y, con confirmacion, cambia su estado a 'B'.
    """
    if not usuarios:
        print("No hay usuarios registrados para dar de baja.")
        lineas()
        return

    baja_dni = input("Ingrese el dni del usuario para darlo de baja o -1 para salir:")
    if baja_dni == "-1":
        print("Operacion cancelada.")
        lineas()
        return

    while not validar_dni(baja_dni):
        if baja_dni == "-1":
            print("Operacion cancelada.")
            lineas()
            return
        print("DNI INVALIDO, TIENE QUE TENER EXACTAMENTE 8 CARACTERES.")
        baja_dni = input("Ingrese el dni del usuario para darlo de baja o -1 para salir:")

    if baja_dni in usuarios and usuarios[baja_dni]["estado"] == "A":
        seguro = ("yes", "y", "no", "n")
        respuesta = input("Esta seguro de darlo de baja? (yes/no, y/n): ").lower()
        while respuesta not in seguro:
            print("Opcion invalida, ingrese 'yes' o 'y' para confirmar, 'no' o 'n' para cancelar.")
            respuesta = input("Esta seguro de darlo de baja? (yes/no, y/n): ").lower()

        if respuesta in ("yes", "y"):
            usuarios[baja_dni]["estado"] = "B"
            actualizar_estado_archivo(usuarios, baja_dni, "B")
            print("--USUARIO DADO DE BAJA--")
            lineas()
            return usuarios

        print("\n--OPERACION CANCELADA--")
        lineas()
        return

    print("\nNo se encontro ningun usuario con ese DNI activo")
    lineas()


def modificar_usuario(usuarios):
    """
    Busca un usuario activo por DNI y permite modificar todos sus datos excepto el DNI.
    """
    if not usuarios:
        print("No hay usuarios registrados")
        lineas()
        return

    dni_buscar = input("Ingrese el DNI a buscar o -1 para salir:")
    if dni_buscar == "-1":
        print("Operacion cancelada.")
        lineas()
        return

    while not validar_dni(dni_buscar):
        print("DNI INVALIDO, TIENE QUE TENER EXACTAMENTE 8 CARACTERES.")
        dni_buscar = input("Ingrese el DNI a buscar:")

    if dni_buscar in usuarios and usuarios[dni_buscar]["estado"] == "A":
        print("Modificando datos para el usuario con DNI", dni_buscar)
        lineas()

        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        while not validar_nombre(nuevo_nombre):
            print("Nombre invalido. Solo se permiten letras, espacios, guiones y apostrofes.")
            nuevo_nombre = input("Ingrese su nombre nuevamente: ")

        nuevo_apellido = input("Ingrese el nuevo apellido: ")
        while not validar_nombre(nuevo_apellido):
            print("Apellido invalido. Solo se permiten letras, espacios, guiones y apostrofes.")
            nuevo_apellido = input("Ingrese su apellido nuevamente: ")

        nuevo_email = input("Ingrese el nuevo eMail: ")
        while not validar_email(nuevo_email):
            print("Correo invalido. Ejemplo valido: nombre@dominio.com")
            nuevo_email = input("Ingrese eMail nuevamente: ")

        nuevo_telefono = input("Ingrese el nuevo telefono (ej 11 o 15 + 8 digitos): ")
        while not re.match(r"^(?:11|15)\d{8}$", nuevo_telefono):
            print("Telefono invalido. Debe comenzar con '11' o '15' seguido de 8 digitos.")
            nuevo_telefono = input("Ingrese telefono:")

        usuarios[dni_buscar]["nombre"] = nuevo_nombre
        usuarios[dni_buscar]["apellido"] = nuevo_apellido
        usuarios[dni_buscar]["email"] = nuevo_email
        usuarios[dni_buscar]["telefono"] = nuevo_telefono
        escribir_archivo(usuarios)

        print("\n-- USUARIO MODIFICADO CON EXITO --")
        return usuarios

    print("\nNo se encontro un usuario activo con ese DNI.")


def quitar_baja(usuarios):
    """
    Reactiva a un usuario previamente dado de baja en el sistema.
    """
    if not usuarios:
        print("No hay usuarios registrados.")
        lineas()
        return

    usuarios_baja = dict(filter(lambda item: item[1]["estado"] == "B", usuarios.items()))
    if not usuarios_baja:
        print("No hay usuarios dados de baja.")
        lineas()
        return

    print("USUARIOS DADOS DE BAJA:")
    for dni, datos in usuarios_baja.items():
        print(
            "Nombre:", datos["nombre"],
            "Apellido:", datos["apellido"],
            "DNI:", dni,
            "Mail:", datos["email"],
            "Telefono:", datos["telefono"],
            "Estado:", datos["estado"],
        )

    while True:
        dni_usuario = input("Ingrese el dni para dar nuevamente de alta o -1 para salir:")
        if dni_usuario == "-1":
            print("Operacion cancelada.")
            lineas()
            return

        if validar_dni(dni_usuario):
            if dni_usuario in usuarios_baja:
                usuarios[dni_usuario]["estado"] = "A"
                escribir_archivo(usuarios)
                print("\nUSUARIO DADO DE ALTA NUEVAMENTE")
                lineas()
                return usuarios

            print("\nNo se encontro ningun usuario con ese DNI dado de baja.")
            lineas()
            return

        print("\nDNI INVALIDO, TIENE QUE TENER EXACTAMENTE 8 CARACTERES.")
        lineas()
