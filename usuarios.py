def lineas():
    print("-------------------------------------\n-------------------------------------")


def alta(lst_nombre,lst_apellido,lst_dni,lst_email,lst_telefono):
    
    print("CREACION DE USUARIO")
    lineas()
    nom=input("Ingrese su nombre:")
    apellido_1=input("Ingrese su apellido:")
    dni_1=int(input("Ingrese su DNI:"))
    #Verificacion DNI
    while len(str(dni_1)) !=8:
        print("El DNI tiene que tener exactamente 8 digitos.")
        dni_1=int(input("Ingrese su DNI:"))

    for dni in lst_dni:
        while dni_1 == dni:
            print("ERROR, EL DNI YA EXISTE")
            dni_1=int(input("Ingrese su DNI:"))
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

    lst_nombre.append(nom)
    lst_apellido.append(apellido_1)
    lst_dni.append(dni_1)
    lst_email.append(email_1)
    lst_telefono.append(telefono_1)

    print("--USUARIO CREADO--")
    return lst_nombre,lst_apellido,lst_dni,lst_email,lst_telefono

def mostrar_usuarios(lst_nombre,lst_apellido,lst_dni,lst_email,lst_telefono):
    if not lst_dni:
        print("No hay usuarios")
        lineas()

    print("LISTA DE CLIENTES \n")
    for i in range(len(lst_dni)):
        print("Nombre:",lst_nombre[i],"Apellido:",lst_apellido[i],"DNI:",lst_dni[i],"Mail",lst_email[i],"Telefono:",lst_telefono[i])
        lineas()

def baja_usuarios(lst_nombre,lst_apellido,lst_dni,lst_email,lst_telefono):
    pass

def main():
    nombre=[]
    apellido=[]
    dni=[]
    email=[]
    telefono=[]
    menu=-1
    while menu!=0:
        menu=int(input("Menu de usuarios \n1)Alta de usuarios \n2)Mostrar usuarios \n3)Baja de usuarios \n0)Ingrese '0' para finalizar el programa \nSeleccione una opcion:"))
        lineas()
        if menu ==1:
            crea_alta=alta(nombre,apellido,dni,email,telefono)

        elif menu==2:
            mostrar_usuarios(nombre,apellido,dni,email,telefono)

        elif menu==3:
            pass
                
        elif menu==0:
            print("Fin del programa")
main()