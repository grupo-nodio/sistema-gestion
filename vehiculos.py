from usuarios import *

#FUNCIONES

#MENU
def menu_vehiculos():
    print("Menu de vehiculos:")
    print("1. Ingresar vehículo")
    print("2. Mostrar vehículos")
    print("3. Eliminar vehículo")
    print("4. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    return opcion

# INGRESAR UN VEHICULO
def ingresar_vehiculo(lista_patente, lista_tipo, lista_dnivehiculo, lista_dniusuarios):
    print("Ingresar datos del vehiculo: ")

    #Ingresar patente del vehiculo y valido que tenga 7 caracteres y que no exista en la lista de patentes
    patente = input("Ingrese la patente del vehiculo:")
    while len(patente) != 7:
        print("La patente ingresada no es valida, por favor ingrese una patente de 7 caracteres.")
        patente = input("Ingrese la patente del vehiculo:")

    while patente in lista_patente:
        print("la patente ya existe, porfavor ingrese otra patente")
        patente = input("Ingrese la patente del vehículo: ")
        while len(patente) != 7:
            print("La patente ingresada no es valida, por favor ingrese una patente de 7 caracteres.")
            patente = input("Ingrese la patente del vehiculo:")
    #Tipo de vehiculo
    tipo = input("Ingrese el tipo de vehiculo(moto, auto, camioneta, etc):")

    #Solicito el dni del usuario propietario del vehiculo y valido que tenga 8 caracteres y que exista en la lista de dni usuario
    dni_usuarios = int(input("Ingrese el DNI del usuario propietario del vehiculo: "))
    while len(str(dni_usuarios)) != 8:
        print("El DNI ingresado no es valido, por favor ingrese un DNI de 8 dígitos.")
        dni_usuarios = int(input("Ingrese el DNI del usuario propietario del vehiculo: "))

    while dni_usuarios not in lista_dniusuarios:
        print("el dni ingresado no existe, porfavor ingrese un dni valido")
        dni_usuarios = int(input("Ingrese el DNI del usuario propietario del vehiculo:"))
        while len(str(dni_usuarios)) != 8:
            print("El DNI ingresado no es valido, por favor ingrese un DNI de 8 dígitos.")
            dni_usuarios = int(input("Ingrese el DNI del usuario propietario del vehiculo: "))

    lista_patente.append(patente)
    lista_tipo.append(tipo)
    lista_dnivehiculo.append(dni_usuarios)


    print("Vehículo ingresado correctamente.")

#Funcion para poder mostrar los vehiculos que estan registrados en el sistema, mostrando la patente, el tipo y el dni del propietario del vehiculo.
def mostrar_vehiculos(lista_patente, lista_tipo, lista_dnivehiculo):
    if not lista_patente:
        print("No hay vehículos registrados.")
    else:
        print("La lista de vehiculos registrados es la siguiente:")
        for i in range(len(lista_patente)):
            print("Patente:", lista_patente[i])
            print("Tipo:", lista_tipo[i])
            print("DNI:", lista_dnivehiculo[i])
#Busqueda secuencial 
def eliminar_vehiculo(lista_patente, lista_tipo, lista_dnivehiculo):
    patente = input("Ingrese la patente del vehiculo que quiere eliminar de la lista: ")
    pos = 0
    while pos < len(lista_patente):
        if lista_patente[pos] == patente:
            del lista_patente[pos]
            del lista_tipo[pos]
            del lista_dnivehiculo[pos]
            print("Vehículo eliminado correctamente.")
            return
        pos += 1
    print("No se encontró ningún vehículo con esa patente.")

#Programa principal






