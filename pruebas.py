from estacionamiento import (
    ver_estado,
    validar_cierre,
    validar_horario
)

# ==============================================================================
# 1. PRUEBAS PARA: ver_estado() -> ESTACIONAMIENTOS
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


# ==============================================================================
# 2. PRUEBAS PARA: validar_cierre() -> ESTACIONAMIENTOS
# ==============================================================================

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


# ==============================================================================
# 3. PRUEBAS PARA: validar_horario() -> ESTACIONAMIENTOS
# ==============================================================================

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
# EJECUCIÓN GENERAL
# ==============================================================================
def ejecutar_todas_las_pruebas():
    pruebas_estacionamiento()
    print("=" * 50)


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

if __name__ == "__main__":
    ejecutar_todas_las_pruebas()