from functools import reduce

def mostrar_reportes(estacionamientos, lista_tipo, lista_dni, lista_estado):
    '''Llama a todas las estadísticas'''
    # Rango de índices válidos (omitiendo la cabecera/índice 0)
    indices = range(1, len(estacionamientos[0]))
    
    # Obtenemos la cantidad de estacionamientos disponibles con filter
    disponibles = len(list(filter(lambda i: estacionamientos[1][i] == 1, indices)))
    
    print("\nESTADÍSTICAS DE ESTACIONAMIENTOS:")
    print("Estacionamientos registrados:", len(estacionamientos[0]) - 1)
    print("Estacionamientos disponibles:", disponibles)
    print("Estacionamientos no disponibles:", (len(estacionamientos[0]) - 1) - disponibles)
    print("Capacidad actual disponible (todos los estacionamientos):", capacidad_actual_disponible(estacionamientos))
    
    # Llamamos a las sub-funciones de reportes
    reporte_vehiculos_por_tipo(lista_tipo)
    reporte_ocupacion_estacionamiento(lista_tipo)
    reporte_usuarios_por_estado(lista_dni, lista_estado)

def capacidad_actual_disponible(estacionamientos):
    '''Muestra la capacidad actual sin reservar en total entre todos los estacionamientos que se encuentren disponibles.'''
    indices = range(1, len(estacionamientos[0]))
    indices_disponibles = filter(lambda i: estacionamientos[1][i] == 1, indices)
    return reduce(lambda acumulador, i: acumulador + estacionamientos[4][i], indices_disponibles, 0)

def reporte_vehiculos_por_tipo(lista_tipo):
    if len(lista_tipo) == 0:
        print("\nNo hay vehículos registrados.")
    else:
        # Filtramos directamente comparando contra las opciones en mayúscula, minúscula y título
        motos = len(list(filter(lambda x: x in ["moto", "Moto", "MOTO"], lista_tipo)))
        autos = len(list(filter(lambda x: x in ["auto", "Auto", "AUTO"], lista_tipo)))
        camionetas = len(list(filter(lambda x: x in ["camioneta", "Camioneta", "CAMIONETA"], lista_tipo)))

        print("\nANÁLISIS DE VEHÍCULOS POR TIPO:")
        print("Cantidad de motos:", motos)
        print("Cantidad de autos:", autos)
        print("Cantidad de camionetas:", camionetas)

def reporte_ocupacion_estacionamiento(lista_tipo):
    if len(lista_tipo) == 0:
        return
    else:
        espacios_grandes = len(list(filter(lambda x: x in ["camioneta", "Camioneta", "CAMIONETA"], lista_tipo)))
        espacios_estandar = len(list(filter(lambda x: x in ["auto", "Auto", "AUTO", "moto", "Moto", "MOTO"], lista_tipo)))

        print("\nLOGÍSTICA DE ESPACIOS OCUPADOS:")
        print("Cantidad de espacios grandes ocupados (camionetas):", espacios_grandes)
        print("Cantidad de espacios estándar ocupados (autos y motos):", espacios_estandar)


def reporte_usuarios_por_estado(lista_dni, lista_estado):
    """
    Reporte de usuarios dados de alta y dados de baja.
    """
    if len(lista_dni) >= len(lista_estado):
        total_usuarios = len(lista_dni)
    else:
        total_usuarios = len(lista_estado)

    if total_usuarios == 0:
        print("\nUSUARIOS REGISTRADOS:")
        print("Usuarios dados de alta: 0")
        print("Usuarios dados de baja: 0")
        return

    usuarios_activos = 0
    usuarios_baja = 0

    for estado in lista_estado:
        if estado == "A":
            usuarios_activos += 1
        elif estado == "B":
            usuarios_baja += 1

    print("\nUSUARIOS REGISTRADOS:")
    print("Usuarios dados de alta:", usuarios_activos)
    print("Usuarios dados de baja:", usuarios_baja)
    print("Total de usuarios registrados:", total_usuarios)