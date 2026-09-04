import re

def escritura_digitos(A):
    if A < 10:
        A = "0" + str(A)
    else:
        A = str(A)
    return A

def validar_fecha(dia, mes, año):
    fecha = False
    while not fecha:
        fecha = True
        if año < 2026:
            año = 0
            fecha = False

        if mes < 1 or mes > 12:
            mes = 0
            fecha = False

        if dia < 1 or dia > 31:
            dia = 0
            fecha = False

        if mes in [4, 6, 9, 11] and dia > 30:
            dia = 0
            fecha = False

        if mes == 2:
            if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
                if dia > 29:
                    dia = 0
                    fecha = False
            else:
                if dia > 28:
                    dia = 0
                    fecha = False

        if not fecha:
            if dia == 0:
                print("La fecha ingresada no es valida, por favor, modifique el dia.")
                dia = int(input("Ingrese el dia que desea hacer la reserva: "))
            elif mes == 0:
                print("La fecha ingresada no es valida, por favor, modifique el mes.")
                mes = int(input("Ingrese el mes que desea hacer la reserva: "))
            elif año == 0:
                print("La fecha ingresada no es valida, por favor, modifique el año.")
                año = int(input("Ingrese el año que desea hacer la reserva: "))

    return dia, mes, año

def validar_hora(hora, minuto):
    tiempo = False
    while not tiempo:
        tiempo = True
        if hora < 0 or hora > 23:
            hora = 0
            tiempo = False

        if minuto not in [0, 30]:
            minuto = 1
            tiempo = False

        if not tiempo:
            if hora == 0:
                print("La hora ingresada es invalida, por favor, modifique la hora.")
                hora = int(input("Ingrese la hora de la reserva, (formato de 24 horas): "))
            elif minuto == 1:
                print("El o los minuto/s ingresado es invalido, por favor, modifique los minutos.")
                minuto = int(input("Ingrese el minuto de la reserva: "))

    return hora, minuto

def modificar_datos(A):
    A = int(input(f"Ingrese el nuevo dato, que modificara al dato [{A}]: "))
    return A

def contar_duracion(duracion, hora):
    horaduracion = hora
    for i in range(duracion):
        if horaduracion == 23:
            horaduracion = 0
        else:
            horaduracion = horaduracion + 1
    return duracion, horaduracion

def escribir_fecha():
    valido = False
    dia, mes, año = 0, 0, 0
    while not valido:
        fecha = input("Ingrese la fecha de la reserva, formato (DD - MM - YYYY): ")
        numeros = re.findall(r"\d+", fecha)

        match numeros:
            case [d, m, a] if len(a) == 4:
                dia = int(d)
                mes = int(m)
                año = int(a)
                valido = True
            case _:
                print("Fecha ingresada invalida. Debe ingresar un dia, un mes y un año con 4 digitos.")

    return dia, mes, año

def escribir_horario():
    valido = False
    hora, minuto = 0, 0
    while not valido:
        horario = input("Ingrese la hora de la reserva. Formato [Horas en 24 hr y minutos saltos de media hr (HH : MM)]: ")
        numeros = re.findall(r"\d+", horario)

        match numeros:
            case [h, m]:
                hora = int(h)
                minuto = int(m)
                valido = True

    return hora, minuto

def generar_reserva(estacionamientos):

    dia, mes, año = escribir_fecha()
    dia, mes, año = validar_fecha(dia, mes, año)

    hora, minuto = escribir_horario()
    hora, minuto = validar_hora(hora, minuto)

    duracion = int(input("Ingrese cuanto tiempo durara la reserva (saltos de una hora): "))
    duracion, horaduracion = contar_duracion(duracion, hora)

    print("=" * 44)
    print("\n CONTROL DE RESERVA \n")
    print("=" * 44)
    print("\n En la fecha DD - MM - YYYY: ", escritura_digitos(dia), "-", escritura_digitos(mes), "-", escritura_digitos(año))
    print(f"la reserva comenzara a las: {escritura_digitos(hora)} : {escritura_digitos(minuto)} y durara hasta las: {escritura_digitos(horaduracion)} : {escritura_digitos(minuto)} hs")

    control = input("\nVerifique si los datos tomados son los correctos [Y / N]: ")

    if control not in ["Y", "y", "yes", "Yes", "si", "Si"]:
        while control not in ["Y", "y", "yes", "Yes", "si", "Si"]:
            cambio = int(input(f"¿Cual de los siguientes datos desea modificar?, [1. {escritura_digitos(dia)} / 2. {escritura_digitos(mes)} / 3. {escritura_digitos(año)} / 4. {escritura_digitos(hora)} / 5. {escritura_digitos(minuto)} / 6. {duracion}]: "))

            match cambio:
                case 1:
                    dia = modificar_datos(dia)
                    dia, mes, año = validar_fecha(dia, mes, año)
                case 2:
                    mes = modificar_datos(mes)
                    dia, mes, año = validar_fecha(dia, mes, año)
                case 3:
                    año = modificar_datos(año)
                    dia, mes, año = validar_fecha(dia, mes, año)
                case 4:
                    hora = modificar_datos(hora)
                    hora, minuto = validar_hora(hora, minuto)
                    duracion, horaduracion = contar_duracion(duracion, hora)
                case 5:
                    minuto = modificar_datos(minuto)
                    hora, minuto = validar_hora(hora, minuto)
                case 6:
                    duracion = modificar_datos(duracion)
                    duracion, horaduracion = contar_duracion(duracion, hora)
                case _:
                    print("Opción no válida.")

            print("=" * 44)
            print("\n CONTROL DE RESERVA \n")
            print("=" * 44)
            print("\n En la fecha DD - MM - YYYY: ", escritura_digitos(dia), "-", escritura_digitos(mes), "-", escritura_digitos(año))
            print(f"la reserva comenzara a las: {escritura_digitos(hora)} : {escritura_digitos(minuto)} hs y durara hasta las: {escritura_digitos(horaduracion)} : {escritura_digitos(minuto)} hs")
            control = input("\nVerifique si los datos tomados son los correctos [Y / N]: ")

    if control in ["Y", "y", "yes", "Yes", "si", "Si"]:
        nombre = input("Ingrese el nombre bajo el cual estara la reserva: ")
        print(f"La reserva se efectuo correctamente bajo el nombre de {nombre} para la fecha {dia}/{mes}/{año}, empezara a las {hora}:{minuto} hs y finalizara a las {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs")


def menu_reservas(estacionamientos):
    print("=" * 44)
    print("\n------------BIENVENIDO A RESERVAS------------\n")
    print("=" * 44)
    print("\n------------MENU RESERVAS------------\n")

    opcion = int(input("Seleccione la opcion que desea realizar. [1. Generar una reserva / 2. Consultar reservas / 3. Modificar reserva / 4. Cancelar una reserva.] : "))

    if opcion == 1:
        generar_reserva(estacionamientos)