from reservas import generar_reserva


def conversion_minutos(hora, minuto):

    #Convierte todo a minutos para comodidad a la hora de comparar valores de horarios.
    return hora * 60 + minuto


def usuario_horario_salida(hora_inicio, minuto_inicio):
    print("\n--- REGISTRO DE SALIDA DEL PARKING ---")

    minutos_inicio_total = hora_inicio * 60 + minuto_inicio

    while True:
        hora_salida = int(input("Ingrese la hora de salida real (0-23): "))
        while hora_salida < 0 or hora_salida > 23:
            hora_salida = int(input("Hora inválida. Ingrese la hora de salida real (0-23): "))

        minuto_salida = int(input("Ingrese los minutos de salida real (0-59): "))
        while minuto_salida < 0 or minuto_salida > 59:
            minuto_salida = int(input("Minutos inválidos. Ingrese los minutos de salida (0-59): "))

        minutos_salida_total = hora_salida * 60 + minuto_salida

        if minutos_salida_total < minutos_inicio_total:
            print(f"\nError: El horario de salida ({hora_salida:02d}:{minuto_salida:02d}) "f"no puede ser anterior al inicio de la reserva ({hora_inicio:02d}:{minuto_inicio:02d}).")
            print("Por favor, ingrese el horario nuevamente.\n")
        else:
            return hora_salida, minuto_salida


def calcular_costo_base(duracion_horas):
    tarifa_base_hora = 3500
    return duracion_horas * tarifa_base_hora


def calcular_recargo_exceso(minutos_pactados, minutos_reales, costo_base):
    if minutos_reales <= minutos_pactados:
        return 0

    minutos_exceso = minutos_reales - minutos_pactados

    if minutos_exceso % 5 == 0:
        bloques_exceso = minutos_exceso // 5
    else:
        bloques_exceso = (minutos_exceso // 5) + 1

    porcentaje_recargo = bloques_exceso * 0.10
    return costo_base * porcentaje_recargo

'''
# --------------- PROGRAMA PRINCIPAL ---------------
print("--- INICIO DE RESERVA ---")
hora_inicial, min_inicial, duracion_horas, hora_fin = generar_reserva()

minutos_entrada_total = conversion_minutos(hora_inicial, min_inicial)
minutos_salida_prevista = conversion_minutos(hora_fin, min_inicial)

if minutos_salida_prevista < minutos_entrada_total:
    minutos_salida_prevista += 24 * 60


hora_salida_real, min_salida_real = usuario_horario_salida(hora_inicial, min_inicial)
minutos_salida_real = conversion_minutos(hora_salida_real, min_salida_real)

if minutos_salida_real < minutos_entrada_total:
    minutos_salida_real += 24 * 60

costo_base = calcular_costo_base(duracion_horas)

recargo = calcular_recargo_exceso(minutos_salida_prevista, minutos_salida_real, costo_base)

total_pagar = costo_base + recargo

print("\n------------- RESUMEN DE CUENTA -------------")
print(f"Costo base de la reserva ({duracion_horas} hs): ${costo_base}")

if recargo > 0:
    minutos_demora = minutos_salida_real - minutos_salida_prevista
    print(f"Minutos de exceso registrados: {minutos_demora} min")
    print(f"Recargo por demora aplicado: ${recargo}")
else:
    print("Salida realizada a tiempo. Sin recargos aplicados.")

print(f"TOTAL A PAGAR: ${total_pagar}")
'''