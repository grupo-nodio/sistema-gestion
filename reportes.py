from functools import reduce
from reservas import escritura_digitos
import estacionamiento

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
    # Se obtienen únicamente los estacionamientos activos (excluyendo los marcados como "ELIMINADO")
    activos = list(filter(lambda est: est["nombre"] != "ELIMINADO", estacionamientos.values()))
    
    # Se filtran los estacionamientos cuyo estado es 1 (disponible)
    disponibles = list(filter(lambda est: est["estado"] == 1, activos))
    
    cant_registrados = len(activos)
    cant_disponibles = len(disponibles)
    cant_no_disponibles = cant_registrados - cant_disponibles
    
    print("\nESTADÍSTICAS DE ESTACIONAMIENTOS:")
    print("Estacionamientos registrados:", cant_registrados)
    print("Estacionamientos disponibles:", cant_disponibles)
    print("Estacionamientos no disponibles:", cant_no_disponibles)
    print("Capacidad actual disponible (todos los estacionamientos):", capacidad_actual_disponible(estacionamientos))

def capacidad_actual_disponible(estacionamientos):
    '''Muestra la capacidad actual sin reservar en total entre todos los estacionamientos que se encuentren disponibles.'''
    # Filtrar estacionamientos que estén activos y disponibles (estado == 1)
    estacionamientos_disponibles = filter(
        lambda est: est["nombre"] != "ELIMINADO" and est["estado"] == 1,
        estacionamientos.values()
    )
    
    # Sumar la capacidad_actual de los estacionamientos filtrados
    return reduce(
        lambda acumulador, est: acumulador + est["capacidad_actual"],
        estacionamientos_disponibles,
        0
    )

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
            
            print(f'{i:<8} | '
                  f'{reservar[i]["nombre"]:<15} | '
                  f'{escritura_digitos(reservar[i]["dia"]):<5} | '
                  f'{escritura_digitos(reservar[i]["mes"]):<5} | '
                  f'{reservar[i]["año"]:<6} | '
                  f'{escritura_digitos(reservar[i]["hora"]):<6} | '
                  f'{escritura_digitos(reservar[i]["minuto"]):<8} | '
                  f'{escritura_digitos(reservar[i]["duracion"]):<10} | ')

        print(f"\nCantidad de reservas realizadas: {len(reservar) - 1}")
    else:
        print("\nNo se realizaron reservas.")

    if len(reservas_canceladas) > 1:
        print("\n REPORTE DE RESERVAS CANCELADAS \n")
        print(f'{"Índice":<8} | {"Nombre":<15} | {"Día":<5} | {"Mes":<5} | {"Año":<6} | {"Hora":<6} | {"Minuto":<8} | {"Duración":<10} | {"Estacionamiento":<15}')
        print("-" * 110)
                
        for i in range(1, len(reservas_canceladas)):
            
            print(f'{i:<8} | '
                  f'{reservas_canceladas[i]["nombre"]:<15} | '
                  f'{escritura_digitos(reservas_canceladas[i]["dia"]):<5} | '
                  f'{escritura_digitos(reservas_canceladas[i]["mes"]):<5} | '
                  f'{reservas_canceladas[i]["año"]:<6} | '
                  f'{escritura_digitos(reservas_canceladas[i]["hora"]):<6} | '
                  f'{escritura_digitos(reservas_canceladas[i]["minuto"]):<8} | '
                  f'{escritura_digitos(reservas_canceladas[i]["duracion"]):<10} | ')

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

def imprimir_datos_estacionamiento(estacionamientos, reservas, tarifas):
    '''Genera un archivo de texto con los datos de un estacionamiento seleccionado'''
    nombre_archivo = input("Ingrese el nombre del archivo: ").strip()

    if not nombre_archivo.endswith(".txt"):
        nombre_archivo += ".txt"

    try:
        with open(nombre_archivo, "r", encoding="utf-8"):
            confirmacion = input("El archivo ya existe. Presione 1 para sobrescribirlo, 2 para agregar los datos al final, 3 para cancelar: ").lower()

            if confirmacion not in ("1", "2"):
                print("Operación cancelada.")
                return
            else:
                eleccion = ("w", "a")

                confirmacion = eleccion[int(confirmacion) - 1]

    except FileNotFoundError:
        confirmacion = "w"

    with open(nombre_archivo, confirmacion, encoding="utf-8") as archivo:
        archivo.write("=" * 45 + "\n")
        archivo.write("       INFORMACIÓN DEL ESTACIONAMIENTO\n")
        archivo.write("=" * 45 + "\n\n")

        seleccion = estacionamiento.elegir_estacionamiento(estacionamientos)

        dias = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')

        archivo.write(f"Nombre: {estacionamientos[seleccion]['nombre']}")
        archivo.write(f"Nombre: {estacionamientos[seleccion]['direccion']}")
        archivo.write(f"Estado: {estacionamiento.ver_estado}")
        archivo.write(f"Capacidad ocupada: {estacionamientos[seleccion]['capacidad_total']}/{estacionamientos[seleccion]['capacidad_actual']}")
        
        archivo.write(f"\nHorarios:")
        
        for dia in range(len(dias)):
            archivo.write(f"{dias[dia]}: {estacionamiento.mostrar_horario(estacionamientos[seleccion]['horarios'][dia])}")

        # PONER ACA ABAJO ESCRITURA DE DATOS DE RESERVA Y TARIFAS

        archivo.write("\n" + "=" * 45 + "\n")

    print(f"Archivo '{nombre_archivo}' creado correctamente.")

''' VERLO
def imprimir_estacionamientos(estacionamientos, reservas, tarifas):
    nombre_archivo = input("Ingrese el nombre del archivo: ").strip()

    if not nombre_archivo.endswith(".txt"):
        nombre_archivo += ".txt"

    try:
        with open(nombre_archivo, "r", encoding="utf-8"):
            confirmacion = input("El archivo ya existe. ¿Desea sobrescribirlo? (S/N): ").lower()

            if confirmacion != "s":
                print("Operación cancelada.")
                return

    except FileNotFoundError:
        pass

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("=" * 45 + "\n")
        archivo.write("       INFORMACIÓN DEL ESTACIONAMIENTO\n")
        archivo.write("=" * 45 + "\n\n")

        #funciona igual que la funcion de imprimir un estacionamiento, pero impime a todos.

        archivo.write("\n" + "=" * 45 + "\n")

    print(f"Archivo '{nombre_archivo}' creado correctamente.")
'''

    
def imprimir_usuarios(usuarios, vehiculos):
    nombre_archivo = input("Ingrese el nombre del archivo: ").strip()

    if not nombre_archivo.endswith(".txt"):
        nombre_archivo += ".txt"

    try:
        with open(nombre_archivo, "r", encoding="utf-8"):
            confirmacion = input("El archivo ya existe. ¿Desea sobrescribirlo? (S/N): ").lower()

            if confirmacion != "s":
                print("Operación cancelada.")
                return

    except FileNotFoundError:
        pass

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("=" * 45 + "\n")
        archivo.write("       BASE DE DATOS USUARIOS Y VEHÍCULOS\n")
        archivo.write("=" * 45 + "\n\n")

        '''
        se debe mostrar la base de datos combinando la informacion de usuarios + vehiculos, el usuario tiene el vehiculo asignado
        '''

        archivo.write("\n" + "=" * 45 + "\n")

    print(f"Archivo '{nombre_archivo}' creado correctamente.")
