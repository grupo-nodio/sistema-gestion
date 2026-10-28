from usuarios import *
import re
import json
#FUNCIONES PARA VEHICULOS

#JSON
def cargar_vehiculosjson(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            vehiculos = json.load(archivo)
    except FileNotFoundError:
        vehiculos = []
    except (OSError, json.JSONDecodeError):
        print("Error al leer el archivo JSON")
        vehiculos = None
    return vehiculos

def guardar_vehiculosjson(nombre_archivo, vehiculos):
    guardado = False
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(vehiculos, ensure_ascii=False, indent=4)
            guardado = True
    except OSError as error:
        print("Error al guardar el archivo JSON:", error)
    return guardado

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
def ingresar_vehiculo(nombre_archivo, lista_dniusuarios):
    vehiculos = cargar_vehiculosjson(nombre_archivo)
    if vehiculos is None:
        print("No se pudo cargar la lista de vehículos. No se puede registrar un nuevo vehículo.")
        return
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

        




