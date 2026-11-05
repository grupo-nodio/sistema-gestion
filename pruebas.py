import re

from estacionamiento import (
    ver_estado,
    validar_cierre,
    validar_horario
)
from usuarios import (
    formato_usuarios_valido,
    validar_nombre,
    validar_email,
    validar_dni,
    formatear_usuario,
)
from vehiculos import (
    cargar_vehiculosjson,
    guardar_vehiculosjson,
)
from reservas import (
    escritura_digitos,
    contar_duracion,
    validar_fecha,
    validar_hora,
    cargar_datos_json,
    guardar_datos_json
)
from tarifas import (
    convertir_hora_a_minutos,
    calcular_minutos_estadia,
    calcular_costo
)

# ==============================================================================
# 1. PRUEBAS PARA: ESTACIONAMIENTOS
# ==============================================================================

def prueba_ver_estado_valido():
    # Caso Válido: Estado 1 devuelve "disponible"
    estacionamientos_test = {1: {"estado": 1}}
    resultado = ver_estado(1, estacionamientos_test)
    if resultado == "disponible":
        print("Prueba ver_estado (Válido): Correcta")
    else:
        print("Error en prueba ver_estado (Válido)")

def prueba_ver_estado_invalido():
    # Caso Inválido: Comprobar que ante un estado ocupado (2) NO devuelva "disponible"
    estacionamientos_test = {1: {"estado": 2}}
    resultado = ver_estado(1, estacionamientos_test)
    if resultado != "disponible":
        print("Prueba ver_estado (Inválido): Correcta")
    else:
        print("Error en prueba ver_estado (Inválido)")

def prueba_ver_estado_limite():
    # Caso Límite: Probar el último estado permitido en las opciones (3 = fuera de servicio)
    estacionamientos_test = {1: {"estado": 3}}
    resultado = ver_estado(1, estacionamientos_test)
    if resultado == "fuera de servicio":
        print("Prueba ver_estado (Límite): Correcta")
    else:
        print("Error en prueba ver_estado (Límite)")


def prueba_validar_cierre_valido():
    # Caso Válido: Hora de cierre posterior a la apertura
    resultado = validar_cierre("08:00", "18:00")
    if resultado == True:
        print("Prueba validar_cierre (Válido): Correcta")
    else:
        print("Error en prueba validar_cierre (Válido)")

def prueba_validar_cierre_invalido():
    # Caso Inválido: Hora de cierre anterior a la apertura
    resultado = validar_cierre("18:00", "08:00")
    if resultado == False:
        print("Prueba validar_cierre (Inválido): Correcta")
    else:
        print("Error en prueba validar_cierre (Inválido)")

def prueba_validar_cierre_limite():
    # Caso Límite: Hora de apertura y cierre idénticas (0 minutos de margen)
    resultado = validar_cierre("08:00", "08:00")
    if resultado == False:
        print("Prueba validar_cierre (Límite): Correcta")
    else:
        print("Error en prueba validar_cierre (Límite)")


def prueba_validar_horario_valido():
    # Caso Válido: Hora dentro de rango y minutos en 00 o 30
    resultado = validar_horario("14:30")
    if resultado == True:
        print("Prueba validar_horario (Válido): Correcta")
    else:
        print("Error en prueba validar_horario (Válido)")

def prueba_validar_horario_invalido():
    # Caso Inválido: Minutos no permitidos (ej. 15 minutos)
    resultado = validar_horario("14:15")
    if resultado == False:
        print("Prueba validar_horario (Inválido): Correcta")
    else:
        print("Error en prueba validar_horario (Inválido)")

def prueba_validar_horario_limite():
    # Caso Límite: Último horario permitido del día (23:30)
    resultado = validar_horario("23:30")
    if resultado == True:
        print("Prueba validar_horario (Límite): Correcta")
    else:
        print("Error en prueba validar_horario (Límite)")


# ============================================================================== 
# 2. PRUEBAS PARA: USUARIOS
# ============================================================================== 

