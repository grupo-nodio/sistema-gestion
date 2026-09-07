import re
from functools import reduce
"""
Seccion usuarios

Permite dar de alta, listar, dar de baja, modificar y reactivar
usuarios utilizando listas paralelas como almacenamiento en memoria.

"""
def validar_nombre(texto):
    """
    Valida que un Nombre o apellido tenga un formato en el que no se puedan ingresar numeros.
    
    """
    patron = r"[A-Za-zÁÉÍÓÚáéíóúÑñ]+(?:[ '-][A-Za-zÁÉÍÓÚáéíóúÑñ]+)*"
    return (re.fullmatch(patron, texto))

def validar_email(email):
    """
    Valida que un correo electrónico tenga un formato básico válido.
    """
    patron = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    return re.fullmatch(patron, email)

def lineas():
    """
    Printea una linea divisora en la consola, sirve para que se vea mejor esteticamente
    el programa

    """
    print("-"*60)


def alta(lst_nombre,lst_apellido,lst_dni,lst_email,lst_telefono,lst_estado):
    """

    Esta funcion solicita y valida datos ingresados por el usuario para registrar su alta y guardarlos en listas diferentes.

    La funcion verifica que:
    - El DNI sea exactamente de 8 digitos y no este duplicado
    - El mail tenga un @
    - El telefono sea exactamente de 10 digitos.
    
    Asigna automaticamente el estado 'A' (Activo) al usuario y agrega los datos
    a las listas correspondientes pasadas como parametros.

    """
    print("CREACION DE USUARIO")
    lineas()
    nom=input("Ingrese su nombre:")
    while not validar_nombre(nom):
        print("Nombre inválido. Solo se permiten letras, espacios, guiones y apóstrofes.")
        nom = input("Ingrese su nombre nuevamente: ")

    apellido_1=input("Ingrese su apellido:")
    while not validar_nombre(apellido_1):
        print("Apellido inválido. Solo se permiten letras, espacios, guiones y apóstrofes.")
        apellido_1 = input("Ingrese su apellido nuevamente: ")
    #Verificacion DNI

    dni_1=input("Ingrese su DNI:")
    while not re.match(r"^\d{8}$", dni_1):
        print("DNI INVALIDO, TIENE QUE TENER EXACTAMENTE 8 CARACTERES.")
        dni_1=input("Ingrese su DNI:")
        

    while dni_1 in lst_dni:
        print("ERROR, EL DNI YA EXISTE, un dni no puede estar duplicado.")
        dni_1 = input("Ingrese su DNI:")
        while not re.match(r"^\d{8}$", dni_1):
            print("DNI INVALIDO, TIENE QUE TENER EXACTAMENTE 8 CARACTERES.")
            dni_1=input("Ingrese su DNI:")


    email_1=input("Ingrese eMail:")
    #Verificacion email
    while not validar_email(email_1):
        print("Correo inválido. Ejemplo válido: nombre@dominio.com")
        email_1 = input("Ingrese eMail nuevamente: ")


    telefono_1=input("Ingrese telefono (prefijo 11 o 15 + 8 dígitos, ej. 1112345678):")
    #Verificacion telefono: debe comenzar con 11 o 15 seguido de 8 dígitos
    while not re.match(r"^(?:11|15)\d{8}$", telefono_1):
        print("Teléfono inválido. Debe comenzar con '11' o '15' seguido de 8 dígitos (ej. 1112345678).")
        telefono_1=input("Ingrese telefono:")

    estado="A"

    lst_nombre.append(nom)
    lst_apellido.append(apellido_1)
    lst_dni.append(dni_1)
    lst_email.append(email_1)
    lst_telefono.append(telefono_1)
    lst_estado.append(estado)

    print("--USUARIO CREADO--")
    return lst_nombre,lst_apellido,lst_dni,lst_email,lst_telefono

