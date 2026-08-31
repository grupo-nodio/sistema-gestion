"""
Seccion usuarios

Permite dar de alta, listar, dar de baja, modificar y reactivar
usuarios utilizando listas paralelas como almacenamiento en memoria.

"""


def lineas():
    """
    Printea una linea divisora en la consola, sirve para que se vea mejor esteticamente
    el programa

    """
    print("--------------------------------------")


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
    apellido_1=input("Ingrese su apellido:")
    dni_1=int(input("Ingrese su DNI:"))
    #Verificacion DNI
    while len(str(dni_1)) !=8:
        print("El DNI tiene que tener exactamente 8 digitos.")
        dni_1=int(input("Ingrese su DNI:"))

    while dni_1 in lst_dni:
        print("ERROR, EL DNI YA EXISTE")
        dni_1 = int(input("Ingrese su DNI:"))


    email_1=input("Ingrese eMail:")
    #Verificacion email
    while "@"  not in email_1 and "." not in email_1:
        print("El correo debe contener un '@' y un '.'")
        email_1 = input("Ingrese eMail nuevamente: ")


    telefono_1=int(input("Ingrese telefono:"))
    #Verificacion telefono
    while len(str(telefono_1)) !=10:
        print("El telefono tiene que tener exactamente 10 digitos.")
        telefono_1=int(input("Ingrese telefono:"))

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

    activo=False
    print("LISTA DE CLIENTES \n")
    for i in range(len(lst_dni)):
        if lst_estado[i] == "A":
            print("Nombre:", lst_nombre[i], "Apellido:", lst_apellido[i], "DNI:", lst_dni[i], "Mail:", lst_email[i], "Telefono:", lst_telefono[i], "Estado:", lst_estado[i])
            lineas()
            activo=True


    if activo==False:
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
            
    baja_dni=int(input("Ingrese el dni del usuario para darlo de baja:"))
    encontrado=False
    posicion = -1
    for i in range(len(lst_dni)):
        if lst_dni[i] == baja_dni and lst_estado[i] == "A":
            posicion = i
            encontrado=True

    if encontrado==True:
        seguro=input("Esta seguro de darlo de baja? (y/n):")
        if seguro == "y":

            lst_estado[posicion] = "B"
        
            print("--USUARIO DADO DE BAJA--")
            lineas()
            return lst_estado
        else:
            print("--OPERACION CANCELADA--")
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

    dni_buscar=int(input("Ingrese el DNI a buscar:"))

    pos=-1
    encontrado=False
    for i in range(len(lst_dni)):
        if lst_dni[i] == dni_buscar and lst_estado[i] == "A":
            posicion = i
            encontrado = True
    if encontrado == True:
        print("Modificando datos para el usuario con DNI",lst_dni[i])
        lineas()

        nuevo_nombre=input("Ingrese el nuevo nombre: ")
        nuevo_apellido=input("Ingrese el nuevo apellido: ")

        # se verifica nuevo mail
        nuevo_email=input("Ingrese el nuevo eMail: ")
        while "@"  not in nuevo_email and "." not in nuevo_email:
            print("El correo debe contener un '@' y un '.'")
            nuevo_email=input("Ingrese eMail nuevamente: ")

        # se verifica nuevo telefono
        nuevo_telefono=int(input("Ingrese el nuevo teléfono: "))
        while len(str(nuevo_telefono)) != 10:
            print("El teléfono tiene que tener exactamente 10 dígitos.")
            nuevo_telefono=int(input("Ingrese teléfono nuevamente: "))

        #Se reemplazan los antiguos valores con los nuevos
        lst_nombre[posicion] = nuevo_nombre
        lst_apellido[posicion] = nuevo_apellido
        lst_mail[posicion] = nuevo_email
        lst_telefono[posicion] = nuevo_telefono

        print("\n-- USUARIO MODIFICADO CON ÉXITO --")
    else:
        print("No se encontró un usuario activo con ese DNI.")

def quitar_baja(lst_nombre,lst_apellido,lst_dni,lst_mail,lst_telefono,lst_estado):
    """Reactiva a un usuario previamente dado de baja en el sistema.

    
    Muestra la lista de usuarios dados de baja ('B'), solicita el DNI del
    usuario a reactivar y cambia su estado a activo ('A') para evitar
    volver a cargarlo desde cero.

    Retorna:
        list: La lista 'lst_estado' actualizada, o None si el DNI no existe.
    """


    for i in range(len(lst_dni)):
        if lst_estado[i]=="B":
            print("Nombre:", lst_nombre[i], "Apellido:", lst_apellido[i], "DNI:", lst_dni[i], "Mail:", lst_mail[i], "Telefono:", lst_telefono[i], "Estado:", lst_estado[i])
            lineas()
        else:
            print("No hay usuarios dados de baja")
            lineas()

    dni_usuario=int(input("Ingrese el dni para dar nuevamente de alta:"))

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
            print("No se encontro ningun usuario con ese DNI")
            lineas()
            return

#PROGRAMA PRINCIPAL
# SE TUVO QUE BORRAR MAIN() POR PROBLEMAS DE IMPORTS.

nombre=[]
apellido=[]
dni=[]
email=[]
telefono=[]
estado=[]
menu=-1
while menu!=0:
    menu=int(input("--MENU DE USUARIOS--\n1)Alta de usuarios \n2)Mostrar usuarios \n3)Baja de usuarios \n4)Modificar usuario \n5)Quitar baja usuario \n0)Ingrese '0' para finalizar el programa \nSeleccione una opcion:"))
    lineas()
    if menu ==1:
        alta(nombre,apellido,dni,email,telefono,estado)

    elif menu==2:
        mostrar_usuarios(nombre,apellido,dni,email,telefono,estado)

    elif menu==3:
        baja_usuarios(dni,estado)

    elif menu==4:
        modificar_usuario(nombre,apellido,dni,email,telefono,estado)
    elif menu==5:
        quitar_baja(nombre,apellido,dni,email,telefono,estado)

    elif menu >5 or menu <0:
        print("Vuelva a seleccionar una opcion")
        lineas()


    elif menu==0:
        print("Fin del programa")
        lineas()
