from usuarios import *
import re
#FUNCIONES PARA VEHICULOS

#VALIDAR PATENTE
def validar_patente():

    """
    Expresiones Regulares para validar que la patente ingresada corresponda exactamente a uno de los formatos permitidos.
    Las patentes que acepta son Formato Nuevo o Viejo de Argentina, por ejemplo: AB123CD o ABC123, tambien formato mercosur, por ejemplo: ABC1234 o AB123CD.
    """
    while True:
        patente = input("Ingrese la patente del vehiculo (Formato Nuevo o Viejo de Argentina, o formato mercosur) por ejemplo: AB123CD o ABC123: ")
        if re.match(r'^([A-Za-z]{2}\d{3}[A-Za-z]{2}|[A-Za-z]{3}\d{3}|[A-Za-z]{3}\d{4})$', patente):
            print("Patente válida.")
            return patente
        else:
            print("Patente inválida. Formatos válidos: AB123CD, ABC123 o ABC1234")
    
#VALIDAR TIPO DE AUTO
def validar_tipodeauto():
    """
    Expresiones Regulares para validar que el tipo de vehículo ingresado corresponda exactamente 
    a una de las opciones permitidas ('auto', 'moto' o 'camioneta').

    """
    while True:
        tipo = input("Ingrese el tipo de vehiculo (moto, auto, camioneta): ")
        if re.match(r"^(auto|moto|camioneta|Auto|Moto|Camioneta|MOTO|CAMIONETA|AUTO)$", tipo):
            print("Tipo de vehículo válido.")
            return tipo
        else:
            print("Tipo de vehículo inválido. Debe ser 'moto', 'auto' o 'camioneta'.")


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
    dni_usuarios = input("Ingrese el DNI del usuario propietario del vehiculo: ")
    while dni_usuarios not in lista_dniusuarios:
        if dni_usuarios == "0":
            print("Operacion cancelada, volviendo al menu principal")
            return
        print("el dni ingresado no existe, porfavor ingrese un dni valido")
        dni_usuarios = input("Ingrese el DNI del usuario propietario del vehiculo:")

    lista_patente.append(patente)
    lista_tipo.append(tipo)
    lista_dnivehiculo.append(dni_usuarios)


    print("Vehículo ingresado correctamente.")


def mostrar_vehiculos(lista_patente, lista_tipo, lista_dnivehiculo):
    """
    Muestra la información de todos los vehículos registrados en las listas.
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
    Agrego una validacion para chequear que el auto eliminado no tenga ninguna reserva activa, en caso de que la tenga, no se podra eliminar el vehiculo y se le informara al usuario.

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
        




