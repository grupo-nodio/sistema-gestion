def validar_fecha(dia, mes, año):
    if año < 2026:
        año == False
        return año
    if mes < 1 or mes > 12:
        mes == False
        return mes
    if dia < 1 or dia > 31:
        dia == False
        return dia
    if mes in [4, 6, 9, 11] and dia > 30:
        dia = False
        return dia
    if mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            if dia > 29:
                dia == False
                return dia
        else:
            if dia > 28:
                dia == False
                return dia
    return True

def validar_hora(hora, minuto):
    if hora < 0 or hora > 23:
        return False
    if minuto < 0 or minuto > 59:
        return False

    return True

def generar_reserva():
    nombre = input("Ingrese su nombre: ")
    
    dia = int(input("Ingrese el día de la reserva: "))
    mes = int(input("Ingrese el mes de la reserva: "))
    año = int(input("Ingrese el año de la reserva: "))
    validacion = validar_fecha(dia, mes, año)

    if validacion != True:
        print("La fecha ingresada no es válida. Por favor, intente nuevamente.")
        while dia == False:
            dia = int(input("Ingrese el día de la reserva: "))
            validacion = validar_fecha(dia, mes, año)
        while mes == False:
            mes = int(input("Ingrese el mes de la reserva: "))
            validacion = validar_fecha(dia, mes, año)
        while año == False:
            año = int(input("Ingrese el año de la reserva: "))
            validacion = validar_fecha(dia, mes, año)

    else:
        Hora = int(input("Ingrese la hora de la reserva (formato 24 horas): "))
        minuto = int(input("Ingrese el minuto de la reserva: "))
        validacion_hora = validar_hora(Hora, minuto)

        if validacion_hora == False:
            print("La hora ingresada no es válida. Por favor, intente nuevamente.")
            while validacion_hora == False:
                Hora = int(input("Ingrese la hora de la reserva (formato 24 horas): "))
                minuto = int(input("Ingrese el minuto de la reserva: "))
                validacion_hora = validar_hora(Hora, minuto)

        else:
            print(f"Reserva realizada con éxito para {nombre} el {dia}/{mes}/{año} a las {Hora}:{minuto}.")
            return (nombre, dia, mes, año, Hora, minuto)


nombre, dia, mes, año, Hora, minuto = generar_reserva()