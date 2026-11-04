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
# 4. PRUEBAS PARA FUNCIONES DE USUARIOS
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
# EJECUCIÓN GENERAL
# ==============================================================================
def ejecutar_todas_las_pruebas():
    pruebas_estacionamiento()
    pruebas_usuarios()
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

def pruebas_usuarios():
    print("\n--- PRUEBAS: usuarios ---")
    prueba_validar_nombre()
    prueba_validar_email()
    prueba_validar_dni()
    prueba_formato_usuarios_valido()
    prueba_formato_usuarios_invalido()
    prueba_formatear_usuario()

if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
