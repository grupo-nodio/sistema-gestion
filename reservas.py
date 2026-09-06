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
                print("La fecha ingresada es errónea. Por favor, reingrese el día correspondiente.")
                dia = int(input("Ingrese el día de la reserva: "))
            elif mes == 0:
                print("La fecha ingresada es errónea. Por favor, reingrese el mes correspondiente.")
                mes = int(input("Ingrese el mes de la reserva: "))
            elif año == 0:
                print("La fecha ingresada es errónea. Por favor, reingrese el año correspondiente.")
                año = int(input("Ingrese el año de la reserva: "))

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
                print("La hora ingresada es errónea. Por favor, reingrese la hora en el formato especificado.")
                hora = int(input("Ingrese la hora de la reserva (formato de 24 horas): "))
            elif minuto == 1:
                print("El valor de minutos ingresado es erróneo. Por favor, reingrese un valor válido.")
                minuto = int(input("Ingrese los minutos de la reserva (00 o 30): "))

    return hora, minuto

def modificar_datos(A):
    A = int(input(f"Ingrese el nuevo valor que reemplazará al dato actual [{A}]: "))
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
                print("El formato de fecha es incorrecto. Debe ingresar el día, el mes y el año con 4 dígitos.")

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

def generar_reserva(estacionamientos, reservas):
    print("\n" + "=" * 44)
    print("\n GENERANDO RESERVA \n")
    print("=" * 44)

    dia, mes, año = escribir_fecha()
    dia, mes, año = validar_fecha(dia, mes, año)

    hora, minuto = escribir_horario()
    hora, minuto = validar_hora(hora, minuto)

    duracion = int(input("Ingrese la duración estimada de la reserva (en intervalos de una hora): "))
    duracion, horaduracion = contar_duracion(duracion, hora)

    print("\n" + "=" * 44)
    print("\n CONTROL DE RESERVA \n")
    print("=" * 44)
    print("\nEn la fecha DD - MM - YYYY: ", escritura_digitos(dia), "-", escritura_digitos(mes), "-", escritura_digitos(año))
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
            print("\nEn la fecha DD - MM - YYYY: ", escritura_digitos(dia), "-", escritura_digitos(mes), "-", escritura_digitos(año))
            print(f"la reserva comenzara a las: {escritura_digitos(hora)} : {escritura_digitos(minuto)} hs y durara hasta las: {escritura_digitos(horaduracion)} : {escritura_digitos(minuto)} hs")
            control = input("\nVerifique si los datos tomados son los correctos [Y / N]: ")

    nombre = ""
    if control in ["Y", "y", "yes", "Yes", "si", "Si"]:
        nombre = input("Ingrese el nombre del titular de la reserva: ")
        print(f"La reserva se efectuo correctamente bajo el nombre de {nombre} para la fecha {escritura_digitos(dia)}/{escritura_digitos(mes)}/{escritura_digitos(año)}, empezara a las {escritura_digitos(hora)}:{escritura_digitos(minuto)} hs y finalizara a las {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs")

    reserva = [nombre, dia, mes, año, hora, minuto, duracion]
    reservas.append(reserva)

def mostrar_lista_reservas(reservas):
    """ Muestra únicamente las reservas sin forzar una llamada al menú. """
    for i in range(len(reservas)):
        print(f"{i + 1}. Nombre: {reservas[i][0]} / dia: {escritura_digitos(reservas[i][1])} / mes: {escritura_digitos(reservas[i][2])} / año: {escritura_digitos(reservas[i][3])} / hora: {escritura_digitos(reservas[i][4])} / minuto: {escritura_digitos(reservas[i][5])} / duracion: {escritura_digitos(reservas[i][6])}hs.")

def consultar_reservas(reservas):
    print("\n" + "=" * 44)
    print("\n CONSULTAR RESERVAS \n")
    print("=" * 44)
    mostrar_lista_reservas(reservas)
    input("\nPresione ENTER para volver...")

def cancelar_reserva(reservas):
    print("\n--- RESERVAS EXISTENTES ---")
    mostrar_lista_reservas(reservas)
    
    reserva_num = int(input("\nSeleccione el número de la reserva que desea cancelar: "))

    # Arreglado: uso de 'or' para corregir la condición lógica del rango
    while reserva_num < 1 or reserva_num > len(reservas):
        print("Opción fuera de rango. Reingrese. ")
        reserva_num = int(input(f"Seleccione un número entre 1 y {len(reservas)}: "))

    indice = reserva_num - 1
    nombre, dia, mes, año, hora, minuto, duracion = reservas[indice]
    duracion, horaduracion = contar_duracion(duracion, hora)

    print("\n" + "=" * 44)
    print(f"CANCELAR RESERVA DE: {nombre}")
    print("=" * 44)
    print(f"Fecha: {escritura_digitos(dia)}-{escritura_digitos(mes)}-{escritura_digitos(año)}")
    print(f"Horario: {escritura_digitos(hora)}:{escritura_digitos(minuto)} hs a {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs (Duración: {duracion} hs)")

    confirmacion_cancelar = input("¿Esta seguro de que desea cancelar esta reserva?, [Y / N]: ") 

    if confirmacion_cancelar in ["Y", "y", "yes", "Yes", "si", "Si"]:
        reservas.pop(indice)
        print("Reserva cancelada exitosamente.")
        input("\nPresione ENTER para continuar...")

