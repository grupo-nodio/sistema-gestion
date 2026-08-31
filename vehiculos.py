from usuarios import * 

# FUNCIONES MENU

def menu_vehiculos():
    print("Menú de Vehículos:")
    print("1. Ingresar vehículo")
    print("2. Mostrar vehículos")
    print("3. Eliminar vehículo")
    print("4. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    return opcion

def opcion_vehiculos(opcion, lista_patente, lista_tipo, lista_dnivehiculo, lista_dni_usuarios):
    if opcion == "1":
        ingresar_vehiculo(lista_patente, lista_tipo, lista_dnivehiculo, lista_dni_usuarios)
    elif opcion == "2":
        mostrar_vehiculos(lista_patente, lista_tipo, lista_dnivehiculo)
    elif opcion == "3":
        eliminar_vehiculo(lista_patente, lista_tipo, lista_dnivehiculo)
    elif opcion == "4":
        print("Volviendo al menú principal...")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

# FUNCIONES PRINCIPALES

def ingresar_vehiculo(lista_patente, lista_tipo, lista_dnivehiculo, lista_dni_usuarios):
    print("Ingresar datos del vehículo:")
    patente = input("Patente: ")
    while patente in lista_patente:
        print("La patente ya existe. Ingrese una patente diferente.")
        patente = input("Ingrese la patente nuevamente por favor: ")

    tipo = input("Tipo de vehículo: ")

    dni_usuario = input("DNI del usuario propietario: ")
    while dni_usuario not in lista_dni_usuarios:
        print("El DNI ingresado no corresponde a ningún usuario registrado.")
        dni_usuario = input("Ingrese el DNI del usuario propietario: ")

    lista_patente.append(patente) 
    lista_tipo.append(tipo)
    lista_dnivehiculo.append(dni_usuario)

    print("Vehículo ingresado correctamente.")

def mostrar_vehiculos(lista_patente, lista_tipo, lista_dnivehiculo):
    if not lista_patente:
        print("No hay vehículos registrados.") 
        return
    print("Vehículos registrados:")
    for i in range(len(lista_patente)):
        print("Patente:", lista_patente[i])
        print("Tipo:", lista_tipo[i])
        print("DNI propietario:", lista_dnivehiculo[i])

def eliminar_vehiculo(lista_patente, lista_tipo, lista_dnivehiculo):
    patente = input("Ingrese la patente del vehículo a eliminar: ")

    for pos in range(len(lista_patente)):
        if lista_patente[pos] == patente:
            del lista_patente[pos]
            del lista_tipo[pos]
            del lista_dnivehiculo[pos]
            print("Vehículo eliminado correctamente.")
            return
            
    print("La patente ingresada no corresponde a ningún vehículo registrado.")

# PROGRAMA PRINCIPAL
patentes = []
tipos = []
dni_vehiculos = []

opcion = ""
while opcion != "4":
    opcion = menu_vehiculos()
    opcion_vehiculos(opcion, patentes, tipos, dni_vehiculos, dni)




