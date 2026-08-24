import usuarios 
#FUNCIONES

#Funcion para ingresar un vehiculo
def ingresar_vehiculo(lista_patente, lista_tipo, lista_dnivehiculo, listadniusuario):
    print("Ingresar datos del vehículo:")
    patente = input("Patente: ")
    while patente in lista_patente: #operador IN para chequear que la patente no se repita, en caso de que se repita, se le pide al usuario que ingrese una nueva patente
        print("La patente ya existe. Ingrese una patente diferente.")
        patente = input("Ingrese la patente nuevamente porfavor ")

    tipo = input("Tipo de vehículo: ") #tipo de vehiculo puede ser auto, camioneta, moto, etc. Se deja a criterio del usuario ingresar el tipo de vehiculo que desee.

    dni_usuario = input("DNI del usuario propietario: ")
    while dni_usuario not in listadniusuario: #operador IN para chequear que el dni ingresado corresponda a un usuario registrado
        print("El DNI ingresado no corresponde a ningún usuario registrado.")
        dni_usuario = input("Ingrese el DNI del usuario propietario: ")

    #ingresa los datos del vehiculo a las listas correspondientes y el dni
    lista_patente.append(patente) 
    lista_tipo.append(tipo)
    lista_dnivehiculo.append(dni_usuario)

    print("Vehículo ingresado correctamente.")

#funcion para mostrar los vehiculos registrados
def mostrar_vehiculos(lista_patente, lista_tipo, lista_dnivehiculo):
    if not lista_patente:
        print("No hay vehículos registrados.") 
        return
    print("Vehículos registrados:")
    for i in range(len(lista_patente)):
        print("patente:", lista_patente[i])
        print("tipo:", lista_tipo[i])
        print("DNI propietario:", lista_dnivehiculo[i])
