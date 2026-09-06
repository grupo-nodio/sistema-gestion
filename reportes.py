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