import re
from functools import reduce



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


def alta(usuarios):
    """
    Solicita y valida datos para registrar un usuario.
    """
    print("CREACION DE USUARIO")
    lineas()

    nombre = input("Ingrese su nombre:")
    while not validar_nombre(nombre):
        print("Nombre invalido. Solo se permiten letras, espacios, guiones y apostrofes.")
        nombre = input("Ingrese su nombre nuevamente: ")

    apellido = input("Ingrese su apellido:")
    while not validar_nombre(apellido):
        print("Apellido invalido. Solo se permiten letras, espacios, guiones y apostrofes.")
        apellido = input("Ingrese su apellido nuevamente: ")

    dni = input("Ingrese su DNI:")
    while not validar_dni(dni):
        print("DNI INVALIDO, TIENE QUE TENER EXACTAMENTE 8 CARACTERES.")
        dni = input("Ingrese su DNI:")

    while dni in usuarios:
        print("ERROR, EL DNI YA EXISTE, un dni no puede estar duplicado.")
        dni = input("Ingrese su DNI:")
        while not validar_dni(dni):
            print("DNI INVALIDO, TIENE QUE TENER EXACTAMENTE 8 CARACTERES.")
            dni = input("Ingrese su DNI:")

    email = input("Ingrese eMail:")
    while not validar_email(email):
        print("Correo invalido. Ejemplo valido: nombre@dominio.com")
        email = input("Ingrese eMail nuevamente: ")

    telefono = input("Ingrese telefono (prefijo 11 o 15 + 8 digitos, ej. 1112345678):")
    while not re.match(r"^(?:11|15)\d{8}$", telefono):
        print("Telefono invalido. Debe comenzar con '11' o '15' seguido de 8 digitos (ej. 1112345678).")
        telefono = input("Ingrese telefono:")

    usuarios[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "telefono": telefono,
        "estado": "A",
    }

    print("--USUARIO CREADO--")
    return usuarios


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


def formatear_usuario(item):
    dni, datos = item
    return (
        "Nombre: " + datos["nombre"]
        + " Apellido: " + datos["apellido"]
        + " DNI: " + dni
        + " Mail: " + datos["email"]
        + " Telefono: " + datos["telefono"]
        + " Estado: " + datos["estado"]
    )


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
        seguro = input("Esta seguro de darlo de baja? (y/n):")
        while seguro.lower() != "y" and seguro.lower() != "n":
            print("Opcion invalida, ingrese 'y' para confirmar o 'n' para cancelar.")
            seguro = input("Esta seguro de darlo de baja? (y/n):")

        if seguro.lower() == "y":
            usuarios[baja_dni]["estado"] = "B"
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
                print("\nUSUARIO DADO DE ALTA NUEVAMENTE")
                lineas()
                return usuarios

            print("\nNo se encontro ningun usuario con ese DNI dado de baja.")
            lineas()
            return

        print("\nDNI INVALIDO, TIENE QUE TENER EXACTAMENTE 8 CARACTERES.")
        lineas()
