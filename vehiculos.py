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
def ingresar_vehiculo(vehiculos, lista_dniusuarios):
    print("Ingresar datos del vehiculo: ")
    """
    Solicita y valida los datos necesarios para registrar un nuevo vehículo 
    """
    
    #Patente
    patente = validar_patente()
    while patente in vehiculos:
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

        vehiculos[patente] = {
        "tipo": tipo,
        "dni": dni_usuarios
    }
    
    print("Vehículo registrado correctamente.")


def mostrar_vehiculos(vehiculos):
    """
    Muestra la información de todos los vehículos registrados en el diccionario.
    """
    if len(vehiculos) == 0:
        print("No hay vehículos registrados.")
    else:
        print("Vehículos registrados:")
        for patente in vehiculos:
            print("Patente:", patente)
            print("tipo:", vehiculos[patente]["tipo"])
            print("DNI del propietario:", vehiculos[patente]["dni"])

#Busqueda secuencial para poder eliminar el vehiculo de la lista
def eliminar_vehiculo(vehiculos):
    """
    Utilizo el metodo in y la instruccion del para eliminar el vehiculo de la lista, si no se encuentra el vehiculo con la patente ingresada, se le informa al usuario que no se encontro el vehiculo.
    """
    patente = input("Ingrese la patente del vehiculo que quiere eliminar de la lista(Ingresela en mayusculas): ")
    try:
        del vehiculos[patente]
    except KeyError:
        print("No se encontró el vehículo con la patente ingresada.")
    else:
        print("Vehículo eliminado correctamente.")

        




