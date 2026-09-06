import re

reservas = []

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

def generar_reserva():

    dia, mes, año = escribir_fecha()
    dia, mes, año = validar_fecha(dia, mes, año)

    hora, minuto = escribir_horario()
    hora, minuto = validar_hora(hora, minuto)

    duracion = int(input("Ingrese cuanto tiempo durara la reserva (saltos de una hora): "))
    duracion, horaduracion = contar_duracion(duracion, hora)

    print("=" * 44)
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
        nombre = input("Ingrese el nombre bajo el cual estara la reserva: ")
        print(f"La reserva se efectuo correctamente bajo el nombre de {nombre} para la fecha {escritura_digitos(dia)}/{escritura_digitos(mes)}/{escritura_digitos(año)}, empezara a las {escritura_digitos(hora)}:{escritura_digitos(minuto)} hs y finalizara a las {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs")

    reserva = [nombre, dia, mes, año, hora, minuto, duracion]

    reservas.append(reserva)

    eleccion = elegir_paso()

def consultar_reservas(reservas):
        for i in range(len(reservas)):
            print(f"{i + 1}. reserva {i}: Nombre {reservas[i][0]} / dia {escritura_digitos(reservas[i][1])} / mes {escritura_digitos(reservas[i][2])} / año {escritura_digitos(reservas[i][3])} / hora {escritura_digitos(reservas[i][4])} / minuto {escritura_digitos(reservas[i][5])} / duracion {escritura_digitos(reservas[i][6])}. ")

        menu_reservas()

def elegir_paso():
    eleccion = int(input("\nSeleccione una opcion. [1. Desea volver al menu / 2. Realizar otra reserva]: "))

    if eleccion == 2:
        reserva = generar_reserva()

    else:
        menu = menu_reservas()

def modificar_reserva(reservas):
    consultar_reservas(reservas)

    # 2. Pedimos el número de reserva a modificar
    reserva_num = int(input("Seleccione la reserva que desea modificar: "))
    
    # Validamos que la opción ingresada esté en el rango de reservas cargadas
    while reserva_num < 1 or reserva_num > len(reservas):
        print("Opción fuera de rango. Por favor, intente nuevamente.")
        reserva_num = int(input(f"Seleccione un número entre 1 y {len(reservas)}: "))
    
    # Ajustamos el número ingresado al índice real de la lista (base 0)
    indice = reserva_num - 1
    
    # 3. Desempaquetamos los datos de la reserva seleccionada
    nombre, dia, mes, año, hora, minuto, duracion = reservas[indice]
    duracion, horaduracion = contar_duracion(duracion, hora)

    print("\n--- MODIFICANDO RESERVA SELECCIONADA ---")
    control = "N"

    # 4. Bucle para permitir modificar datos
    while control not in ["Y", "y", "yes", "Yes", "si", "Si"]:
        print("=" * 44)
        print(f"Reserva de: {nombre}")
        print(f"Fecha: {escritura_digitos(dia)}-{escritura_digitos(mes)}-{escritura_digitos(año)}")
        print(f"Horario: {escritura_digitos(hora)}:{escritura_digitos(minuto)} hs hasta {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs (Duración: {duracion} hs)")
        print("=" * 44)

        cambio = int(input(f"\n¿Qué dato desea modificar?\n"
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

        control = input("\n¿Está conforme con las modificaciones hechas? [Y / N]: ")

    # 5. Sobrescribimos la reserva modificada en la lista global
    reservas[indice] = [nombre, dia, mes, año, hora, minuto, duracion]
    print("\n¡La reserva ha sido actualizada correctamente!")
    
    menu_reservas()


def menu_reservas():
    print("=" * 44)
    print("\n------------BIENVENIDO A RESERVAS------------\n")
    print("=" * 44)
    print("\n------------MENU RESERVAS------------\n")

    opcion = int(input("Seleccione la opcion que desea realizar. [1. Generar una reserva / 2. Consultar reservas / 3. Modificar reserva / 4. Cancelar una reserva / 0. Volver al menu principal.] : "))
    if opcion == 1:
        generar_reserva()

    if opcion == 2:
        if len(reservas) == 0:
            print("Debe cargarse una reserva previamente.")
            menu_reservas()

        else:
            consultar_reservas(reservas)

    if opcion == 3:
        if len(reservas) == 0:
            print("Debe cargarse una reserva previamente.")
            menu_reservas()
    
        else:
            modificar_reserva(reservas)

menu = menu_reservas()