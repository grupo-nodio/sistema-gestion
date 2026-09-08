from functools import reduce
from reservas import escritura_digitos

def mostrar_reportes(estacionamientos, lista_tipo, lista_dni, lista_estado, reservar, reservas_canceladas, lista_cobros):
    '''Llama a todas las estadísticas'''
    reporte_estacionamiento(estacionamientos)
    reporte_vehiculos_por_tipo(lista_tipo)
    reporte_ocupacion_estacionamiento(lista_tipo)
    reporte_usuarios_por_estado(lista_dni, lista_estado)
    reporte_reservas(reservar, reservas_canceladas)
    reporte_recaudacion(lista_cobros)

def reporte_estacionamiento(estacionamientos):
    '''Muestra en pantalla estacionamientos registrados, disponibles, no disponibles y capacidad actual disponible total'''
    indices = range(1, len(estacionamientos[0]))
    disponibles = len(list(filter(lambda i: estacionamientos[1][i] == 1, indices)))
    
    print("\nESTADÍSTICAS DE ESTACIONAMIENTOS:")
    print("Estacionamientos registrados:", len(estacionamientos[0]) - 1)
    print("Estacionamientos disponibles:", disponibles)
    print("Estacionamientos no disponibles:", (len(estacionamientos[0]) - 1) - disponibles)
    print("Capacidad actual disponible (todos los estacionamientos):", capacidad_actual_disponible(estacionamientos))

def capacidad_actual_disponible(estacionamientos):
    '''Muestra la capacidad actual sin reservar en total entre todos los estacionamientos que se encuentren disponibles.'''
    indices = range(1, len(estacionamientos[0]))
    indices_disponibles = filter(lambda i: estacionamientos[1][i] == 1, indices)
    return reduce(lambda acumulador, i: acumulador + estacionamientos[4][i], indices_disponibles, 0)

def reporte_vehiculos_por_tipo(lista_tipo):
    """Muestra un reporte de la cantidad de vehículos registrados por tipo (moto, auto, camioneta), utilizando filter para contar cada tipo de vehículo."""
    if len(lista_tipo) == 0:
        print("\nNo hay vehículos registrados.")
    else:
        motos = len(list(filter(lambda x: x in ["moto", "Moto", "MOTO"], lista_tipo)))
        autos = len(list(filter(lambda x: x in ["auto", "Auto", "AUTO"], lista_tipo)))
        camionetas = len(list(filter(lambda x: x in ["camioneta", "Camioneta", "CAMIONETA"], lista_tipo)))

        print("\nANÁLISIS DE VEHÍCULOS POR TIPO:")
        print("Cantidad de motos:", motos)
        print("Cantidad de autos:", autos)
        print("Cantidad de camionetas:", camionetas)

def reporte_ocupacion_estacionamiento(lista_tipo):
    """
    Muestra un reporte de la ocupación de estacionamientos por tipo de vehículo, utilizando filter para contar los tipos de vehículos.
    Si el vehículo es una camioneta, ocupa un espacio grande; si es un auto o moto, ocupa un espacio estándar.
    """
    if len(lista_tipo) == 0:
        return
    else:
        espacios_grandes = len(list(filter(lambda x: x in ["camioneta", "Camioneta", "CAMIONETA"], lista_tipo)))
        espacios_estandar = len(list(filter(lambda x: x in ["auto", "Auto", "AUTO", "moto", "Moto", "MOTO"], lista_tipo)))

        print("\nLOGÍSTICA DE ESPACIOS OCUPADOS:")
        print("Cantidad de espacios grandes ocupados (camionetas):", espacios_grandes)
        print("Cantidad de espacios estándar ocupados (autos y motos):", espacios_estandar)

def reporte_reservas(reservar, reservas_canceladas):
    """ Muestra únicamente las reservas realizadas y canceladas. """
    print("\n" + "=" * 44)
    print("\n REPORTE DE RESERVAS REALIZADAS \n")
    print("=" * 44)

    for i in range(len(reservar)):
        print(f"{i + 1}. Nombre: {reservar[i][0]} / dia: {escritura_digitos(reservar[i][1])} / mes: {escritura_digitos(reservar[i][2])} / año: {escritura_digitos(reservar[i][3])} / hora: {escritura_digitos(reservar[i][4])} / minuto: {escritura_digitos(reservar[i][5])} / duracion: {escritura_digitos(reservar[i][6])}hs / estacionamiento: {escritura_digitos(reservar[i][7])}.")

    print(f"Cantidad de reservas realizadas con éxito: {len(reservar)}")

    print("\n" + "=" * 44)
    print("\n REPORTE DE RESERVAS CANCELADAS \n")
    print("=" * 44)

    if len(reservas_canceladas) > 0:
        for i in range(len(reservas_canceladas)):
            # CORREGIDO: Se usa reservas_canceladas en lugar de reservar, y se aplica escritura_digitos al año
            print(f"{i + 1}. Nombre: {reservas_canceladas[i][0]} / dia: {escritura_digitos(reservas_canceladas[i][1])} / mes: {escritura_digitos(reservas_canceladas[i][2])} / año: {escritura_digitos(reservas_canceladas[i][3])} / hora: {escritura_digitos(reservas_canceladas[i][4])} / minuto: {escritura_digitos(reservas_canceladas[i][5])} / duracion: {escritura_digitos(reservas_canceladas[i][6])}hs / estacionamiento: {escritura_digitos(reservas_canceladas[i][7])}.")

        print(f"Cantidad de reservas canceladas: {len(reservas_canceladas)}")
    else:
        print("No se canceló ninguna reserva.")

def reporte_usuarios_por_estado(lista_dni, lista_estado):
    """ Reporte de usuarios dados de alta y dados de baja. """
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

def reporte_recaudacion(lista_cobros):
    """Muestra la cantidad total de dinero recaudado."""
    if len(lista_cobros) == 0:
        print("\nREPORTE DE RECAUDACIÓN:")
        print("Todavía no se registró ningún cobro en el sistema.")
    else:
        total_dinero = sum(lista_cobros)
            
        print("\nREPORTE DE RECAUDACIÓN:")
        print("Cantidad de cobros realizados:", len(lista_cobros))
        print("Total de dinero recaudado: $", total_dinero)