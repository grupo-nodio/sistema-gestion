from functools import reduce
import json
from reservas import escritura_digitos
import estacionamiento

def mostrar_reportes(estacionamientos, lista_tipo, usuarios, reservar, reservas_canceladas, lista_cobros):
    '''Llama a todas las estadísticas'''
    reporte_estacionamiento(estacionamientos)
    reporte_vehiculos_por_tipo(lista_tipo)
    reporte_ocupacion_estacionamiento(lista_tipo)
    reporte_usuarios_por_estado(usuarios)
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
    
def reporte_usuarios_por_estado(usuarios):
    """ Reporte de usuarios dados de alta y dados de baja. """
    total_usuarios = len(usuarios)

    if total_usuarios == 0:
        print("\nUSUARIOS REGISTRADOS:")
        print("Usuarios dados de alta: 0")
        print("Usuarios dados de baja: 0")
        return

    usuarios_activos = 0
    usuarios_baja = 0

    for datos in usuarios.values():
        if datos["estado"] == "A":
            usuarios_activos += 1
        elif datos["estado"] == "B":
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

    if isinstance(vehiculos, str):
        try:
            with open(vehiculos, "r", encoding="utf-8") as archivo_vehiculos:
                vehiculos = json.load(archivo_vehiculos)
        except FileNotFoundError:
            vehiculos = []
        except (OSError, json.JSONDecodeError):
            print("No se pudo leer el archivo de vehículos.")
            return

    ancho = 72
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("=" * ancho + "\n")
        titulo = "PARK DIRECT | REPORTE DE USUARIOS Y VEHÍCULOS"
        espacios = (ancho - len(titulo)) // 2
        archivo.write(" " * espacios + titulo + "\n")
        archivo.write("=" * ancho + "\n")
        archivo.write(f"Usuarios registrados: {len(usuarios)}    |    Vehículos registrados: {len(vehiculos)}\n\n")

        if not usuarios:
            archivo.write("No hay usuarios registrados.\n")
        else:
            for dni, datos in usuarios.items():
                estado = "Activo" if datos["estado"] == "A" else "Dado de baja" if datos["estado"] == "B" else "Desconocido"
                archivo.write("-" * ancho + "\n")
                archivo.write(f"Nombre: {datos['nombre']}    Apellido: {datos['apellido']}\n")
                archivo.write(f"DNI: {dni}    |    Estado: {estado}\n")
                archivo.write(f"Email: {datos['email']}\n")
                archivo.write(f"Teléfono: {datos['telefono']}\n")
                vehiculos_usuario = [v for v in vehiculos if v["dni"] == dni]
                archivo.write("Vehículos:\n")
                if vehiculos_usuario:
                    for vehiculo in vehiculos_usuario:
                        archivo.write(f"  • {vehiculo['patente']} — {vehiculo['tipo']}\n")
                else:
                    archivo.write("  Sin vehículos registrados.\n")
            archivo.write("\n" + "=" * ancho + "\n")

    print(f"Archivo '{nombre_archivo}' creado correctamente.")
