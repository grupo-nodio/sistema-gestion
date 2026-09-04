from usuarios import *
import re
#FUNCIONES PARA VEHICULOS

#VALIDAR PATENTE
def validar_patente():

    """
    Expresiones regulares para que la patente tenga 4 letras MAYUSCULAS y 3 numeros
    """

    patente = input("Ingrese la patente del vehiculo: ")
    if re.match(r'^[A-Z]{4}\d{3}$', patente):
        print("Patente válida.")
        return patente
    else:
        print("Patente inválida. Debe tener 4 letras MAYUSCULAS y 3 numeros.")

#VALIDAR TIPO DE AUTO
def validar_tipodeauto():
    """
    Expresiones Regulares para validar que el tipo de vehículo ingresado corresponda exactamente 
    a una de las opciones permitidas ('auto', 'moto' o 'camioneta').
    
    """

    tipo = input("Ingrese el tipo de vehiculo(moto, auto, camioneta): ")
    if re.match(r"^(auto|moto|camioneta)$", tipo):
        print("Tipo de vehículo válido.")
        return tipo
    else:
        print("Tipo de vehículo inválido debe ser moto, auto o camioneta.")

#INGRESAR UN VEHICULO
def ingresar_vehiculo(lista_patente, lista_tipo, lista_dnivehiculo, lista_dniusuarios):
    print("Ingresar datos del vehiculo: ")
    """
    Solicita y valida los datos necesarios para registrar un nuevo vehículo 
    """
    
    #Patente
    patente = validar_patente()
    while patente in lista_patente:
        print("la patente ya existe, porfavor ingrese otra patente")
        patente=validar_patente()

    #Tipo de vehiculo
    tipo = validar_tipodeauto()

    #DNI del usuario propietario del vehiculo
    dni_usuarios = int(input("Ingrese el DNI del usuario propietario del vehiculo: "))
    while dni_usuarios not in lista_dniusuarios:
        print("el dni ingresado no existe, porfavor ingrese un dni valido")
        dni_usuarios = int(input("Ingrese el DNI del usuario propietario del vehiculo:"))

    lista_patente.append(patente)
    lista_tipo.append(tipo)
    lista_dnivehiculo.append(dni_usuarios)


    print("Vehículo ingresado correctamente.")


def mostrar_vehiculos(lista_patente, lista_tipo, lista_dnivehiculo):
    """
    Muestra la información de todos los vehículos registrados en las listas paralelas.
    """
    if len(lista_patente) == 0:
        print("No hay vehículos registrados.")
    else:
        print("Vehículos registrados:")
        for i in range(len(lista_patente)):
            print("patente:", lista_patente[i])
            print("tipo:", lista_tipo[i])
            print("DNI del propietario:", lista_dnivehiculo[i])

#Busqueda secuencial para poder eliminar el vehiculo de la lista
def eliminar_vehiculo(lista_patente, lista_tipo, lista_dnivehiculo):
    """
    Utilizo el metodo in para buscar la patente en la lista de patentes y eliminar el vehículo correspondiente de las listas paralelas.

    """
    patente = input("Ingrese la patente del vehiculo que quiere eliminar de la lista(Ingresela en mayusculas): ")
    if patente in lista_patente:
        pos = 0 
        while pos < len(lista_patente):
            if lista_patente[pos] == patente:
                del lista_patente[pos]
                del lista_tipo[pos]
                del lista_dnivehiculo[pos]
                print("Vehículo eliminado correctamente.")
                return
            pos += 1    
    else:
        print("No se encontró un vehículo con esa patente.")

"""
Cuenta y muestra la cantidad de vehículos registrados de cada tipo (moto, auto, camioneta) en la lista proporcionada.

"""
def contar_motos(lista_contar):
    motos = list(filter(lambda x: x == "moto", lista_contar))
    print("Cantidad de motos registradas:", len(motos))

def contar_autos(lista_contar):
    autos = list(filter(lambda x: x == "auto", lista_contar))
    print("Cantidad de autos registrados:", len(autos))

def contar_camionetas(lista_contar):
    camionetas = list(filter(lambda x: x == "camioneta", lista_contar))
    print("Cantidad de camionetas registradas:", len(camionetas))



