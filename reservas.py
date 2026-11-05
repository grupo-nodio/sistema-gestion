import re, json

def cargar_datos_json(name_archive):
    '''Funcion utilizada, para la lectura o creacion del archivo .json.'''

    try:
        with open(name_archive, "r", encoding="UTF-8") as archivo:
            return json.load(archivo)
    except(FileNotFoundError, json.JSONDecodeError): 
        return [None]

def guardar_datos_json(name_archive, datos):
    '''Abre el archivo .json, y almacena los cambios realizados en los diccionarios, para luego cerrar el archivo.'''
    with open(name_archive, "w", encoding="UTF-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def pedir_nombre(mensaje):
    '''Funcion usada para utilizar pedir exclusivamente valores alfabeticos.'''
    name = input(mensaje)

    while not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", name):
        print("Palabra ingresada inválida.")
        name = input("Ingrese únicamente valores alfabéticos: ")
        
    return name

def pedir_numero(mensaje):
    '''Funcion usada para utilizar pedir exclusivamente valores numericos.'''
    while True:
        valor = input(mensaje)

        try:
            return int(valor)
        except ValueError:
            print("El valor ingresado no es de valor numerico. Vuelva a ingresar.")

def escritura_digitos(A):
    '''Se introduce una variable obligatoriamente numerica, y en caso de ser menor a 10, se le introduce un cero adelante.'''
    if A < 10:
        A = "0" + str(A)
    else:
        A = str(A)
    return A

def validar_fecha(dia, mes, año):
    '''Se controla que la fecha ingresada, sea una fecha valida para los estandares del sistema.'''
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

        if mes in (4, 6, 9, 11) and dia > 30:
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
    '''Se controla que el horario ingresado, sea un horario valido para los estandares del sistema.'''
    tiempo = False
    while not tiempo:
        tiempo = True
        if hora < 0 or hora > 23:
            hora = 0
            tiempo = False

        if minuto not in (0, 30):
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
    A = pedir_numero(f"Ingrese el nuevo valor que reemplazará al dato actual [{A}]: ")
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

def generar_archivo(nombre_archivo, lista_reservas, EST_JSON, sel, indice):
    try:
        archivo = open(nombre_archivo, 'w', encoding="UTF-8")

        nombre = lista_reservas[indice]['nombre']
        dia = lista_reservas[indice]['dia']
        mes = lista_reservas[indice]['mes']
        año = lista_reservas[indice]['año'] 
        hora = lista_reservas[indice]['hora']
        minuto = lista_reservas[indice]['minuto'] 
        duracion = lista_reservas[indice]['duracion']
        _, horaduracion = contar_duracion(duracion, hora)

        archivo.write("=" * 50 + "\n")
        archivo.write(f"{'TICKET DE RESERVA':^50}\n")
        archivo.write("=" * 50 + "\n\n")

        archivo.write(f" ESTACIONAMIENTO: {EST_JSON[sel]['nombre']}\n")
        archivo.write(f" TITULAR:         {nombre}\n\n")

        archivo.write("-" * 50 + "\n")
        archivo.write(f" Fecha:           {escritura_digitos(dia)}/{escritura_digitos(mes)}/{escritura_digitos(año)}\n")
        archivo.write(f" Hora de inicio:  {escritura_digitos(hora)}:{escritura_digitos(minuto)} hs\n")
        archivo.write(f" Hora de fin:     {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs\n")
        archivo.write(f" Tiempo total:    {escritura_digitos(duracion)} horas\n")
        archivo.write(f"\n Estado de reserva: \n")
        archivo.write("-" * 50 + "\n\n")

        archivo.write(f"{'¡RESERVA REALIZADA CON ÉXITO!':^50}\n")
        archivo.write("=" * 50 + "\n")

        archivo.close()

        print("Recibo realizado con exito.")

    except FileNotFoundError:
        print("Archivo no encontrado.")

def escribir_archivo(nombre_archivo, lista_reservas, EST_JSON, sel, indice):
    try:
        archivo = open(nombre_archivo, 'a', encoding="UTF-8")
    
        nombre = lista_reservas[indice]['nombre']
        dia = lista_reservas[indice]['dia']
        mes = lista_reservas[indice]['mes']
        año = lista_reservas[indice]['año'] 
        hora = lista_reservas[indice]['hora']
        minuto = lista_reservas[indice]['minuto'] 
        duracion = lista_reservas[indice]['duracion']
        _, horaduracion = contar_duracion(duracion, hora)
    
        archivo.write("=" * 50 + "\n")
        archivo.write(f"{'TICKET DE RESERVA':^50}\n")
        archivo.write("=" * 50 + "\n\n")
    
        archivo.write(f" ESTACIONAMIENTO: {EST_JSON[sel]['nombre']}\n")
        archivo.write(f" TITULAR:         {nombre}\n\n")
    
        archivo.write("-" * 50 + "\n")
        archivo.write(f" Fecha:           {escritura_digitos(dia)}/{escritura_digitos(mes)}/{escritura_digitos(año)}\n")
        archivo.write(f" Hora de inicio:  {escritura_digitos(hora)}:{escritura_digitos(minuto)} hs\n")
        archivo.write(f" Hora de fin:     {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs\n")
        archivo.write(f" Tiempo total:    {escritura_digitos(duracion)} horas\n")
        archivo.write(f"\n Estado de reserva: \n")
        archivo.write("-" * 50 + "\n\n")
    
        archivo.write(f"{'¡RESERVA REALIZADA CON ÉXITO!':^50}\n")
        archivo.write("=" * 50 + "\n")
    
        archivo.close()
    
        print("Recibo realizado con exito.")
    
    except FileNotFoundError:
        print("Archivo no encontrado.")

def generar_reserva(sel, EST_JSON, RESER_JSON, reservar):
    if EST_JSON[sel]['capacidad_actual'] <= 0:
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
    while duracion <= 0:
        print("Duracion ingresada invalida.")
        duracion = pedir_numero("Ingrese la duración estimada de la reserva (en intervalos de una hora): ")
    duracion, horaduracion = contar_duracion(duracion, hora)

    print("\n" + "=" * 44)
    print("\n CONTROL DE RESERVA \n")
    print("=" * 44)
    print("\nEn la fecha DD - MM - YYYY: ", escritura_digitos(dia), "-", escritura_digitos(mes), "-", escritura_digitos(año))
    print(f"la reserva comenzara a las: {escritura_digitos(hora)} : {escritura_digitos(minuto)} y durara hasta las: {escritura_digitos(horaduracion)} : {escritura_digitos(minuto)} hs")

    control = input("\nVerifique si los datos tomados son los correctos [Y / N]: ")

    if control.lower() not in ("y", "yes", "si"):
        while control.lower() not in ("y", "yes", "si"):
            cambio = pedir_numero(f"¿Cual de los siguientes datos desea modificar?, [1. {escritura_digitos(dia)} / 2. {escritura_digitos(mes)} / 3. {escritura_digitos(año)} / 4. {escritura_digitos(hora)} / 5. {escritura_digitos(minuto)} / 6. {duracion}]: ")

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
                    while duracion <= 0:
                        print("Duracion ingresada invalida.")
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

    if control.lower() in ("y", "yes", "si"):
        nombre = pedir_nombre("Ingrese el nombre del titular de la reserva: ")
        
        EST_JSON[sel]['capacidad_actual'] -= 1
        
        print(f"\nLa reserva se efectuo correctamente bajo el nombre de {nombre} para la fecha {escritura_digitos(dia)}/{escritura_digitos(mes)}/{escritura_digitos(año)}, empezara a las {escritura_digitos(hora)}:{escritura_digitos(minuto)} hs y finalizara a las {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs")

        reserva = {
            'nombre':nombre,
            'dia':dia,
            'mes':mes,
            'año':año,
            'hora':hora,
            'minuto':minuto,
            'duracion':duracion,
            'estacionamiento':sel
        }
        reservar.append(reserva)

        guardar_datos_json(RESER_JSON, reservar)

        indice = len(reservar) - 1

        nombre_archivo = 'recibos.txt'
        if len(reservar) == 2:
            generar_archivo(nombre_archivo, reservar, EST_JSON, sel, indice)
        else: 
            escribir_archivo(nombre_archivo, reservar, EST_JSON, sel, indice)

def mostrar_lista_reservas(lista):
    print(f'{"Índice":<8} | {"Nombre":<15} | {"Día":<5} | {"Mes":<5} | {"Año":<6} | {"Hora":<6} | {"Minuto":<8} | {"Duración":<10} | {"Estacionamiento":<15}')
    print("-" * 120)
    
    for i in range(1, len(lista)):
        print(f'{i:<8} | '
              f'{lista[i]["nombre"]:<15} | '
              f'{escritura_digitos(lista[i]["dia"]):<5} | '
              f'{escritura_digitos(lista[i]["mes"]):<5} | '
              f'{escritura_digitos(lista[i]["año"]):<6} | '
              f'{escritura_digitos(lista[i]["hora"]):<6} | '
              f'{escritura_digitos(lista[i]["minuto"]):<8} | '
              f'{escritura_digitos(lista[i]["duracion"]):<10} | '
              f'{lista[i]["estacionamiento"]:<15}')

def consultar_reservas(lista_reservas):
    print("\n" + "=" * 44)
    print("\n CONSULTAR RESERVAS \n")
    print("=" * 44)
    mostrar_lista_reservas(lista_reservas)
    input("\nPresione ENTER para volver...")

def modificar_reserva(sel, EST_JSON, RESER_JSON, reservar):
    print("\n--- RESERVAS EXISTENTES ---")
    mostrar_lista_reservas(reservar)

    reserva_num = pedir_numero("\nSeleccione el número de la reserva que desea modificar: ")

    while reserva_num < 1 or reserva_num >= len(reservar):
        print("Opción fuera de rango. Reingrese.")
        reserva_num = pedir_numero(f"Seleccione un número entre 1 y {len(reservar) - 1}: ")

    _, horaduracion = contar_duracion(reservar[reserva_num]['duracion'], reservar[reserva_num]['hora'])

    nombre = reservar[reserva_num]['nombre']
    dia = reservar[reserva_num]['dia']
    mes = reservar[reserva_num]['mes']
    año = reservar[reserva_num]['año'] 
    hora = reservar[reserva_num]['hora']
    minuto = reservar[reserva_num]['minuto'] 
    duracion = reservar[reserva_num]['duracion']
    control = "N"
    
    while control.lower() not in ("y", "yes","si"):
        print("\n" + "=" * 44)
        print(f"MODIFICANDO RESERVA DE: {nombre}")
        print("=" * 44)
        print(f"Fecha: {escritura_digitos(dia)}-{escritura_digitos(mes)}-{escritura_digitos(año)}")
        print(f"Horario: {escritura_digitos(hora)}:{escritura_digitos(minuto)} hs a {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs (Duración: {escritura_digitos(duracion)} hs)")

        cambio = pedir_numero("\n¿Qué dato desea modificar?\n"
                           f"[1. Nombre ({nombre}) / "
                           f"2. Día ({escritura_digitos(dia)}) / "
                           f"3. Mes ({escritura_digitos(mes)}) / "
                           f"4. Año ({escritura_digitos(año)}) / "
                           f"5. Hora ({escritura_digitos(hora)}) / "
                           f"6. Minuto ({escritura_digitos(minuto)}) / "
                           f"7. Duración ({escritura_digitos(duracion)})]: ")

        match cambio:
            case 1:
                nombre = pedir_nombre("Ingrese el nuevo nombre: ")
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

    reservar[reserva_num] = {
        'nombre':nombre,
        'dia':dia,
        'mes':mes,
        'año':año,
        'hora':hora,
        'minuto':minuto,
        'duracion':duracion,
        'estacionamiento':sel
    }

    guardar_datos_json(RESER_JSON, reservar)
    escribir_archivo("recibos.txt", reservar, EST_JSON, sel, reserva_num)
    
    print("\n¡La reserva fue actualizada exitosamente!")
    input("\nPresione ENTER para continuar...")

def cancelar_reserva(sel, EST_JSON, RESER_JSON, RESER_CANCEL_JSON, reservas_canceladas, reservar):
    print("\n--- RESERVAS EXISTENTES ---")
    mostrar_lista_reservas(reservar)

    reserva_num = pedir_numero("\nSeleccione el número de la reserva que desea cancelar: ")

    while reserva_num < 1 or reserva_num >= len(reservar):
        print("Opción fuera de rango. Reingrese. ")
        reserva_num = pedir_numero(f"Seleccione un número entre 1 y {len(reservar) - 1}: ")

    _, horaduracion = contar_duracion(reservar[reserva_num]['duracion'], reservar[reserva_num]['hora'])
    
    nombre = reservar[reserva_num]['nombre']
    dia = reservar[reserva_num]['dia']
    mes = reservar[reserva_num]['mes']
    año = reservar[reserva_num]['año'] 
    hora = reservar[reserva_num]['hora']
    minuto = reservar[reserva_num]['minuto'] 
    duracion = reservar[reserva_num]['duracion']

    print("\n" + "=" * 44)
    print(f"CANCELAR RESERVA DE: {nombre}")
    print("=" * 44)
    print(f"Fecha: {escritura_digitos(dia)}-{escritura_digitos(mes)}-{escritura_digitos(año)}")
    print(f"Horario: {escritura_digitos(hora)}:{escritura_digitos(minuto)} hs a {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs (Duración: {escritura_digitos(duracion)} hs)")

    confirmacion_cancelar = input("¿Esta seguro de que desea cancelar esta reserva?, [Y / N]: ") 

    if confirmacion_cancelar.lower() in ("y", "yes", "si"):
        reservas_canceladas.append(reservar[reserva_num])
        del reservar[reserva_num]

        guardar_datos_json(RESER_JSON, reservar)
        guardar_datos_json(RESER_CANCEL_JSON, reservas_canceladas)
        
        if EST_JSON[sel]['capacidad_actual'] < EST_JSON[sel]["capacidad_total"]:
            EST_JSON[sel]['capacidad_actual'] += 1
            
        print("Reserva cancelada exitosamente.")
        input("\nPresione ENTER para continuar...")

def recuperar_reserva(sel, EST_JSON, RESER_JSON, RESER_CANCEL_JSON, reservas_canceladas, reservar):
    print("\n--- RESERVAS CANCELADAS ---")
    mostrar_lista_reservas(reservas_canceladas)

    reserva_num = pedir_numero("\nSeleccione el número de la reserva que desea recuperar: ")

    while reserva_num < 1 or reserva_num >= len(reservas_canceladas):
        print("Opción fuera de rango. Reingrese. ")
        reserva_num = pedir_numero(f"Seleccione un número entre 1 y {len(reservas_canceladas) - 1}: ")

    _, horaduracion = contar_duracion(reservas_canceladas[reserva_num]['duracion'], reservas_canceladas[reserva_num]['hora'])

    print("\n" + "=" * 44)
    print(f"RECUPERAR RESERVA DE: {reservas_canceladas[reserva_num]['nombre']}")
    print("=" * 44)
    print(f"Fecha: {escritura_digitos(reservas_canceladas[reserva_num]['dia'])}-{escritura_digitos(reservas_canceladas[reserva_num]['mes'])}-{escritura_digitos(reservas_canceladas[reserva_num]['año'])}")
    print(f"Horario: {escritura_digitos(reservas_canceladas[reserva_num]['hora'])}:{escritura_digitos(reservas_canceladas[reserva_num]['minuto'])} hs a {escritura_digitos(horaduracion)}:{escritura_digitos(reservas_canceladas[reserva_num]['minuto'])} hs (Duración: {reservas_canceladas[reserva_num]['duracion']} hs)")

    confirmacion_recuperar = input("¿Esta seguro de que desea recuperar esta reserva?, [Y / N]: ") 

    if confirmacion_recuperar.lower() in ("y", "yes", "si"):
        if EST_JSON[sel]['capacidad_actual'] <= 0:
            print("\nNo hay espacios disponibles en este estacionamiento.")
            return
        
        EST_JSON[sel]['capacidad_actual'] -= 1

        reservar.append(reservas_canceladas[reserva_num])
        del reservas_canceladas[reserva_num]

        guardar_datos_json(RESER_CANCEL_JSON, reservas_canceladas)
        guardar_datos_json(RESER_JSON, reservar)
        
        escribir_archivo("recibos.txt", reservar, EST_JSON, sel, len(reservar) - 1)
            
        print("Reserva recuperada exitosamente.")
        input("\nPresione ENTER para continuar...")
