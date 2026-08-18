def verificacion_horarios(hora_entrada, minutos_entrada, hora_salida, minutos_salida):

    #Verificación de la hora y minutos de entrada con un rango válido de 0 a 23 para la hora y de 0 a 59 para los minutos
    while int(hora_entrada) < 0 or int(hora_entrada) > 23 or int(minutos_entrada) < 0 or int(minutos_entrada) > 59:
        print("Hora o minutos de entrada inválidos. Por favor, ingrese valores válidos.")
        hora_entrada = input("Ingrese la hora de entrada (HH):    ")
        minutos_entrada = input("Ingrese los minutos de entrada (MM):    ")

    #Verificación de la hora y minutos de salida con un rango válido de 0 a 23 para la hora y de 0 a 59 para los minutos
    while int(hora_salida) < 0 or int(hora_salida) > 23 or int(minutos_salida) < 0 or int(minutos_salida) > 59:
        print("Hora o minutos de salida inválidos. Por favor, ingrese valores válidos.")
        hora_salida = input("Ingrese la hora de salida (HH):    ")
        minutos_salida = input("Ingrese los minutos de salida (MM):    ")

    return hora_entrada, minutos_entrada, hora_salida, minutos_salida


def conversion_entrada_salida(hora_entrada, minutos_entrada, hora_salida, minutos_salida):
    
    # Convertir la hora y los minutos de entrada y salida a minutos totales luego de hacer la verificación
    hora_entrada, minutos_entrada, hora_salida, minutos_salida = verificacion_horarios(hora_entrada, minutos_entrada, hora_salida, minutos_salida)
    entrada_total = int(hora_entrada) * 60 + int(minutos_entrada)
    salida_total = int(hora_salida) * 60 + int(minutos_salida)
    
    # Verificar si la hora de salida es mayor que la hora de entrada
    while salida_total < entrada_total:
        print("La hora de salida no puede ser menor que la hora de entrada. Por favor, ingrese valores válidos.")
        hora_entrada = input("Ingrese la hora de entrada (HH):    ")
        minutos_entrada = input("Ingrese los minutos de entrada (MM):    ")
        hora_salida = input("Ingrese la hora de salida (HH):    ")
        minutos_salida = input("Ingrese los minutos de salida (MM):    ")


        hora_entrada, minutos_entrada, hora_salida, minutos_salida = verificacion_horarios(hora_entrada, minutos_entrada, hora_salida, minutos_salida)

        entrada_total = int(hora_entrada) * 60 + int(minutos_entrada)
        salida_total = int(hora_salida) * 60 + int(minutos_salida)

    #Se calcula la permanencia en minutos
    permanencia = salida_total - entrada_total
    
    return entrada_total, salida_total, permanencia


#Programa principal

fecha = input("Ingrese la fecha de estacionamiento (DD-MM-YYYY):    ")
hora_entrada = input("Ingrese la hora de entrada (HH):    ")
minutos_entrada = input("Ingrese los minutos de entrada (MM):    ")
hora_salida = input("Ingrese la hora de salida (HH):    ")
minutos_salida = input("Ingrese los minutos de salida (MM):    ")

entrada_total, salida_total, permanencia = conversion_entrada_salida(hora_entrada, minutos_entrada, hora_salida, minutos_salida)