def mostrar_usuarios(lst_nombre,lst_apellido,lst_dni,lst_email,lst_telefono,lst_estado):
    """
    Esta funcion muestra unicamente los usuarios que estan dados de ALTA, esto
    se identifica si el estado=A, si no fuese asi, no se mostrarian aunque estuvieran
    en la memoria del programa.
    
    """
    if not lst_dni:
        print("No hay usuarios")
        lineas()
        return

    indices = range(len(lst_dni))
    indices_activos = list(filter(lambda i: lst_estado[i] == "A", indices))
    lineas_usuarios = list(map(lambda i: "Nombre: " + lst_nombre[i] + " Apellido: " + lst_apellido[i] + " DNI: " + lst_dni[i] + " Mail: " + lst_email[i] + " Telefono: " + lst_telefono[i] + " Estado: " + lst_estado[i], indices_activos))
    cantidad_activos = reduce(lambda total, i: total + 1, indices_activos, 0)

    print("LISTA DE CLIENTES \n")
    for linea_usuario in lineas_usuarios:
        print(linea_usuario)
        lineas()


    if cantidad_activos == 0:
        print("No hay usuario activos")
        lineas()


def baja_usuarios(lst_dni,lst_estado):
    """
    Esta funcion modifica todos los datos del usuario(a excepcion del DNI), primero los busca por DNI, si lo encuentra
    (puede no encontrarlo y simplemente cancelar la operacion) va a pedir una nueva
    confirmacion por si realmente lo quiere dar de baja, si presiona 'y', el usuario es dado
    de baja cambiando su estado a 'B' y finalizando la operacion. Si presiona 'n', se cancela
    la operacion.
    
    """
    if not lst_dni:
        print("No hay usuarios registrados para dar de baja.")
        lineas()
        return
            
    baja_dni=input("Ingrese el dni del usuario para darlo de baja o -1 para salir:")
    if baja_dni == "-1":
        print("Operación cancelada.")
        lineas()
        return
    while not re.match(r"^\d{8}$", baja_dni):
        print("DNI INVALIDO, TIENE QUE TENER EXACTAMENTE 8 CARACTERES.")
        baja_dni=input("Ingrese el dni del usuario para darlo de baja:")
    encontrado=False
    posicion = -1
    for i in range(len(lst_dni)):
        if lst_dni[i] == baja_dni and lst_estado[i] == "A":
            posicion = i
            encontrado=True

    if encontrado==True:
        seguro=input("Esta seguro de darlo de baja? (y/n):")
        while seguro.lower() != "y" and seguro.lower() != "n":
            print("Opcion invalida, ingrese 'y' para confirmar o 'n' para cancelar.")
            seguro=input("Esta seguro de darlo de baja? (y/n):")

        if seguro.lower() == "y":
    
            lst_estado[posicion] = "B"
        
            print("--USUARIO DADO DE BAJA--")
            lineas()
            return lst_estado
        else:
            print("\n--OPERACION CANCELADA--")
            lineas()
            return
    else:
        print("\nNo se encontro ningun usuario con ese DNI activo")
        lineas()
        return