def prueba_validar_nombre():
    if validar_nombre("María José") and not validar_nombre("María2") and validar_nombre("Ana-María"):
        print("Prueba validar_nombre: Correcta")
    else:
        print("Error en prueba validar_nombre")

def prueba_validar_email():
    if validar_email("ana.perez@example.com") and not validar_email("ana@"):
        print("Prueba validar_email: Correcta")
    else:
        print("Error en prueba validar_email")

def prueba_validar_dni():
    if validar_dni("12345678") and not validar_dni("1234567") and not validar_dni("1234567A"):
        print("Prueba validar_dni: Correcta")
    else:
        print("Error en prueba validar_dni")

def prueba_formato_usuarios_valido():
    usuario = {"12345678": {
        "nombre": "Ana", "apellido": "Pérez", "email": "ana@example.com",
        "telefono": "1112345678", "estado": "A",
    }}
    if formato_usuarios_valido(usuario):
        print("Prueba formato_usuarios_valido (Válido): Correcta")
    else:
        print("Error en prueba formato_usuarios_valido (Válido)")

def prueba_formato_usuarios_invalido():
    usuario_incompleto = {"12345678": {"nombre": "Ana"}}
    if not formato_usuarios_valido(usuario_incompleto) and not formato_usuarios_valido([]):
        print("Prueba formato_usuarios_valido (Inválido): Correcta")
    else:
        print("Error en prueba formato_usuarios_valido (Inválido)")

def prueba_formatear_usuario():
    usuario = ("12345678", {
        "nombre": "Ana", "apellido": "Pérez", "email": "ana@example.com",
        "telefono": "1112345678", "estado": "A",
    })
    resultado = formatear_usuario(usuario)
    if all(dato in resultado for dato in ("Ana", "Pérez", "12345678", "ana@example.com", "1112345678", "A")):
        print("Prueba formatear_usuario: Correcta")
    else:
        print("Error en prueba formatear_usuario")


# ==============================================================================
# 3. PRUEBAS PARA: VEHÍCULOS
# ==============================================================================

def prueba_validar_patente_valida():
    # Caso Válido: Formato nuevo de patente (ej. AB123CD)
    patente_test = "AB123CD"
    coincidencia = re.match(r'^([A-Za-z]{2}\d{3}[A-Za-z]{2}|[A-Za-z]{3}\d{3}|[A-Za-z]{3}\d{4})$', patente_test)
    if coincidencia != None:
        print("Prueba validar_patente (Válido): Correcta")
    else:
        print("Error en prueba validar_patente (Válido)")

def prueba_validar_patente_invalida():
    # Caso Inválido: Formato incorrecto con guiones
    patente_test = "123-ABCD-45"
    coincidencia = re.match(r'^([A-Za-z]{2}\d{3}[A-Za-z]{2}|[A-Za-z]{3}\d{3}|[A-Za-z]{3}\d{4})$', patente_test)
    if coincidencia == None:
        print("Prueba validar_patente (Inválido): Correcta")
    else:
        print("Error en prueba validar_patente (Inválido)")

def prueba_validar_patente_limite():
    # Caso Límite: Formato Mercosur de 7 caracteres (ej. ABC1234)
    patente_test = "ABC1234"
    coincidencia = re.match(r'^([A-Za-z]{2}\d{3}[A-Za-z]{2}|[A-Za-z]{3}\d{3}|[A-Za-z]{3}\d{4})$', patente_test)
    if coincidencia != None:
        print("Prueba validar_patente (Límite): Correcta")
    else:
        print("Error en prueba validar_patente (Límite)")

def prueba_validar_tipo_valido():
    # Caso Válido: Tipo de vehículo permitido ('auto')
    tipo_test = "auto"
    coincidencia = re.match(r"^(auto|moto|camioneta|Auto|Moto|Camioneta|MOTO|CAMIONETA|AUTO)$", tipo_test)
    if coincidencia != None:
        print("Prueba validar_tipo (Válido): Correcta")
    else:
        print("Error en prueba validar_tipo (Válido)")

