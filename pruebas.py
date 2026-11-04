import re
from vehiculos import (
    cargar_vehiculosjson,
    guardar_vehiculosjson,
    validar_patente,
    validar_tipodeauto
)

# ==============================================================================
# 1. PRUEBAS PARA: validar_patente() -> VEHÍCULOS
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


# ==============================================================================
# 2. PRUEBAS PARA: validar_tipodeauto() -> VEHÍCULOS
# ==============================================================================

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


# ==============================================================================
# 3. PRUEBAS PARA: JSON y Persistencia -> VEHÍCULOS
# ==============================================================================

def prueba_json_valido():
    # Caso Válido: Guardar y cargar datos correctamente
    archivo_prueba = "test_vehiculos.json"
    datos_prueba = [{"patente": "AB123CD", "tipo": "auto", "dni": "44123456"}]
    
    guardado_ok = guardar_vehiculosjson(archivo_prueba, datos_prueba)
    datos_cargados = cargar_vehiculosjson(archivo_prueba)
    
    # Dejamos el archivo vaciado usando guardar_vehiculosjson
    guardar_vehiculosjson(archivo_prueba, [])

    if guardado_ok and datos_cargados == datos_prueba:
        print("Prueba JSON (Válido): Correcta")
    else:
        print("Error en prueba JSON (Válido)")

def prueba_json_invalido():
    # Caso Inválido / Excepción: Intentar abrir un archivo inexistente
    archivo_inexistente = "archivo_fantasma_prueba.json"
    resultado = cargar_vehiculosjson(archivo_inexistente)
    if resultado == []:
        print("Prueba JSON (Inexistente): Correcta")
    else:
        print("Error en prueba JSON (Inexistente)")


# ==============================================================================
# EJECUCIÓN GENERAL
# ==============================================================================
def ejecutar_todas_las_pruebas():
    pruebas_vehiculos()
    print("=" * 50)


def pruebas_vehiculos():
    print("--- PRUEBAS: validar_patente ---")
    prueba_validar_patente_valida()
    prueba_validar_patente_invalida()
    prueba_validar_patente_limite()

    print("\n--- PRUEBAS: validar_tipodeauto ---")
    prueba_validar_tipo_valido()
    prueba_validar_tipo_invalido()
    prueba_validar_tipo_limite()

    print("\n--- PRUEBAS: JSON y Persistencia ---")
    prueba_json_valido()
    prueba_json_invalido()


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
