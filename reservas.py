def escritura_dijitos(A):
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

def generar_reserva():
    nombre = input("Ingrese el nombre para comenzar la reserva: ")

    dia = int(input("Ingrese el dia que desea hacer la reserva: "))
    mes = int(input("Ingrese el mes que desea hacer la reserva: "))
    año = int(input("Ingrese el año que desea hacer la reserva: "))
    validacion_fecha, dia, mes, año = validar_fecha(dia, mes, año)

    if validacion_fecha != True:
        while validacion_fecha != True:
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
    else:
        hora = int(input("Ingrese la hora de la reserva, (formato de 24 horas): "))
        minuto = int(input("Ingrese el minuto de la reserva: "))
        duracion = int(input("Ingrese cuanto tiempo durara la reserva: "))
        validacion_horario, hora, minuto = validar_hora(hora, minuto)

        if validacion_horario != True:
            while validacion_horario != True:
                if hora == 0:
                    print("La hora ingresada es invalida, por favor, modifique la hora.")
                    hora = int(input("Ingrese la hora de la reserva, (formato de 24 horas): "))
                elif minuto == 0:
                    print("El o los minuto/s ingresado es invalido, por favor, modifique los minutos.")
                    minuto = int(input("Ingrese el minuto de la reserva: "))
                validacion_horario, hora, minuto = validar_hora

        else:
            dia = escritura_dijitos(dia)
            mes = escritura_dijitos(mes)
            hora = escritura_dijitos(hora)
            minuto = escritura_dijitos(minuto)
            print("\n -------------CONTROL DE RESERVA------------- \n")
            print("La reserva se genero bajo el nombre de: " + str(nombre))
            print("En la fecha DD - MM - YYYY: ",dia ," - ",mes ," - ",año)
            print("la reserva comenzara a las: ",hora ,":",minuto, ", y durara: ", duracion,"hs")
                
#---------------programa principal------------
ejecutar_reserva = generar_reserva()