def prueba_validar_tipo_invalido():
    # Caso Inválido: Tipo no contemplado ('colectivo')
    tipo_test = "colectivo"
    coincidencia = re.match(r"^(auto|moto|camioneta|Auto|Moto|Camioneta|MOTO|CAMIONETA|AUTO)$", tipo_test)
    if coincidencia == None:
        print("Prueba validar_tipo (Inválido): Correcta")
    else:
        print("Error en prueba validar_tipo (Inválido)")

def prueba_validar_tipo_limite():
    # Caso Límite: Entrada en mayúsculas sostenidas ('CAMIONETA')
    tipo_test = "CAMIONETA"
    coincidencia = re.match(r"^(auto|moto|camioneta|Auto|Moto|Camioneta|MOTO|CAMIONETA|AUTO)$", tipo_test)
    if coincidencia != None:
        print("Prueba validar_tipo (Límite): Correcta")
    else:
        print("Error en prueba validar_tipo (Límite)")

def prueba_json_vehiculos_valido():
    # Caso Válido: Guardar y cargar datos correctamente
    archivo_prueba = "test_vehiculos.json"
    datos_prueba = [{"patente": "AB123CD", "tipo": "auto", "dni": "44123456"}]
    
    guardado_ok = guardar_vehiculosjson(archivo_prueba, datos_prueba)
    datos_cargados = cargar_vehiculosjson(archivo_prueba)
    
    guardar_vehiculosjson(archivo_prueba, [])

    if guardado_ok and datos_cargados == datos_prueba:
        print("Prueba JSON Vehículos (Válido): Correcta")
    else:
        print("Error en prueba JSON Vehículos (Válido)")

def prueba_json_vehiculos_invalido():
    # Caso Inválido / Excepción: Intentar abrir un archivo inexistente
    archivo_inexistente = "archivo_fantasma_prueba.json"
    resultado = cargar_vehiculosjson(archivo_inexistente)
    if resultado == []:
        print("Prueba JSON Vehículos (Inexistente): Correcta")
    else:
        print("Error en prueba JSON Vehículos (Inexistente)")


# ==============================================================================
# 4. PRUEBAS PARA: RESERVAS
# ==============================================================================

def prueba_escritura_digitos_menor():
    # Caso Válido: Un número menor a 10 debe agregarle un "0" adelante
    resultado = escritura_digitos(5)
    if resultado == "05":
        print("Prueba escritura_digitos (Menor a 10): Correcta")
    else:
        print("Error en prueba escritura_digitos (Menor a 10)")

def prueba_escritura_digitos_mayor():
    # Caso Límite: Un número mayor a 9 debe devolver el mismo número en texto
    resultado = escritura_digitos(15)
    if resultado == "15":
        print("Prueba escritura_digitos (Mayor a 9): Correcta")
    else:
        print("Error en prueba escritura_digitos (Mayor a 9)")

def prueba_contar_duracion_normal():
    # Caso Válido: Reserva normal en el mismo día (2 horas desde las 14)
    duracion, hora_fin = contar_duracion(2, 14)
    if duracion == 2 and hora_fin == 16:
        print("Prueba contar_duracion (Normal): Correcta")
    else:
        print("Error en prueba contar_duracion (Normal)")

def prueba_contar_duracion_madrugada():
    # Caso Límite: Reserva que cruza la medianoche (3 horas desde las 22hs)
    duracion, hora_fin = contar_duracion(3, 22)
    if duracion == 3 and hora_fin == 1:
        print("Prueba contar_duracion (Madrugada): Correcta")
    else:
        print("Error en prueba contar_duracion (Madrugada)")

def prueba_validar_fecha_valida():
    # Caso Válido: Fecha correcta, no debe modificar nada
    dia, mes, año = validar_fecha(15, 6, 2026)
    if dia == 15 and mes == 6 and año == 2026:
        print("Prueba validar_fecha (Válido): Correcta")
    else:
        print("Error en prueba validar_fecha (Válido)")

def prueba_validar_hora_valida():
    # Caso Válido: Horario correcto (ej 14:30), no debe modificar nada
    hora, minuto = validar_hora(14, 30)
    if hora == 14 and minuto == 30:
        print("Prueba validar_hora (Válido): Correcta")
    else:
        print("Error en prueba validar_hora (Válido)")

