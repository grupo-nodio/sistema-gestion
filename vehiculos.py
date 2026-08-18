import usuarios  # Módulo con la lista de clientes (usuarios.dni)

# Lista para almacenar los vehículos registrados en memoria
vehiculos = []


# FUNCIONES

def clientesregistrados():
    numero = int(input("Ingrese su número de cliente/dni: "))
    
    # Verificamos si el DNI está en la lista del módulo usuarios
    if numero in usuarios.dni:
        print("Cliente registrado.")
    else:
        print("Cliente no encontrado en el sistema.")


def registrarvehiculo():
    print("\n--- REGISTRO DE VEHÍCULO ---")
    numero = int(input("Ingrese el DNI del cliente asociado: "))

    # Corrección: Cambiamos usuarios.lista_dnis por usuarios.dni
    if numero not in usuarios.dni:
        print("Error: El cliente no existe. Debe registrarlo primero.")
        return

    # Datos del vehículo
    tipo = input("Ingrese el tipo de vehículo (auto, moto, camión): ").strip().lower()
    patente = input("Patente: ").strip().upper()

    # Guardamos el vehículo
    vehiculos.append([patente, tipo, numero])
    print(f"Vehículo {patente} registrado con éxito para el cliente {numero}.")


# MENÚ PRINCIPAL 
print("Bienvenido al sistema de registro de vehículos.")
print("1. Registrar vehículo")
print("2. Ver si un cliente está registrado")
opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    registrarvehiculo()
elif opcion == 2:
    clientesregistrados()
else:
    print("Opción no válida.")