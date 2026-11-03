import json

tarifas_por_hora = {"moto": 2500, "auto": 4000, "camioneta": 6000}
escala_descuentos = ((24, 20), (12, 10))

campos_cobro = ("numero", "estacionamiento", "patente", "tipo", "dni", "ingreso", "egreso", "minutos", "horas", "subtotal", "descuento", "total")
campos_numericos = ("numero", "minutos", "horas", "subtotal", "descuento", "total")

minutos_por_hora = 60
minutos_por_dia = 1440
dias_maximos = 365

archivo_cobros = "cobros.json"
archivo_registro = "registro_cobros.txt"
separador = "|"

respuestas_si = ("s", "si", "sí", "y", "yes")
respuestas_no = ("n", "no")

def a_minusculas(texto):
    resultado = ""
    for letra in texto:
        if "A" <= letra <= "Z":
            resultado += chr(ord(letra) + 32)
        else:
            resultado += letra
    return resultado

def a_mayusculas(texto):
    resultado = ""
    for letra in texto:
        if "a" <= letra <= "z":
            resultado += chr(ord(letra) - 32)
        else:
            resultado += letra
    return resultado

def convertir_hora_a_minutos(hora):
    if len(hora) != 5 or hora[2] != ":":
        print("Error: Formato de hora inválido. Use HH:MM con dos dígitos (ejemplo: 08:30).")
        return -1
    
    try:
        horas = int(hora[0:2])
        minutos = int(hora[3:5])
    except ValueError:
        print("Error: La hora debe contener números.")
        return -1

    if horas > 23 or minutos > 59:
        print("Error: Hora fuera de rango. Las horas van de 00 a 23 y los minutos de 00 a 59.")
        return -1

    return horas * minutos_por_hora + minutos

def calcular_minutos_estadia(ingreso, egreso, dias=0):
    if dias < 0 or dias > dias_maximos:
        print(f"Error: Los días deben ser un número entero entre 0 y {dias_maximos}.")
        return -1
    
    min_egreso = convertir_hora_a_minutos(egreso)
    min_ingreso = convertir_hora_a_minutos(ingreso)
    
    if min_egreso == -1 or min_ingreso == -1:
        return -1

    minutos = (dias * minutos_por_dia + min_egreso - min_ingreso)
    if minutos <= 0:
        print("Error: El egreso debe ser posterior al ingreso.")
        return -1
    return minutos

def calcular_horas_a_cobrar(minutos):
    if minutos <= 0:
        print("Error: La permanencia debe ser un número entero de minutos mayor a 0.")
        return -1

    horas = minutos // minutos_por_hora
    resto = minutos % minutos_por_hora
    
    if resto > 0:
        horas += 1
    return horas

def obtener_porcentaje_descuento(horas):
    for tupla in escala_descuentos:
        if horas >= tupla[0]:
            return tupla[1]
    return 0

def calcular_costo(horas, tipo_vehiculo):
    tipo = a_minusculas(tipo_vehiculo.replace(" ", ""))
    
    if tipo not in tarifas_por_hora:
        print(f"Error: No existe una tarifa para el tipo de vehículo '{tipo_vehiculo}'.")
        return -1, -1, -1
    if horas <= 0:
        print("Error: Las horas a cobrar deben ser un número entero mayor a 0.")
        return -1, -1, -1

    subtotal = horas * tarifas_por_hora[tipo]
    descuento = subtotal * obtener_porcentaje_descuento(horas) // 100
    total = subtotal - descuento
    return subtotal, descuento, total

def formatear_pesos(monto):
    return "$" + f"{monto:,}".replace(",", ".")

def formatear_duracion(minutos):
    horas = minutos // minutos_por_hora
    resto = minutos % minutos_por_hora
    
    if resto < 10:
        return f"{horas} h 0{resto} min"
    return f"{horas} h {resto} min"

def buscar_vehiculo(patente, lista_patentes, lista_tipos, lista_dnis):
    if patente not in lista_patentes:
        print(f"Error: La patente {patente} no está registrada en el sistema.")
        return None

    posicion = lista_patentes.index(patente)
    return patente, lista_tipos[posicion], lista_dnis[posicion]

def proximo_numero(cobros):
    mayor = 0
    for cobro in cobros:
        if cobro["numero"] > mayor:
            mayor = cobro["numero"]
    
    if mayor == 0:
        return 1
    return mayor + 1

def crear_cobro(numero, nombre_estacionamiento, vehiculo, estadia, importes):
    patente, tipo, dni = vehiculo
    ingreso, egreso, minutos, horas = estadia
    subtotal, descuento, total = importes

    return {
        "numero": numero,
        "estacionamiento": nombre_estacionamiento,
        "patente": patente,
        "tipo": tipo,
        "dni": dni,
        "ingreso": ingreso,
        "egreso": egreso,
        "minutos": minutos,
        "horas": horas,
        "subtotal": subtotal,
        "descuento": descuento,
        "total": total,
    }

