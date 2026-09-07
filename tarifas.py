# Lambada que calcula el costo con los datos de duración obtenidos de reservas.py y la tarifa según el tipo de vehículo.
calcular = lambda horas, tarifa: horas * tarifa

def calcular_costo(duracion, tipo_vehiculo):
    if tipo_vehiculo == "moto":
        return calcular(duracion, 2500)
    elif tipo_vehiculo == "auto":
        return calcular(duracion, 4000)
    elif tipo_vehiculo == "camioneta":
        return calcular(duracion, 6000)

lista_cobros = []
lista_patente_cobrada = []


def cobrar_estacionamiento(duracion, lista_patente, lista_tipo):

    """Objetivo: Cobrar el estacionamiento de un vehículo según su tipo y duración de la reserva.
    Parámetros: duracion de la reserva en horas, y las listas de vehículos.
    Salida: Muestra el resumen de la cuenta y guarda el cobro en las listas."""

    print("\n--- COBRO DE ESTACIONAMIENTO ---")
    
    # Si no hay vehículos registrados, se cancela el cobro y se vuelve al menú.
    if len(lista_patente) == 0:
        print("No hay vehículos registrados en el sistema para cobrar.")
        return None

    print("Escriba '0' si desea cancelar y volver al menú.")
    patente_cobro = input("Ingrese la patente del vehiculo a cobrar: ")
    
    # Si la persona escribe 0, se cancela todo y vuelve al menú
    if patente_cobro == "0":
        print("Cobro cancelado. Volviendo al menú.")
        return None
    
    while patente_cobro not in lista_patente:
        print("Error: Esa patente no se encuentra registrada.")
        patente_cobro = input("Ingrese una patente válida (o '0' para cancelar): ")
        
        if patente_cobro == "0":
            print("Cobro cancelado. Volviendo al menú.")
            return None

    # Buscamos la posicion de la patente en la lista para obtener el tipo de vehículo.
    posicion = 0
    for i in range(len(lista_patente)):
        if lista_patente[i] == patente_cobro:
            posicion = i

    tipo_vehiculo = lista_tipo[posicion]
    
    print("Vehículo encontrado:", tipo_vehiculo, "con patente", patente_cobro)

    costo = calcular_costo(duracion, tipo_vehiculo)
    total_pagar = costo


    # Guardamos el cobro correspondiente a su patente.
    lista_cobros.append(total_pagar)
    lista_patente_cobrada.append(patente_cobro)

    print("\n------------- RESUMEN DE CUENTA -------------")
    print("Vehículo cobrado:", tipo_vehiculo, "Patente:", patente_cobro)
    print("Costo base de la reserva (", duracion, "hs): $", costo)
    print("TOTAL A PAGAR: $", total_pagar)