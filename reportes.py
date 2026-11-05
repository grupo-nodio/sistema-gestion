from functools import reduce
import json
from reservas import escritura_digitos
import estacionamiento
import tarifas

def mostrar_reportes(estacionamientos, lista_tipo, usuarios, reservar, reservas_canceladas, lista_cobros):
    '''Llama a todas las estadísticas generales por pantalla'''
    reporte_estacionamiento(estacionamientos)
    reporte_vehiculos_por_tipo(lista_tipo)
    reporte_ocupacion_estacionamiento(lista_tipo)
    reporte_usuarios_por_estado(usuarios)
    reporte_reservas(reservar, reservas_canceladas)
    reporte_recaudacion(lista_cobros)

def reporte_estacionamiento(estacionamientos):
    '''Muestra en pantalla estacionamientos registrados, disponibles, no disponibles y capacidad actual disponible total'''
    activos = list(filter(lambda est: est["nombre"] != "ELIMINADO", estacionamientos.values()))
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
    estacionamientos_disponibles = filter(
        lambda est: est["nombre"] != "ELIMINADO" and est["estado"] == 1,
        estacionamientos.values()
    )
    return reduce(
        lambda acumulador, est: acumulador + est["capacidad_actual"],
        estacionamientos_disponibles,
        0
    )

def reporte_vehiculos_por_tipo(lista_tipo):
    """Muestra un reporte de la cantidad de vehículos registrados por tipo."""
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
    """Muestra un reporte de la ocupación de espacios por tipo de vehículo."""
    print("\nLOGÍSTICA DE ESPACIOS OCUPADOS:")
    if len(lista_tipo) == 0:
        return
    else:
        espacios_grandes = len(list(filter(lambda x: x in ["camioneta", "Camioneta", "CAMIONETA"], lista_tipo)))
        espacios_estandar = len(list(filter(lambda x: x in ["auto", "Auto", "AUTO", "moto", "Moto", "MOTO"], lista_tipo)))

        print("Cantidad de espacios grandes ocupados (camionetas):", espacios_grandes)
        print("Cantidad de espacios estándar ocupados (autos y motos):", espacios_estandar)

def reporte_reservas(RESER_JSON, reservas_canceladas):
    if len(RESER_JSON) > 1:
        print("\n REPORTE DE RESERVAS REALIZADAS \n")
        print(f'{"Índice":<8} | {"Nombre":<15} | {"Día":<5} | {"Mes":<5} | {"Año":<6} | {"Hora":<6} | {"Minuto":<8} | {"Duración":<10}')
        print("-" * 110)
            
        for i in range(1, len(RESER_JSON)):
            print(f'{i:<8} | '
                  f'{RESER_JSON[i]["nombre"]:<15} | '
                  f'{escritura_digitos(RESER_JSON[i]["dia"]):<5} | '
                  f'{escritura_digitos(RESER_JSON[i]["mes"]):<5} | '
                  f'{RESER_JSON[i]["año"]:<6} | '
                  f'{escritura_digitos(RESER_JSON[i]["hora"]):<6} | '
                  f'{escritura_digitos(RESER_JSON[i]["minuto"]):<8} | '
                  f'{escritura_digitos(RESER_JSON[i]["duracion"]):<10} | ')

        print(f"\nCantidad de reservas realizadas: {len(RESER_JSON) - 1}")
    else:
        print("\nNo se realizaron reservas.")

    if len(reservas_canceladas) > 1:
        print("\n REPORTE DE RESERVAS CANCELADAS \n")
        print(f'{"Índice":<8} | {"Nombre":<15} | {"Día":<5} | {"Mes":<5} | {"Año":<6} | {"Hora":<6} | {"Minuto":<8} | {"Duración":<10}')
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
        total_dinero = reduce(lambda acumulador, cobro: acumulador + cobro["total"], lista_cobros, 0)
            
        print("\nREPORTE DE RECAUDACIÓN:")
        print("Cantidad de cobros realizados:", len(lista_cobros))
        print("Total de dinero recaudado:", tarifas.formatear_pesos(total_dinero))

def escribir_ficha_estacionamiento(archivo, sel, estacionamientos):
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

    archivo.write("=" * 45 + "\n\n")

def imprimir_datos_estacionamiento(estacionamientos):
    '''Genera un archivo de texto con los datos de uno o todos los estacionamientos activos.'''
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

    if opcion == "2":
        modo = "w"
    else:
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

    if opcion == "1":
        seleccion = estacionamiento.elegir_estacionamiento(estacionamientos)
        lista_ids = [seleccion]
    else:
        lista_ids = list(activos.keys())

    with open(nombre_archivo, modo, encoding="utf-8") as archivo:
        for id_est in lista_ids:
            escribir_ficha_estacionamiento(archivo, id_est, estacionamientos)

    print(f"Archivo '{nombre_archivo}' generado correctamente.")

def imprimir_usuarios(usuarios, vehiculos):
    '''Genera un archivo de texto con los usuarios registrados y sus vehículos asociados.'''
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

    try:
        with open(vehiculos, "r", encoding="utf-8") as archivo_vehiculos:
            lista_vehiculos = json.load(archivo_vehiculos)
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        lista_vehiculos = []

    ancho = 72
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("=" * ancho + "\n")
        titulo = "PARK DIRECT | REPORTE DE USUARIOS Y VEHÍCULOS"
        espacios = (ancho - len(titulo)) // 2
        archivo.write(" " * espacios + titulo + "\n")
        archivo.write("=" * ancho + "\n")
        archivo.write(f"Usuarios registrados: {len(usuarios)}    |    Vehículos registrados: {len(lista_vehiculos)}\n\n")

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
                vehiculos_usuario = [v for v in lista_vehiculos if v["dni"] == dni]
                archivo.write("Vehículos:\n")
                if vehiculos_usuario:
                    for vehiculo in vehiculos_usuario:
                        archivo.write(f"  • {vehiculo['patente']} — {vehiculo['tipo']}\n")
                else:
                    archivo.write("  Sin vehículos registrados.\n")
            archivo.write("\n" + "=" * ancho + "\n")

    print(f"Archivo '{nombre_archivo}' creado correctamente.")

def reporte_tarifas_archivo(archivo, sel, estacionamientos):
    """Escribe el historial de cobros y recaudación de un estacionamiento en el archivo txt."""
    archivo.write("\n--- HISTORIAL DE COBROS Y TARIFAS ---\n")
    
    cobros_totales = tarifas.cargar_cobros()
    cobros_estacionamiento = list(filter(
        lambda cobro: cobro["estacionamiento"] == estacionamientos[sel]["nombre"], 
        cobros_totales
    ))
    
    if len(cobros_estacionamiento) == 0:
        archivo.write("No hay cobros registrados en este estacionamiento.\n")
    else:
        recaudacion = reduce(lambda acumulador, cobro: acumulador + cobro["total"], cobros_estacionamiento, 0)
        
        archivo.write(f"Cantidad de cobros: {len(cobros_estacionamiento)}\n")
        archivo.write(f"Recaudación total: {tarifas.formatear_pesos(recaudacion)}\n\n")
        
        archivo.write(f"{'N°':<7}{'Patente':<10}{'Tipo':<11}{'Horas':>6}{'Total':>13}\n")
        archivo.write("-" * 50 + "\n")
        for cobro in cobros_estacionamiento:
            numero = f"{cobro['numero']:04d}"
            total = tarifas.formatear_pesos(cobro["total"])
            archivo.write(f"{numero:<7}{cobro['patente']:<10}{cobro['tipo']:<11}{cobro['horas']:>6}{total:>13}\n")
