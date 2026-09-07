#Reportes de Vehículos (Logística de Espacios)
from functools import reduce

def mostrar_reportes(estacionamientos, lista_tipo):
    print("Cantidad de estacionamientos:", len(estacionamientos) - 1)

    disponibles = len(filter(lambda i: estacionamientos[1][i] == 1, estacionamientos[0][i]))
    print("\nESTADISTICAS DE ESTACIONAMIENTOS:")
    print("Estacionamientos registrados:", len(estacionamientos[0] - 1))
    print("Estacionamientos disponibles:", disponibles)
    print("Estacionamientos no disponibles:", len(estacionamientos[0]) - disponibles - 1)
    print("Capacidad actual disponible(todos los estacionamientos):", capacidad_actual_disponible(estacionamientos))
    reporte_ocupacion_estacionamiento(lista_tipo)

def capacidad_actual_disponible(estacionamientos):
    indices = range(1, len(estacionamientos[0]))

    indices_disponibles = filter(lambda i: estacionamientos[1][i] == 1, indices)

    return reduce(lambda acumulador, i: acumulador + estacionamientos[4][i], indices_disponibles, 0) No newline at end of file

def reporte_vehiculos_por_tipo(lista_tipo):
    if len(lista_tipo) == 0:
        print("No hay vehículos registrados.")
    else:
        motos = len(list(filter(lambda x: x == "moto" or x == "Moto" or x == "MOTO", lista_tipo)))
        autos = len(list(filter(lambda x: x == "auto" or x == "Auto" or x == "AUTO", lista_tipo)))
        camionetas = len(list(filter(lambda x: x == "camioneta" or x == "Camioneta" or x == "CAMIONETA", lista_tipo)))

        print("\nANALISIS DE VEHÍCULOS POR TIPO:")
        print("Cantidad de motos:", motos)
        print("Cantidad de autos:", autos)
        print("Cantidad de camionetas:", camionetas)

#Buscador por patente
def reporte_ocupacion_estacionamiento(lista_tipo):
    if len(lista_tipo) == 0:
        print("No hay vehículos registrados.")
    else:
        espacios_grandes = len(list(filter(lambda x: x == "camioneta" or x == "Camioneta" or x == "CAMIONETA", lista_tipo)))
        espacios_estandar = len(list(filter(lambda x: x == "auto" or x == "Auto" or x == "AUTO" or x == "moto" or x == "Moto" or x == "MOTO", lista_tipo)))

        print("Cantidad de espacios grandes ocupados (camionetas):", espacios_grandes)
        print("Cantidad de espacios estándar ocupados (autos y motos):", espacios_estandar)