def modificar_reserva(reservas):
    print("\n--- RESERVAS EXISTENTES ---")
    mostrar_lista_reservas(reservas)

    reserva_num = int(input("\nSeleccione el número de la reserva que desea modificar: "))

    while reserva_num < 1 or reserva_num > len(reservas):
        print("Opción fuera de rango. Reingrese.")
        reserva_num = int(input(f"Seleccione un número entre 1 y {len(reservas)}: "))

    indice = reserva_num - 1
    nombre, dia, mes, año, hora, minuto, duracion = reservas[indice]
    duracion, horaduracion = contar_duracion(duracion, hora)

    control = "N"
    while control not in ["Y", "y", "yes", "Yes", "si", "Si"]:
        print("\n" + "=" * 44)
        print(f"MODIFICANDO RESERVA DE: {nombre}")
        print("=" * 44)
        print(f"Fecha: {escritura_digitos(dia)}-{escritura_digitos(mes)}-{escritura_digitos(año)}")
        print(f"Horario: {escritura_digitos(hora)}:{escritura_digitos(minuto)} hs a {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs (Duración: {duracion} hs)")

        cambio = int(input("\n¿Qué dato desea modificar?\n"
                           f"[1. Nombre ({nombre}) / "
                           f"2. Día ({escritura_digitos(dia)}) / "
                           f"3. Mes ({escritura_digitos(mes)}) / "
                           f"4. Año ({escritura_digitos(año)}) / "
                           f"5. Hora ({escritura_digitos(hora)}) / "
                           f"6. Minuto ({escritura_digitos(minuto)}) / "
                           f"7. Duración ({duracion})]: "))

        match cambio:
            case 1:
                nombre = input("Ingrese el nuevo nombre: ")
            case 2:
                dia = modificar_datos(dia)
                dia, mes, año = validar_fecha(dia, mes, año)
            case 3:
                mes = modificar_datos(mes)
                dia, mes, año = validar_fecha(dia, mes, año)
            case 4:
                año = modificar_datos(año)
                dia, mes, año = validar_fecha(dia, mes, año)
            case 5:
                hora = modificar_datos(hora)
                hora, minuto = validar_hora(hora, minuto)
                duracion, horaduracion = contar_duracion(duracion, hora)
            case 6:
                minuto = modificar_datos(minuto)
                hora, minuto = validar_hora(hora, minuto)
            case 7:
                duracion = modificar_datos(duracion)
                duracion, horaduracion = contar_duracion(duracion, hora)
            case _:
                print("Opción no válida.")

        control = input("\n¿Está conforme con los datos modificados? [Y / N]: ")

    reservas[indice] = [nombre, dia, mes, año, hora, minuto, duracion]
    print("\n¡La reserva fue actualizada exitosamente!")
    input("\nPresione ENTER para continuar...")

def menu_reservas(estacionamientos, reservas):
    print("\n" + "=" * 44)
    print("-----------BIENVENIDO A RESERVAS-----------")
    print("=" * 44)
    print("------------MENU RESERVAS------------\n")

    opcion = int(input("Seleccione la opcion que desea realizar. [1. Generar una reserva / 2. Consultar reservas / 3. Modificar reserva / 4. Cancelar una reserva / 0. Salir]: "))

    if opcion == 1:
        generar_reserva(estacionamientos, reservas)

    elif opcion == 2:
        if len(reservas) == 0:
            print("\n---------------- !IMPORTANTE¡ ---------------- \n")
            print("Debe cargarse una reserva previamente.\n")
        else:
            consultar_reservas(reservas)

    elif opcion == 3:
        if len(reservas) == 0:
            print("\n---------------- !IMPORTANTE¡ ---------------- \n")
            print("Debe cargarse una reserva previamente.\n")
        else:
            modificar_reserva(reservas)

    elif opcion == 4:
        if len(reservas) == 0:
            print("\n---------------- !IMPORTANTE¡ ---------------- \n")
            print("Debe cargarse una reserva previamente.\n")
        else:
            cancelar_reserva(reservas)

    elif opcion == 0:
        print("Saliendo del módulo de reservas.")