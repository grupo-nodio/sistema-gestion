'''
1. Reportes de Usuarios (Marketing y Fidelización)
    Generador de Mailing (Marketing): Un reporte que extraiga únicamente los correos electrónicos de los usuarios que están Activos ("A"). Sirve para enviarles promociones.
    Concepto a usar: Comprensión de listas con condición o filter() + map().  Ejemplo: emails_activos = [lst_email[i] for i in range(len(lst_dni)) if lst_estado[i] == "A"].  
    
    Tasa de Retención (Auditoría): Calcular qué porcentaje de los usuarios registrados históricos siguen activos versus los que se dieron de baja.
    Concepto a usar: reduce() para contar y una simple regla de tres.  
'''

#Reportes de Vehículos (Logística de Espacios)
def reporte_vehiculos_por_tipo(lista_tipo):
    if len(lista_tipo) == 0:
        print("No hay vehículos registrados.")
    else:
        motos = len(list(filter(lambda x: x == "moto" or x == "Moto" or x == "MOTO", lista_tipo)))
        autos = len(list(filter(lambda x: x == "auto" or x == "Auto" or x == "AUTO", lista_tipo)))
        camionetas = len(list(filter(lambda x: x == "camioneta" or x == "Camioneta" or x == "CAMIONETA", lista_tipo)))

        print("ANALISIS DE VEHÍCULOS POR TIPO:")
        print("Cantidad de motos:", motos)
        print("Cantidad de autos:", autos)
        print("Cantidad de camionetas:", camionetas)

#Buscador por patente
def reporte_ocupacion_estacionamiento(lista_tipo):
    if len(lista_tipo) == 0:
        print("No hay vehículos registrados.")
    else:
        espacios_grandes = len(list(filter(lambda x: x == "camioneta" or x == "Camioneta" or x == "CAMIONETA", lista_tipo)))
        espacios_estandar = len(list(filter(lambda x: x == "auto" or x == "Auto" or x == "AUTO" or x == "moto" or x == "Moto" or x == "MOTO", lista_tipo)))

        print("ANALISIS DE OCUPACION DEL ESTACIONAMIENTO:")
        print("Cantidad de espacios grandes ocupados (camionetas):", espacios_grandes)
        print("Cantidad de espacios estándar ocupados (autos y motos):", espacios_estandar)






'''
3. Reportes Avanzados de Datos (Limpieza y Regex)
    Auditoría de Procedencia por Teléfono: Agrupar a los usuarios según su código de área telefónico (por ejemplo, los que empiezan con "11" de Buenos Aires u otros prefijos). Sirve para saber de dónde vienen tus clientes.
    Concepto a usar: Expresiones regulares (re.match(r"^11\d{8}$", telefono)) combinadas con un filtro.  
    
    Análisis de Dominios de Email: Extraer qué plataformas de correo usan más tus clientes (gmail.com, hotmail.com, etc.).
    Concepto a usar: re.findall(r"@[\w.-]+", email) para capturar solo la parte del dominio y luego usar funciones de agregación (count()) para saber cuál es el más popular.  
    
¿Cómo estructurarlo?
En tu archivo reportes.py, podrías crear un menú propio (usando match en lugar de if-elif) que se llame desde la opción de estadísticas del main.py. A este módulo simplemente le pasarías todas las listas por parámetro (reportes.menu_reportes(nombres, emails, estados, patentes, tipos)).  
'''