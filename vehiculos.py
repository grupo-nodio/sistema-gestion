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
    for v in vehiculos:
        if v["patente"] == patente.upper():
            print("La patente ingresada ya existe en la lista de vehículos. No se puede registrar un nuevo vehículo con la misma patente.")
            return

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

        nuevo_vehiculo = {
            "patente": patente,
            "tipo": tipo,
            "dni": dni_usuarios
        }
        vehiculos.append(nuevo_vehiculo)

    if guardar_vehiculosjson(nombre_archivo, vehiculos):
        print("Vehículo registrado correctamente.")


def mostrar_vehiculos(vehiculos):
    
    vehiculos = cargar_vehiculosjson(nombre_archivo)
    if vehiculos is not None:
        if len(vehiculos) == 0:
            print("No hay vehículos registrados.")
        else:
           print("Vehículos registrados:")
           print(f"{'Patente':<15}{'Tipo':<15}{'DNI Propietario':<15}")
           print("-" * 45)
           for v in vehiculos:
                print(f"{v['patente']:<15}{v['tipo']:<15}{v['dni']:<15}")

def eliminar_vehiculo(vehiculos):
    vehiculos = cargar_vehiculosjson(nombre_archivo)
    if vehiculos is not None:
        patente = input("Ingrese la patente del vehículo que desea eliminar: ")
        encontrado = False
        actualizados = []

        for v in vehiculos:
            if v["patente"].upper() == patente:
                encontrado = True
            else:
                actualizados.append(v)

        if encontrado:
            if guardar_vehiculosjson(nombre_archivo, actualizados):
                print("Vehículo eliminado correctamente.")
        else:
            print("No se encontró un vehículo con la patente ingresada.")
   
#NOMBRE_ARCHIVO LO LLAMO EN EL MAIN
        




