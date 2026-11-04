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
    print("\nANÁLISIS DE VEHÍCULOS POR TIPO:")

    if len(lista_tipo) == 0:
        print("\nNo hay vehículos registrados.")
    else:
        motos = len(list(filter(lambda x: x in ["moto", "Moto", "MOTO"], lista_tipo)))
        autos = len(list(filter(lambda x: x in ["auto", "Auto", "AUTO"], lista_tipo)))
        camionetas = len(list(filter(lambda x: x in ["camioneta", "Camioneta", "CAMIONETA"], lista_tipo)))

        print("Cantidad de motos:", motos)
        print("Cantidad de autos:", autos)
        print("Cantidad de camionetas:", camionetas)

def reporte_ocupacion_estacionamiento(lista_tipo):
    """
    Muestra un reporte de la ocupación de estacionamientos por tipo de vehículo, utilizando filter para contar los tipos de vehículos.
    Si el vehículo es una camioneta, ocupa un espacio grande; si es un auto o moto, ocupa un espacio estándar.
    """
    print("\nLOGÍSTICA DE ESPACIOS OCUPADOS:")
    if len(lista_tipo) == 0:
        return
    else:
        espacios_grandes = len(list(filter(lambda x: x in ["camioneta", "Camioneta", "CAMIONETA"], lista_tipo)))
        espacios_estandar = len(list(filter(lambda x: x in ["auto", "Auto", "AUTO", "moto", "Moto", "MOTO"], lista_tipo)))

        print("Cantidad de espacios grandes ocupados (camionetas):", espacios_grandes)
        print("Cantidad de espacios estándar ocupados (autos y motos):", espacios_estandar)

def reporte_reservas(reservar, reservas_canceladas):
    if len(reservar) > 1:
        print("\n REPORTE DE RESERVAS REALIZADAS \n")
        print(f'{"Índice":<8} | {"Nombre":<15} | {"Día":<5} | {"Mes":<5} | {"Año":<6} | {"Hora":<6} | {"Minuto":<8} | {"Duración":<10} | {"Estacionamiento":<15}')
        print("-" * 110)
            
        for i in range(1, len(reservar)):
            # Buscamos el nombre real del estacionamiento usando el índice guardado
            nombre_est = estacionamientos[reservar[i]["estacionamiento"]]["nombre"]
            
            print(f'{i:<8} | '
                  f'{reservar[i]["nombre"]:<15} | '
                  f'{escritura_digitos(reservar[i]["dia"]):<5} | '
                  f'{escritura_digitos(reservar[i]["mes"]):<5} | '
                  f'{reservar[i]["año"]:<6} | '
                  f'{escritura_digitos(reservar[i]["hora"]):<6} | '
                  f'{escritura_digitos(reservar[i]["minuto"]):<8} | '
                  f'{escritura_digitos(reservar[i]["duracion"]):<10} | '
                  f'{nombre_est:<15}')

        print(f"\nCantidad de reservas realizadas: {len(reservar) - 1}")
    else:
        print("\nNo se realizaron reservas.")

    if len(reservas_canceladas) > 1:
        print("\n REPORTE DE RESERVAS CANCELADAS \n")
        print(f'{"Índice":<8} | {"Nombre":<15} | {"Día":<5} | {"Mes":<5} | {"Año":<6} | {"Hora":<6} | {"Minuto":<8} | {"Duración":<10} | {"Estacionamiento":<15}')
        print("-" * 110)
                
        for i in range(1, len(reservas_canceladas)):
            # Buscamos el nombre real del estacionamiento usando el índice guardado
            nombre_est_canc = estacionamientos[reservas_canceladas[i]["estacionamiento"]]["nombre"]
            
            print(f'{i:<8} | '
                  f'{reservas_canceladas[i]["nombre"]:<15} | '
                  f'{escritura_digitos(reservas_canceladas[i]["dia"]):<5} | '
                  f'{escritura_digitos(reservas_canceladas[i]["mes"]):<5} | '
                  f'{reservas_canceladas[i]["año"]:<6} | '
                  f'{escritura_digitos(reservas_canceladas[i]["hora"]):<6} | '
                  f'{escritura_digitos(reservas_canceladas[i]["minuto"]):<8} | '
                  f'{escritura_digitos(reservas_canceladas[i]["duracion"]):<10} | '
                  f'{nombre_est_canc:<15}')

        print(f"\nCantidad de reservas canceladas: {len(reservas_canceladas) - 1}")
    else:
        print("\nNo se canceló ninguna reserva.")

    # Pausa para que el usuario llegue a leer el reporte antes de que el programa siga
    input("\nPresione ENTER para volver...")
    
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