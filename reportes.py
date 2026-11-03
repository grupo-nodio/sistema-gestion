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
    """ Muestra únicamente las reservas realizadas y canceladas. """
    print("\n REPORTE DE RESERVAS REALIZADAS \n")

    for i in range(len(reservar)):
        print(f"{i + 1}. Nombre: {reservar[i][0]} / dia: {escritura_digitos(reservar[i][1])} / mes: {escritura_digitos(reservar[i][2])} / año: {escritura_digitos(reservar[i][3])} / hora: {escritura_digitos(reservar[i][4])} / minuto: {escritura_digitos(reservar[i][5])} / duracion: {escritura_digitos(reservar[i][6])}hs / estacionamiento: {escritura_digitos(reservar[i][7])}.")

    print(f"Cantidad de reservas realizadas con éxito: {len(reservar)}")

    print("\n REPORTE DE RESERVAS CANCELADAS \n")

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

def escribir_ficha_estacionamiento(archivo, sel, estacionamientos, reservas, tarifas):
    '''Escribe el bloque de datos de un estacionamiento específico dentro del archivo abierto.'''
    dias = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo')

    archivo.write("=" * 45 + "\n")
    archivo.write("       INFORMACIÓN DEL ESTACIONAMIENTO\n")
    archivo.write("=" * 45 + "\n")
    archivo.write(f"ID: {sel}\n")
    archivo.write(f"Nombre: {estacionamientos[sel]['nombre']}\n")
    archivo.write(f"Dirección: {estacionamientos[sel]['direccion']}\n")
    archivo.write(f"Estado: {estacionamiento.ver_estado(sel, estacionamientos)}\n")
    archivo.write(f"Capacidad Total: {estacionamientos[sel]['capacidad_total']}\n")
    archivo.write(f"Capacidad Disponible: {estacionamientos[sel]['capacidad_actual']}\n")
    
    archivo.write("\nHorarios:\n")
    for dia in range(len(dias)):
        horario_texto = estacionamiento.mostrar_horario(estacionamientos[sel]['horarios'][dia])
        archivo.write(f"  - {dias[dia]}: {horario_texto}\n")

    # =========================================================================
    # ESCRIBIR ACÁ ABAJO LOS DATOS DE RESERVAS Y TARIFAS (COMPAÑEROS)
    # =========================================================================

    archivo.write("=" * 45 + "\n\n")


def imprimir_datos_estacionamiento(estacionamientos, reservas, tarifas):
    '''Genera un archivo de texto con los datos de uno o todos los estacionamientos activos.'''
    
    # Filtrar estacionamientos activos (excluir los eliminados)
    activos = {k: v for k, v in estacionamientos.items() if v["nombre"] != "ELIMINADO"}
    
    if not activos:
        print("Error: No hay estacionamientos activos para reportar.")
        return

    print("\n--- EXPORTAR REPORTE A TEXTO ---")
    print("1. Reportar un estacionamiento en particular")
    print("2. Reportar TODOS los estacionamientos")
    
    opcion = input("Seleccione una opción (1 u 2): ").strip()
    
    while opcion not in ("1", "2"):
        opcion = input("Error, opción inválida. Ingrese 1 o 2: ").strip()

    nombre_archivo = input("Ingrese el nombre del archivo: ").strip()

    if not nombre_archivo.endswith(".txt"):
        nombre_archivo += ".txt"

    # Determinar el modo de apertura ("w" para sobreescribir, "a" para anexar)
    if opcion == "2":
        # Si elige TODOS, se sobreescribe directamente sin usar append
        modo = "w"
    else:
        # Si elige UNO SOLO, se valida si el archivo ya existe
        try:
            with open(nombre_archivo, "r", encoding="utf-8"):
                print("El archivo ya existe.")
                print("1. Sobrescribir")
                print("2. Agregar datos al final (Append)")
                print("3. Cancelar")
                confirmacion = input("Seleccione una opción: ").strip()

                if confirmacion not in ("1", "2"):
                    print("Operación cancelada.")
                    return
                
                opciones_modo = ("w", "a")
                modo = opciones_modo[int(confirmacion) - 1]

        except FileNotFoundError:
            modo = "w"

    # Definir la lista de IDs a procesar
    if opcion == "1":
        seleccion = estacionamiento.elegir_estacionamiento(estacionamientos)
        lista_ids = [seleccion]
    else:
        lista_ids = list(activos.keys())

    # Escritura en el archivo
    with open(nombre_archivo, modo, encoding="utf-8") as archivo:
        for id_est in lista_ids:
            escribir_ficha_estacionamiento(archivo, id_est, estacionamientos, reservas, tarifas)

    print(f"Archivo '{nombre_archivo}' generado correctamente.")

    
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