def prueba_json_reservas_valido():
    # Caso Válido: Guardar datos en JSON y luego cargarlos para ver si coinciden
    archivo_prueba = "test_reservas_temp.json"
    datos_prueba = [{"nombre": "Juan", "dia": 10}]
    
    guardar_datos_json(archivo_prueba, datos_prueba)
    datos_cargados = cargar_datos_json(archivo_prueba)
    
    guardar_datos_json(archivo_prueba, [None])
        
    if datos_cargados == datos_prueba:
        print("Prueba JSON Reservas (Válido): Correcta")
    else:
        print("Error en prueba JSON Reservas (Válido)")

def prueba_json_reservas_invalido():
    # Caso Inválido: Intentar cargar un archivo que no existe
    resultado = cargar_datos_json("archivo_inexistente.json")
    if resultado == [None]:
        print("Prueba JSON Reservas (Inexistente): Correcta")
    else:
        print("Error en prueba JSON Reservas (Inexistente)")


# ==============================================================================
# 5. PRUEBAS PARA: TARIFAS
# ==============================================================================

# --- 5.1 PRUEBAS PARA: convertir_hora_a_minutos() ---

def prueba_convertir_hora_valida():
    # Caso Válido: Conversión habitual ("08:30" -> 510 minutos)
    resultado = convertir_hora_a_minutos("08:30")
    if resultado == 510:
        print("Prueba convertir_hora_a_minutos (Válido): Correcta")
    else:
        print("Error en prueba convertir_hora_a_minutos (Válido)")

def prueba_convertir_hora_invalida():
    # Caso Inválido: Formato incorrecto sin dos dígitos iniciales
    resultado = convertir_hora_a_minutos("8:30")
    if resultado == -1:
        print("Prueba convertir_hora_a_minutos (Inválido): Correcta")
    else:
        print("Error en prueba convertir_hora_a_minutos (Inválido)")

def prueba_convertir_hora_limite():
    # Caso Límite: Último minuto permitido del día ("23:59" -> 1439 minutos)
    resultado = convertir_hora_a_minutos("23:59")
    if resultado == 1439:
        print("Prueba convertir_hora_a_minutos (Límite): Correcta")
    else:
        print("Error en prueba convertir_hora_a_minutos (Límite)")


# --- 5.2 PRUEBAS PARA: calcular_minutos_estadia() ---

def prueba_calcular_minutos_valida():
    # Caso Válido: Permanencia habitual en el mismo día (08:00 a 10:30 -> 150 min)
    resultado = calcular_minutos_estadia("08:00", "10:30", 0)
    if resultado == 150:
        print("Prueba calcular_minutos_estadia (Válido): Correcta")
    else:
        print("Error en prueba calcular_minutos_estadia (Válido)")

def prueba_calcular_minutos_invalida():
    # Caso Inválido: Egreso registrado antes que el ingreso en el mismo día
    resultado = calcular_minutos_estadia("10:30", "08:00", 0)
    if resultado == -1:
        print("Prueba calcular_minutos_estadia (Inválido): Correcta")
    else:
        print("Error en prueba calcular_minutos_estadia (Inválido)")

def prueba_calcular_minutos_limite():
    # Caso Límite: Estadía exacta de 1 día (24 horas -> 1440 min)
    resultado = calcular_minutos_estadia("08:00", "08:00", 1)
    if resultado == 1440:
        print("Prueba calcular_minutos_estadia (Límite): Correcta")
    else:
        print("Error en prueba calcular_minutos_estadia (Límite)")


# --- 5.3 PRUEBAS PARA: calcular_costo() ---

def prueba_calcular_costo_valida():
    # Caso Válido: Auto por 5 horas sin descuento ($4000 * 5 = 20000)
    subtotal, descuento, total = calcular_costo(5, "auto")
    if subtotal == 20000 and descuento == 0 and total == 20000:
        print("Prueba calcular_costo (Válido): Correcta")
    else:
        print("Error en prueba calcular_costo (Válido)")

