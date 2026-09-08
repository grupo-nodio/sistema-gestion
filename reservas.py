import re

def pedir_numero(A):
    valor = input(A)

    while not re.match(r"^\d+$", valor):
        print("Valor ingresado invalido. ")
        valor = input("Ingrese unicamente valores numericos: ")

    return int(valor)

def escritura_digitos(A):
    ''' Agrega un 0 por delante a los valores numericos inferiores a 10 '''
    if A < 10:
        A = "0" + str(A)
    else:
        A = str(A)
    return A

def validar_fecha(dia, mes, año):
    ''' Verifica que la fecha sea valida, si el año es menor a 2026 = invalido, si el mes es menor a 1 y mayor a 13 = invalido y los dias si son menores a 1 y mayores a [28, 29, 30, 31], dependiendo del mes '''
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
                dia = pedir_numero("Ingrese el día de la reserva: ")
            elif mes == 0:
                print("La fecha ingresada es errónea. Por favor, reingrese el mes correspondiente.")
                mes = pedir_numero("Ingrese el mes de la reserva: ")
            elif año == 0:
                print("La fecha ingresada es errónea. Por favor, reingrese el año correspondiente.")
                año = pedir_numero("Ingrese el año de la reserva: ")

    return dia, mes, año

def validar_hora(hora, minuto):
    ''' Valida la hora, a traves de un formato de 24 horas y intervalos de 30 minutos '''
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
                hora = pedir_numero("Ingrese la hora de la reserva (formato de 24 horas): ")
            elif minuto == 1:
                print("El valor de minutos ingresado es erróneo. Por favor, reingrese un valor válido.")
                minuto = pedir_numero("Ingrese los minutos de la reserva (00 o 30): ")

    return hora, minuto

def modificar_datos(A):
    ''' Funcion utilizada para modificar los valores dentro de una reserva '''
    A = pedir_numero(f"Ingrese el nuevo valor que reemplazará al dato actual [{A}]: ")

    return A

def contar_duracion(duracion, hora):
    ''' Permite calcular la hora exacta en la que terminara la reserva, tomando en cuanta a la hora que comienza y la duracion de la misma '''
    horaduracion = hora
    for i in range(duracion):
        if horaduracion == 23:
            horaduracion = 0
        else:
            horaduracion = horaduracion + 1
    return duracion, horaduracion

def escribir_fecha():
    """ Permite escribir la fecha dentro de un mismo input, para luego tomar los valores numericos por separado """
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
    """ Permite escribir el horario dentro de un mismo input, para luego tomar los valores numericos por separado """
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

def generar_reserva(sel, estacionamientos, reservar):
    ''' Permite generar una reserva tomando datos como, la fecha, el horario, la duracion, y el nombre del titular de la reserva '''
    
    # 1. VERIFICACIÓN: Comprobar si hay espacio antes de pedir los datos
    if estacionamientos[4][sel] <= 0:
        print("\nNo hay espacios disponibles en este estacionamiento.")
        return

    print("\n" + "=" * 44)
    print("\n GENERANDO RESERVA \n")
    print("=" * 44)

    dia, mes, año = escribir_fecha()
    dia, mes, año = validar_fecha(dia, mes, año)

    hora, minuto = escribir_horario()
    hora, minuto = validar_hora(hora, minuto)

    duracion = pedir_numero("Ingrese la duración estimada de la reserva (en intervalos de una hora): ")
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

    if control in ["Y", "y", "yes", "Yes", "si", "Si"]:
        nombre = input("Ingrese el nombre del titular de la reserva: ")
        
        # 2. REDUCCIÓN DE CAPACIDAD: Restamos 1 al espacio disponible actual (índice 4)
        estacionamientos[4][sel] -= 1
        
        print(f"La reserva se efectuo correctamente bajo el nombre de {nombre} para la fecha {escritura_digitos(dia)}/{escritura_digitos(mes)}/{escritura_digitos(año)}, empezara a las {escritura_digitos(hora)}:{escritura_digitos(minuto)} hs y finalizara a las {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs")

        reserva = [nombre, dia, mes, año, hora, minuto, duracion, sel]
        reservar.append(reserva)