def cobro_a_linea(cobro):
    linea = ""
    for i in range(len(campos_cobro)):
        campo = campos_cobro[i]
        linea += f"{cobro[campo]}"
        if i < len(campos_cobro) - 1:
            linea += separador
    return linea

def linea_a_cobro(linea):
    linea_limpia = linea.replace("\n", "")
    partes = []
    palabra = ""
    
    for letra in linea_limpia:
        if letra == separador:
            partes.append(palabra)
            palabra = ""
        else:
            palabra += letra
    partes.append(palabra)
    
    if len(partes) != len(campos_cobro):
        print("La línea no tiene la cantidad de campos esperada.")
        return None

    cobro = {}
    for i in range(len(campos_cobro)):
        cobro[campos_cobro[i]] = partes[i]

    for campo in campos_numericos:
        try:
            cobro[campo] = int(cobro[campo])
        except ValueError:
            return None
            
    return cobro

def agregar_al_registro(cobro, ruta=archivo_registro):
    try:
        with open(ruta, "a") as archivo:
            archivo.write(cobro_a_linea(cobro) + "\n")
        return True
    except OSError as error:
        print(f"Error: no se pudo escribir en {ruta} ({error}).")
        return False

def leer_registro(ruta=archivo_registro):
    try:
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        return []
    except OSError as error:
        print(f"Error: no se pudo leer {ruta} ({error}).")
        return []

    cobros = []
    omitidas = 0
    for linea in lineas:
        if linea.replace("\n", "").replace(" ", "") != "":
            nuevo_cobro = linea_a_cobro(linea)
            if nuevo_cobro != None:
                cobros.append(nuevo_cobro)
            else:
                omitidas += 1

    if omitidas > 0:
        print(f"Aviso: se omitieron {omitidas} líneas dañadas de {ruta}.")
    return cobros

def guardar_cobros(cobros, ruta=archivo_cobros):
    try:
        with open(ruta, "w") as archivo:
            json.dump(cobros, archivo, indent=4, ensure_ascii=False)
        return True
    except OSError as error:
        print(f"Error: no se pudo guardar {ruta} ({error}).")
        return False

def cargar_cobros(ruta_json=archivo_cobros, ruta_registro=archivo_registro):
    cobros = leer_registro(ruta_registro)
    
    if len(cobros) > 0:
        guardar_cobros(cobros, ruta_json)
        
    return cobros

def registrar_cobro(cobros, cobro, ruta_json=archivo_cobros, ruta_registro=archivo_registro):
    cobros.append(cobro)
    guardado_en_texto = agregar_al_registro(cobro, ruta_registro)
    guardado_en_json = guardar_cobros(cobros, ruta_json)
    return guardado_en_texto and guardado_en_json

def filtrar_cobros(cobros, nombre_estacionamiento):
    filtrados = []
    for cobro in cobros:
        if cobro["estacionamiento"] == nombre_estacionamiento:
            filtrados.append(cobro)
    return filtrados

def pedir_texto(mensaje):
    texto = input(mensaje)
    while texto == "" or texto == " ":
        print("Error: este dato es obligatorio.")
        texto = input(mensaje)
    return texto

def pedir_entero(mensaje, minimo, maximo):
    while True:
        texto = pedir_texto(mensaje)
        try:
            numero = int(texto)
            if numero < minimo or numero > maximo:
                print(f"Error: el valor debe estar entre {minimo} y {maximo}.")
            else:
                return numero
        except ValueError:
            print("Error: debe ingresar un número entero.")

def pedir_hora(mensaje):
    while True:
        texto = pedir_texto(mensaje)
        if texto == "0":
            return None
            
        resultado = convertir_hora_a_minutos(texto)
        if resultado != -1:
            return texto

def pedir_vehiculo(lista_patentes, lista_tipos, lista_dnis):
    print("Escriba '0' si desea cancelar y volver al menú.")
    while True:
        patente = a_mayusculas(pedir_texto("Ingrese la patente del vehículo a cobrar: "))
        if patente == "0":
            return None
            
        vehiculo = buscar_vehiculo(patente, lista_patentes, lista_tipos, lista_dnis)
        if vehiculo != None:
            return vehiculo

