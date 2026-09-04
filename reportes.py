<<<<<<< HEAD
from estacionamiento import elegir_estacionamiento, mostrar_estacionamientos
import re

def escritura_digitos(A):
    if A < 10:
        A = "0" + str(A)
    else:
        A = str(A)
    return A

def validar_fecha(dia, mes, año):
    fecha = False
    while fecha != True:
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

        if fecha != True:
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
    while tiempo != True:
        tiempo = True
        if hora < 0 or hora > 23:
            hora = 0
            tiempo = False
        
        if minuto not in [0, 30]:
            minuto = 1
            tiempo = False

        if tiempo != True:
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

    # Seleccionar estacionamiento usando la función importada
    espacio = elegir_estacionamiento(estacionamientos)
    nombre_lugar = estacionamientos[0][espacio]

    print("=" * 44)
    print("\n CONTROL DE RESERVA \n")
    print("=" * 44)
    print(f"Lugar seleccionado: {nombre_lugar}")
    print("\n En la fecha DD - MM - YYYY: ", escritura_digitos(dia), "-", escritura_digitos(mes), "-", escritura_digitos(año))
    print(f"la reserva comenzara a las: {escritura_digitos(hora)} : {escritura_digitos(minuto)} y durara hasta las: {escritura_digitos(horaduracion)} : {escritura_digitos(minuto)} hs")

    control = input("\nVerifique si los datos tomados son los correctos [Y / N]: ")

    if control not in ["Y", "y", "yes", "Yes", "si", "Si"]:
        while control not in ["Y", "y", "yes", "Yes", "si", "Si"]:
            cambio = int(input(f"¿Cual de los siguientes datos desea modificar?, [1. {escritura_digitos(dia)} / 2. {escritura_digitos(mes)} / 3. {escritura_digitos(año)} / 4. {escritura_digitos(hora)} / 5. {escritura_digitos(minuto)} / 6. {duracion}]: "))
            if cambio == 1:
                dia = modificar_datos(dia)
                dia, mes, año = validar_fecha(dia, mes, año)
            elif cambio == 2:
                mes = modificar_datos(mes)
                dia, mes, año = validar_fecha(dia, mes, año)
            elif cambio == 3:
                año = modificar_datos(año)
                dia, mes, año = validar_fecha(dia, mes, año)
            elif cambio == 4:
                hora = modificar_datos(hora)
                hora, minuto = validar_hora(hora, minuto)
                duracion, horaduracion = contar_duracion(duracion, hora)
            elif cambio == 5:
                minuto = modificar_datos(minuto)
                hora, minuto = validar_hora(hora, minuto)
            elif cambio == 6:
                duracion = modificar_datos(duracion)
                duracion, horaduracion = contar_duracion(duracion, hora)

            print("=" * 44)
            print("\n CONTROL DE RESERVA \n")
            print("=" * 44)
            print("En la fecha DD - MM - YYYY: ", escritura_digitos(dia), "-", escritura_digitos(mes), "-", escritura_digitos(año))
            print(f"la reserva comenzara a las: {escritura_digitos(hora)} : {escritura_digitos(minuto)} hs y durara hasta las: {escritura_digitos(horaduracion)} : {escritura_digitos(minuto)} hs")
            control = input("\nVerifique si los datos tomados son los correctos [Y / N]:  ")

    if control in ["Y", "y", "yes", "Yes", "si", "Si"]:
        nombre = input("Ingrese el nombre bajo el cual estara la reserva: ")
        print(f"La reserva se efectuo correctamente en '{nombre_lugar}', bajo el nombre de {nombre} para la fecha {dia}/{mes}/{año}, empezara a las {hora}:{minuto} hs y finalizara a las {escritura_digitos(horaduracion)}:{escritura_digitos(minuto)} hs")

def menu_reservas(estacionamientos):
    print("=" * 44)
    print("\n------------BIENVENIDO A RESERVAS------------\n")
    print("=" * 44)
    print("\n------------MENU RESERVAS------------\n")

    opcion = int(input("Seleccione la opcion que desea realizar. [1. Generar una reserva / 2. Consultar reservas / 3. Modificar reserva / 4. Cancelar una reserva.] : "))

    if opcion == 1:
        generar_reserva(estacionamientos)

# --------------- programa principal ------------

# 1. Primero se declaran las estructuras de datos
estacionamientos = [
    [None, "Parking del sol", "Estacione Recoleta"],  # 0 Nombre
    [None, 1, 2],                                      # 1 Estado
    [None, "Av. 123", "Calle 123"],                    # 2 Dirección
    [None, 100, 24]                                    # 3 Espacios
]

horarios = [
    None,
    [
        ["07:00", "20:00"], ["07:00", "20:00"], ["07:00", "20:00"],
        ["07:00", "20:00"], ["07:00", "20:00"], ["08:00", "18:00"], False
    ],
    [True, True, True, True, True, True, True]
]

# 2. Luego se inicia la ejecución del programa
menu_reservas(estacionamientos)
=======
'''
1. Reportes de Usuarios (Marketing y Fidelización)
    Generador de Mailing (Marketing): Un reporte que extraiga únicamente los correos electrónicos de los usuarios que están Activos ("A"). Sirve para enviarles promociones.
    Concepto a usar: Comprensión de listas con condición o filter() + map().  Ejemplo: emails_activos = [lst_email[i] for i in range(len(lst_dni)) if lst_estado[i] == "A"].  
    
    Tasa de Retención (Auditoría): Calcular qué porcentaje de los usuarios registrados históricos siguen activos versus los que se dieron de baja.
    Concepto a usar: reduce() para contar y una simple regla de tres.  
    
2. Reportes de Vehículos (Logística de Espacios)
    Análisis de Flota por Tipo: Contar cuántos vehículos de cada tipo (Auto, Moto, Camioneta) hay registrados. Esto le sirve al dueño para saber si necesita pintar más espacios chicos para motos o espacios grandes para camionetas.
    Concepto a usar: filter() y len(). Por ejemplo, filtrar la lista de tipos donde el elemento coincida (sin distinguir mayúsculas) con la palabra "Moto" y medir el largo de la lista resultante.  
    
    Buscador Rápido por Patente: Un reporte donde el administrador escriba los primeros 3 números o letras de una patente y el sistema devuelva todos los vehículos que coincidan.
    Concepto a usar: re.search() o re.match() para verificar coincidencias parciales de cadenas dentro de un bucle o un filter().  
    
3. Reportes Avanzados de Datos (Limpieza y Regex)
    Auditoría de Procedencia por Teléfono: Agrupar a los usuarios según su código de área telefónico (por ejemplo, los que empiezan con "11" de Buenos Aires u otros prefijos). Sirve para saber de dónde vienen tus clientes.
    Concepto a usar: Expresiones regulares (re.match(r"^11\d{8}$", telefono)) combinadas con un filtro.  
    
    Análisis de Dominios de Email: Extraer qué plataformas de correo usan más tus clientes (gmail.com, hotmail.com, etc.).
    Concepto a usar: re.findall(r"@[\w.-]+", email) para capturar solo la parte del dominio y luego usar funciones de agregación (count()) para saber cuál es el más popular.  
    
¿Cómo estructurarlo?
En tu archivo reportes.py, podrías crear un menú propio (usando match en lugar de if-elif) que se llame desde la opción de estadísticas del main.py. A este módulo simplemente le pasarías todas las listas por parámetro (reportes.menu_reportes(nombres, emails, estados, patentes, tipos)).  
'''
>>>>>>> 855d73533701374d8254c2e4a28a085beaf65d7b