def modificar_usuario(lst_nombre,lst_apellido,lst_dni,lst_mail,lst_telefono,lst_estado):
    """
    Esta funcion va a dar de baja al usuario, primero los busca por DNI, si lo encuentra
    (puede no encontrarlo y simplemente cancelar la operacion) va a pedir todos los datos
    para modificarlos.
    
    """

    if not lst_dni:
        print("No hay usuarios registrados")
        lineas()
        return

    dni_buscar=input("Ingrese el DNI a buscar o -1 para salir:")
    if dni_buscar == "-1":
        print("Operación cancelada.")
        lineas()
        return
    
    while not re.match(r"^\d{8}$", dni_buscar):
        print("DNI INVALIDO, TIENE QUE TENER EXACTAMENTE 8 CARACTERES.")
        dni_buscar=input("Ingrese el DNI a buscar:")

    pos=-1
    encontrado=False
    for i in range(len(lst_dni)):
        if lst_dni[i] == dni_buscar and lst_estado[i] == "A":
            posicion = i
            encontrado = True
    if encontrado == True:
        print("Modificando datos para el usuario con DNI",lst_dni[posicion])
        lineas()

        nuevo_nombre=input("Ingrese el nuevo nombre: ")
        while not validar_nombre(nuevo_nombre):
                    print("Nombre inválido. Solo se permiten letras, espacios, guiones y apóstrofes.")
                    nuevo_nombre = input("Ingrese su nombre nuevamente: ")



        nuevo_apellido=input("Ingrese el nuevo apellido: ")
        while not validar_nombre(nuevo_apellido):
            print("Apellido inválido. Solo se permiten letras, espacios, guiones y apóstrofes.")
            nuevo_apellido = input("Ingrese su apellido nuevamente: ")
        # se verifica nuevo mail
        nuevo_email=input("Ingrese el nuevo eMail: ")
        while not validar_email(nuevo_email):
            print("Correo inválido. Ejemplo válido: nombre@dominio.com")
            nuevo_email = input("Ingrese eMail nuevamente: ")

        # se verifica nuevo telefono
        nuevo_telefono=input("Ingrese el nuevo teléfono (ej 11 o 15 + 8 dígitos): ")
        while not re.match(r"^(?:11|15)\d{8}$", nuevo_telefono):
            print("Teléfono inválido. Debe comenzar con '11' o '15' seguido de 8 dígitos.")
            nuevo_telefono=input("Ingrese telefono:")
        

        #Se reemplazan los antiguos valores con los nuevos
        if nuevo_nombre:
            lst_nombre[posicion] = nuevo_nombre

        if nuevo_apellido:
            lst_apellido[posicion] = nuevo_apellido

        if nuevo_email:
            lst_mail[posicion] = nuevo_email

        if nuevo_telefono:
            lst_telefono[posicion] = nuevo_telefono

        print("\n-- USUARIO MODIFICADO CON ÉXITO --")
    else:
        print("No se encontró un usuario activo con ese DNI.")

def quitar_baja(lst_nombre,lst_apellido,lst_dni,lst_mail,lst_telefono,lst_estado):
    """
    Reactiva a un usuario previamente dado de baja en el sistema.

    
    Muestra la lista de usuarios dados de baja ('B'), solicita el DNI del
    usuario a reactivar y cambia su estado a activo ('A') para evitar
    volver a cargarlo desde cero.

    """
    if not lst_dni:
        print("No hay usuarios registrados.")
        lineas()
        return

    if "B" not in lst_estado:
        print("No hay usuarios dados de baja.")
        lineas()
        return

    
    print("USUARIOS DADOS DE BAJA:")
    for i in range(len(lst_dni)):
        if lst_estado[i]=="B":
            print("Nombre:", lst_nombre[i], "Apellido:", lst_apellido[i], "DNI:", lst_dni[i], "Mail:", lst_mail[i], "Telefono:", lst_telefono[i], "Estado:", lst_estado[i])

    while True:
        dni_usuario = input("Ingrese el dni para dar nuevamente de alta o -1 para salir:")
        if dni_usuario == "-1":
            print("Operación cancelada.")
            lineas()
            return
        if not re.match(r"^\d{8}$", dni_usuario):
            print("DNI INVALIDO, TIENE QUE TENER EXACTAMENTE 8 CARACTERES.")
            

        
        posicion = -1
        for i in range(len(lst_dni)):
            if lst_dni[i] == dni_usuario:
                posicion = i
                
        if posicion != -1:  
            lst_estado[posicion] = "A"
            print("USUARIO DADO DE ALTA NUEVAMENTE")
            lineas()
            return lst_estado
        else:
            print("No se encontro ningun usuario con ese DNI dado de baja.")
            lineas()
            return