def pedir_estadia():
    while True:
        ingreso = pedir_hora("Hora de ingreso (HH:MM, 0 para cancelar): ")
        if ingreso == None:
            return None

        egreso = pedir_hora("Hora de egreso (HH:MM, 0 para cancelar): ")
        if egreso == None:
            return None

        dias = pedir_entero("Días transcurridos entre ingreso y egreso (0 = mismo día): ", 0, dias_maximos)
        minutos = calcular_minutos_estadia(ingreso, egreso, dias)
        
        if minutos != -1:
            return ingreso, egreso, minutos
            
        print("Vuelva a ingresar los datos de la estadía.")

def confirmar(mensaje):
    respuesta = a_minusculas(input(mensaje).replace(" ", ""))
    while respuesta not in respuestas_si and respuesta not in respuestas_no: 
        respuesta = a_minusculas(input("Error: responda con s (sí) o n (no): ").replace(" ", ""))
    return respuesta in respuestas_si

def imprimir_campo(etiqueta, valor):
    print(f" {etiqueta:<16}: {valor}")

def imprimir_descuento(horas, descuento):
    porcentaje = obtener_porcentaje_descuento(horas)
    if porcentaje > 0:
        imprimir_campo(f"Descuento {porcentaje}%", "-" + formatear_pesos(descuento))
    else:
        imprimir_campo("Descuento", "no corresponde")

def mostrar_ticket(cobro):
    linea = "=" * 52

    print("\n" + linea)
    print(f" COMPROBANTE DE COBRO N° {cobro['numero']:04d}")
    print(linea)
    imprimir_campo("Estacionamiento", cobro["estacionamiento"])
    imprimir_campo("Vehículo", f"{cobro['tipo']} - patente {cobro['patente']}")
    imprimir_campo("DNI propietario", cobro["dni"])
    imprimir_campo("Ingreso", cobro["ingreso"])
    imprimir_campo("Egreso", cobro["egreso"])
    imprimir_campo("Permanencia", formatear_duracion(cobro["minutos"]))
    imprimir_campo("Horas a cobrar", f"{cobro['horas']} (por hora o fracción)")
    imprimir_campo("Subtotal", formatear_pesos(cobro["subtotal"]))
    imprimir_descuento(cobro["horas"], cobro["descuento"])
    print("-" * 52)
    imprimir_campo("TOTAL A PAGAR", formatear_pesos(cobro["total"]))
    print(linea)

def cobrar_estacionamiento(nombre_estacionamiento, lista_patentes, lista_tipos, lista_dnis):
    print("\n--- COBRO DE ESTACIONAMIENTO ---")
    
    cobros = cargar_cobros()

    if len(lista_patentes) == 0:
        print("No hay vehículos registrados en el sistema para cobrar.")
        return None

    vehiculo = pedir_vehiculo(lista_patentes, lista_tipos, lista_dnis)
    if vehiculo == None:
        print("Cobro cancelado. Volviendo al menú.")
        return None

    patente, tipo, dni = vehiculo
    print(f"Vehículo encontrado: {tipo} con patente {patente} (DNI propietario: {dni})")

    if tipo not in tarifas_por_hora:
        print(f"Error: el vehículo {patente} tiene un tipo sin tarifa ({tipo}). No se puede cobrar.")
        return None

    estadia = pedir_estadia()
    if estadia == None:
        print("Cobro cancelado. Volviendo al menú.")
        return None

    ingreso, egreso, minutos = estadia
    horas = calcular_horas_a_cobrar(minutos)
    importes = calcular_costo(horas, tipo)

    cobro = crear_cobro(proximo_numero(cobros), nombre_estacionamiento, vehiculo,
                        (ingreso, egreso, minutos, horas), importes)
    mostrar_ticket(cobro)

    if not confirmar("¿Confirmar el cobro? (s/n): "):
        print("Cobro cancelado. No se registró ningún importe.")
        return None

    if registrar_cobro(cobros, cobro):
        print("Cobro registrado correctamente.")
    else:
        print("Aviso: el cobro quedó registrado en memoria, pero no pudo guardarse en disco.")
    return cobro

def mostrar_cobros(nombre_estacionamiento):
    cobros_totales = cargar_cobros()
    cobros = filtrar_cobros(cobros_totales, nombre_estacionamiento)
    
    print(f"\n--- HISTORIAL DE COBROS ({nombre_estacionamiento}) ---")
    if len(cobros) == 0:
        print("No hay cobros registrados en este estacionamiento.")
        return

    print(f"{'N°':<7}{'Patente':<10}{'Tipo':<11}{'Permanencia':<13}{'Horas':>6}{'Total':>13}")
    print("-" * 60)
    for cobro in cobros:
        numero = f"{cobro['numero']:04d}"
        permanencia = formatear_duracion(cobro["minutos"])
        total = formatear_pesos(cobro["total"])
        print(f"{numero:<7}{cobro['patente']:<10}{cobro['tipo']:<11}{permanencia:<13}"
              f"{cobro['horas']:>6}{total:>13}")