def prueba_calcular_costo_invalida():
    # Caso Inválido: Tipo de vehículo sin tarifa registrada
    subtotal, descuento, total = calcular_costo(5, "colectivo")
    if (subtotal, descuento, total) == (-1, -1, -1):
        print("Prueba calcular_costo (Inválido): Correcta")
    else:
        print("Error en prueba calcular_costo (Inválido)")

def prueba_calcular_costo_limite():
    # Caso Límite: Aplicar primer escalón de descuento (>= 12 horas aplica 10% desc)
    # Camioneta = $6000 * 12 = $72000. Desc 10% = $7200. Total = $64800
    subtotal, descuento, total = calcular_costo(12, "camioneta")
    if subtotal == 72000 and descuento == 7200 and total == 64800:
        print("Prueba calcular_costo (Límite): Correcta")
    else:
        print("Error en prueba calcular_costo (Límite)")


# ==============================================================================
# CASO PRUEBA ADICIONAL
# ==============================================================================


# ==============================================================================
# EJECUCIÓN GENERAL
# ==============================================================================

def pruebas_estacionamiento():
    print("--- PRUEBAS: ver_estado ---")
    prueba_ver_estado_valido()
    prueba_ver_estado_invalido()
    prueba_ver_estado_limite()

    print("\n--- PRUEBAS: validar_cierre ---")
    prueba_validar_cierre_valido()
    prueba_validar_cierre_invalido()
    prueba_validar_cierre_limite()

    print("\n--- PRUEBAS: validar_horario ---")
    prueba_validar_horario_valido()
    prueba_validar_horario_invalido()
    prueba_validar_horario_limite()

def pruebas_usuarios():
    print("\n--- PRUEBAS: usuarios ---")
    prueba_validar_nombre()
    prueba_validar_email()
    prueba_validar_dni()
    prueba_formato_usuarios_valido()
    prueba_formato_usuarios_invalido()
    prueba_formatear_usuario()

def pruebas_vehiculos():
    print("\n--- PRUEBAS: validar_patente ---")
    prueba_validar_patente_valida()
    prueba_validar_patente_invalida()
    prueba_validar_patente_limite()

    print("\n--- PRUEBAS: validar_tipodeauto ---")
    prueba_validar_tipo_valido()
    prueba_validar_tipo_invalido()
    prueba_validar_tipo_limite()

    print("\n--- PRUEBAS: JSON Vehículos ---")
    prueba_json_vehiculos_valido()
    prueba_json_vehiculos_invalido()

def pruebas_reservas():
    print("\n--- PRUEBAS: escritura_digitos ---")
    prueba_escritura_digitos_menor()
    prueba_escritura_digitos_mayor()

    print("\n--- PRUEBAS: contar_duracion ---")
    prueba_contar_duracion_normal()
    prueba_contar_duracion_madrugada()

    print("\n--- PRUEBAS: validar fechas/horas ---")
    prueba_validar_fecha_valida()
    prueba_validar_hora_valida()

    print("\n--- PRUEBAS: JSON Reservas ---")
    prueba_json_reservas_valido()
    prueba_json_reservas_invalido()

def pruebas_tarifas():
    print("\n--- PRUEBAS: convertir_hora_a_minutos ---")
    prueba_convertir_hora_valida()
    prueba_convertir_hora_invalida()
    prueba_convertir_hora_limite()

    print("\n--- PRUEBAS: calcular_minutos_estadia ---")
    prueba_calcular_minutos_valida()
    prueba_calcular_minutos_invalida()
    prueba_calcular_minutos_limite()

    print("\n--- PRUEBAS: calcular_costo ---")
    prueba_calcular_costo_valida()
    prueba_calcular_costo_invalida()
    prueba_calcular_costo_limite()

def ejecutar_todas_las_pruebas():
    pruebas_estacionamiento()
    pruebas_usuarios()
    pruebas_vehiculos()
    pruebas_reservas()
    pruebas_tarifas()
    print("\n" + "=" * 50)

if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
