import usuarios 
#FUNCIONES

#Funcion para ingresar un vehiculo
def ingresar_vehiculo(lista_patente, lista_tipo, lista_dnivehiculo, listadniusuario):
    print("Ingresar datos del vehículo:")
    patente = input("Patente: ")
    while patente in lista_patente:
        print("La patente ya existe. Ingrese una patente diferente.")
        patente = input("Ingrese la patente nuevamente porfavor ")

    tipo = input("Tipo de vehículo (auto, moto, camioneta): ")

    dni_usuario = input("DNI del usuario propietario: ")
    while dni_usuario not in listadniusuario:
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
        print("patente:", lista_patente[i], "| tipo:", lista_tipo[i], "| DNI propietario:", lista_dnivehiculo[i])