def mostrar_lista_reservas(reservar):
    """ Muestra únicamente las reservas. """
    for i in range(len(reservar)):
        print(f"{i + 1}. Nombre: {reservar[i][0]} / dia: {escritura_digitos(reservar[i][1])} / mes: {escritura_digitos(reservar[i][2])} / año: {escritura_digitos(reservar[i][3])} / hora: {escritura_digitos(reservar[i][4])} / minuto: {escritura_digitos(reservar[i][5])} / duracion: {escritura_digitos(reservar[i][6])}hs / estacionamiento: {escritura_digitos(reservar[i][7])}. ")

def consultar_reservas(reservar):
    ''' Permite consultar las reservas realizadas previamente '''
    print("\n" + "=" * 44)
    print("\n CONSULTAR RESERVAS \n")
    print("=" * 44)
    mostrar_lista_reservas(reservar)
    input("\nPresione ENTER para volver...")

def cancelar_reserva(sel, estacionamientos, reservar, reservas_canceladas):
    ''' Permite ver las reservas hechas y cancelar la reserva seleccionada '''
    print("\n--- RESERVAS EXISTENTES ---")
    mostrar_lista_reservas(reservar)
    
    reserva_num = pedir_numero("\nSeleccione el número de la reserva que desea cancelar: ")

    while reserva_num < 1 or reserva_num > len(reservar):
        print("Opción fuera de rango. Reingrese. ")
        reserva_num = pedir_numero(f"Seleccione un número entre 1 y {len(reservar)}: ")

    indice = reserva_num - 1
    nombre, dia, mes, año, hora, minuto, duracion, sel = reservar[indice]
    duracion, horaduracion = contar_duracion(duracion, hora)

    print("\n" + "=" * 44)
    print(f"CANCELAR RESERVA DE: {nombre}")
    print("=" * 44)
    print(f"Fecha: {escritura_digitos(dia)}-{escritura_digitos(mes)}-{escritura_digitos(año)}")
    print(f"Horario: {escritura_digitos(hora)}:{escritura_digitos(minuto)} hs a {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs (Duración: {duracion} hs)")

    confirmacion_cancelar = input("¿Esta seguro de que desea cancelar esta reserva?, [Y / N]: ") 

    if confirmacion_cancelar in ["Y", "y", "yes", "Yes", "si", "Si"]:
        reserva_cancelada = [nombre, dia, mes, año, hora, minuto, duracion, sel]
        reservas_canceladas.append(reserva_cancelada)
        reservar.pop(indice)
        
        # Se verifica que al devolver el espacio no se supere la capacidad total (índice 3)
        if estacionamientos[4][sel] < estacionamientos[3][sel]:
            estacionamientos[4][sel] += 1
            
        print("Reserva cancelada exitosamente.")
        input("\nPresione ENTER para continuar...")

def modificar_reserva(reservar):
    """ Permite ver las reservas y modificar algun dato seleccionado de una, habiendo terminado la reserva previamente """
    print("\n--- RESERVAS EXISTENTES ---")
    mostrar_lista_reservas(reservar)

    reserva_num = pedir_numero("\nSeleccione el número de la reserva que desea modificar: ")

    while reserva_num < 1 or reserva_num > len(reservar):
        print("Opción fuera de rango. Reingrese.")
        reserva_num = pedir_numero(f"Seleccione un número entre 1 y {len(reservar)}: ")

    indice = reserva_num - 1
    nombre, dia, mes, año, hora, minuto, duracion = reservar[indice]
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

    reservar[indice] = [nombre, dia, mes, año, hora, minuto, duracion]
    print("\n¡La reserva fue actualizada exitosamente!")
    input("\nPresione ENTER para continuar...")