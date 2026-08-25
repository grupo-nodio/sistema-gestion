def escritura_digitos(A):
    if A < 10:
        A = "0" + str(A)

    else:
        A = str(A)

    return A

def validar_fecha(dia, mes, año):
    if año < 2026:
        año = 0
        return False, dia, mes, año

    if mes < 1 or mes > 12:
        mes = 0
        return False, dia, mes, año

    if dia < 1 or dia > 31:
        dia = 0
        return False, dia, mes, año

    if mes in [4, 6, 9, 11] and dia > 30:
        dia = 0
        return False, dia, mes, año

    if mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            if dia > 29:
                dia = 0
                return False, dia, mes, año

        else:
            if dia > 28:
                dia = 0
                return False, dia, mes, año

    return True, dia, mes, año

def validar_hora(hora, minuto):
    if hora < 0 or hora > 23:
        hora = 0
        return False, hora, minuto
    if minuto < 0 or minuto > 59:
        minuto = 0
        return False, hora, minuto

    return True, hora, minuto

def modificar_datos(A):
    A = input("Ingrese el nuevo dato, el cual sera modificado en su reserva: ")

    return A

def generar_reserva():
    nombre = input("Ingrese el nombre para comenzar la reserva: ")

    dia = int(input("Ingrese el dia que desea hacer la reserva: "))
    mes = int(input("Ingrese el mes que desea hacer la reserva: "))
    año = int(input("Ingrese el año que desea hacer la reserva: "))
    validacion_fecha, dia, mes, año = validar_fecha(dia, mes, año)

    while validacion_fecha != True:
        if validacion_fecha != True:
            if dia == 0:
                print("La fecha ingresada no es valida, por favor, modifique el dia.")
                dia = int(input("Ingrese el dia que desea hacer la reserva: "))
            elif mes == 0:
                print("La fecha ingresada no es valida, por favor, modifique el mes.")
                mes = int(input("Ingrese el mes que desea hacer la reserva: "))
            elif año == 0:
                print("La fecha ingresada no es valida, por favor, modifique el año.")
                año = int(input("Ingrese el año que desea hacer la reserva: "))
            validacion_fecha, dia, mes, año = validar_fecha(dia, mes, año)

    hora = int(input("Ingrese la hora de la reserva, (formato de 24 horas): "))
    minuto = int(input("Ingrese el minuto de la reserva: "))
    duracion = int(input("Ingrese cuanto tiempo durara la reserva: "))
    validacion_horario, hora, minuto = validar_hora(hora, minuto)

    while validacion_horario != True:
        if validacion_horario != True:
            if hora == 0:
                print("La hora ingresada es invalida, por favor, modifique la hora.")
                hora = int(input("Ingrese la hora de la reserva, (formato de 24 horas): "))
            elif minuto == 0:
                print("El o los minuto/s ingresado es invalido, por favor, modifique los minutos.")
                minuto = int(input("Ingrese el minuto de la reserva: "))
            validacion_horario, hora, minuto = validar_hora(hora, minuto)

    dia = escritura_digitos(dia)
    mes = escritura_digitos(mes)
    hora = escritura_digitos(hora)
    minuto = escritura_digitos(minuto)
    print("\n -------------CONTROL DE RESERVA------------- \n")
    print("La reserva se genero bajo el nombre de: " + str(nombre))
    print("En la fecha DD - MM - YYYY: ",dia ,"-",mes ,"-",año)
    print("la reserva comenzara a las: ",hora ,":",minuto, ", y durara: ", duracion,"hs")

    control = input("\nVerifique si los datos tomados son los correctos [Y / N]: ")

    if control not in ["Y", "y", "yes", "Yes", "si", "Si"]:
        cambio = int(input(f"¿Cual de los siguientes datos desea modificar?, [1. {nombre} / 2. {dia} / 3. {mes} / 4. {año} / 5. {hora} / 6. {minuto} / 7. {duracion}]: "))
        if cambio == 1:
            cambio_datos = modificar_datos(nombre)
        elif cambio == 2:
            cambio_datos = modificar_datos(dia)
            validacion_fecha, dia, mes, año = validacion_fecha(dia, mes, año)
            
            while validacion_fecha != True:
                cambio_datos = modificar_datos(dia)
                validacion_fecha, dia, mes, año = validacion_fecha(dia, mes, año)
        elif cambio == 3:
            cambio_datos = modificar_datos(mes)
        elif cambio == 4:
            cambio_datos = modificar_datos(año)
        elif cambio == 5:
            cambio_datos = modificar_datos(hora)
        elif cambio == 6:
            cambio_datos = modificar_datos(minuto)
        elif cambio == 7 :
            cambio_datos = modificar_datos(duracion)
                
#---------------programa principal------------
ejecutar_reserva = generar_reserva()