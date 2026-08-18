def lineas():
    print("--------------------------------------")


def alta(lst_nombre,lst_apellido,lst_dni,lst_email,lst_telefono,lst_estado):
    
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
    while "@" not in email_1:
        print("El correo debe contener un '@'")
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

        
def baja_usuarios(lst_nombre,lst_apellido,lst_dni,lst_email,lst_telefono,lst_estado):
    if not lst_dni:
        print("No hay usuarios registrados para dar de baja.")
        lineas()
        return
            
    baja_dni=int(input("Ingrese el dni del usuario para darlo de baja:"))

    posicion = -1
    for i in range(len(lst_dni)):
        if lst_dni[i] == baja_dni:
            posicion = i

    if posicion != -1:

        lst_estado[posicion] = "B"
        print("USUARIO DADO DE BAJA")
        lineas()
        return lst_estado
    else:
        print("No se encontro ningun usuario con ese DNI")
        lineas()
        return 
def main():
    nombre=[]
    apellido=[]
    dni=[]
    email=[]
    telefono=[]
    estado=[]
    menu=-1
    while menu!=0:
        menu=int(input("Menu de usuarios \n1)Alta de usuarios \n2)Mostrar usuarios \n3)Baja de usuarios \n0)Ingrese '0' para finalizar el programa \nSeleccione una opcion:"))
        lineas()
        if menu ==1:
            crea_alta=alta(nombre,apellido,dni,email,telefono,estado)

        elif menu==2:
            mostrar_usuarios(nombre,apellido,dni,email,telefono,estado)

        elif menu==3:
            baja_usuarios(nombre,apellido,dni,email,telefono,estado)
                
        elif menu==0:
            print("Fin del programa")
main()