from vehiculos import lista_patente, lista_tipo
from reservas import duracion


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



def cobrar_estacionamiento(duracion):

    """Objetivo: Cobrar el estacionamiento de un vehículo según su tipo y duración de la reserva.
    Parámetros: duracion de la reserva en horas.
    Salida: Muestra el resumen de la cuenta y guarda el cobro en las listas."""

    print("\n--- COBRO DE ESTACIONAMIENTO ---")
    
    patente_cobro = input("Ingrese la patente del vehiculo a cobrar: ")
    
    while patente_cobro not in lista_patente:
        print("Error: Esa patente no se encuentra registrada.")
        patente_cobro = input("Ingrese una patente válida: ")


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

