import estacionamiento
import tarifas
import reservas
import usuarios
import vehiculos
import reportes

def menu_principal():
    # --- INICIALIZACIÓN DE LA BASE DE DATOS EN MEMORIA ---
    
    # 1. Listas de Estacionamientos
    estacionamientos = [[None], [None], [None], [None], [None]] # Nombre, estado, direccion, capacidad total, capacidad actual
    horarios = [None] # Cada lista(fila) es un día de la semana(7 fijas de Lunes a Domingo), la columna es cada estacionamiento: True = 24 horas, False = Cerrado, str = "00:00 - 12:30"
    
    # 2. Listas de Usuarios
    nombres = []
    apellidos = []
    dnis = []
    emails = []
    telefonos = []
    estados = []

    # 3. Listas de Vehículos
    patentes = []
    tipos = []
    dni_vehiculos = []

    # 4. Lista de reservas
    reservar = []
    reservas_canceladas = []

    # 5. Listas de Tarifas y Cobros
    lista_cobros = []
    lista_patente_cobrada = []

    # --- BUCLE DEL MENÚ PRINCIPAL ---
    opcion_principal = "-1"
    
    while opcion_principal != "0":
        print("\n" + "="*60)
        print("PARK DIRECT - SISTEMA DE GESTIÓN - PANEL ADMINISTRADOR")
        print("="*60)
        print("1. Seleccionar un estacionamiento existente")
        print("2. Crear un estacionamiento nuevo")
        print("3. Ver estadísticas generales del sistema")
        print("4. Eliminar un estacionamiento")
        print("0. Salir del sistema")
        print("="*60)
        
        opcion_principal = input("Seleccione una opción: ")
        
        while opcion_principal not in ["0", "1", "2", "3", "4"]:
            opcion_principal = input("Error: Opción inválida. Vuelva a seleccionar: ")

        # --- CREAR ESTACIONAMIENTO ---
        if opcion_principal == "2":
            estacionamiento.crear_estacionamiento(estacionamientos, horarios)

        # --- SELECCIONAR ESTACIONAMIENTO ---
        elif opcion_principal == "1":
            if len(estacionamientos[0]) > 1: 
                # El administrador elige sobre qué estacionamiento va a trabajar
                sel = estacionamiento.elegir_estacionamiento(estacionamientos)
                nombre_actual = estacionamientos[0][sel]
                
                op_sub = "-1"
                while op_sub != "0":
                    print("\n" + "="*60)
                    print(f" ADMINISTRANDO: {nombre_actual}")
                    print("="*60)
                    print("1. Ver / Modificar datos del estacionamiento")
                    print("2. Administrar Reservas")
                    print("3. Administrar Usuarios y Vehículos")
                    print("4. Administrar Tarifas y Cobros")
                    print("0. Volver al menú de inicio")
                    print("="*60)
                    
                    op_sub = input("Seleccione un módulo: ")
                    while op_sub not in ["0", "1", "2", "3", "4"]:
                        op_sub = input("Error: Opción inválida. Vuelva a seleccionar: ")

                    # 1. DATOS DEL ESTACIONAMIENTO
                    if op_sub == "1":
                        estacionamiento.mostrar_informacion(sel, estacionamientos, horarios)
                        modificar = input("\n¿Desea modificar este estacionamiento? (y/n): ")
    
                        if modificar in ['y', 'Y', 's', 'S', 'si', 'SI', 'Si', 'sI', 'yes', 'YES', 'Yes']:
                            estacionamiento.modificar(sel, estacionamientos, horarios)
                    
                    # 2. RESERVAS
                    elif op_sub == "2":
                        op_res = "-1"
                        while op_res != "0":
                            print(f"\n -------- MENU RESERVAS ({nombre_actual}) --------")
                            print("1. Generar una reserva. ")
                            print("2. Consultar reservas. ")
                            print("3. Modificar reserva. ")
                            print("4. Cancelar una reserva.")
                            print("0. Volver atrás.")
                            op_res = input("Opción: ")
                            
                            if op_res == "1":
                                # Se agregó 'sel' como parámetro
                                reservas.generar_reserva(sel, estacionamientos, reservar)

                            elif op_res == "2":
                                if len(reservar) == 0:
                                    print("\n---------------- !IMPORTANTE¡ ---------------- \n")
                                    print("Debe cargarse una reserva previamente.\n")
                                else:
                                    reservas.consultar_reservas(reservar)

                            elif op_res == "3":
                                if len(reservar) == 0:
                                    print("\n---------------- !IMPORTANTE¡ ---------------- \n")
                                    print("Debe cargarse una reserva previamente.\n")
                                else:
                                    reservas.modificar_reserva(reservar, sel)

                            elif op_res == "4":
                                if len(reservar) == 0:
                                    print("\n---------------- !IMPORTANTE¡ ---------------- \n")
                                    print("Debe cargarse una reserva previamente.\n")
                                else:
                                    # Se agregó 'sel' como parámetro
                                    reservas.cancelar_reserva(sel, estacionamientos, reservar, reservas_canceladas)

                    # 3. USUARIOS Y VEHÍCULOS (Integrados)
                    elif op_sub == "3":
                        op_usu = "-1"
                        while op_usu != "0":
                            print(f"\n--- USUARIOS Y VEHÍCULOS ({nombre_actual}) ---")
                            print("1. Alta de usuario")
                            print("2. Mostrar usuarios activos")
                            print("3. Modificar usuario")
                            print("4. Ingresar vehículo nuevo (Requiere DNI)")
                            print("5. Mostrar vehículos registrados")
                            print("6. Dar de baja al usuario")
                            print("7. Reactivar usuario dado de baja")
                            print("8. Eliminar vehículo")
                            print("0. Volver atrás")
                            op_usu = input("Opción: ")
                            
                            if op_usu == "1":
                                usuarios.alta(nombres, apellidos, dnis, emails, telefonos, estados)
                            elif op_usu == "2":
                                usuarios.mostrar_usuarios(nombres, apellidos, dnis, emails, telefonos, estados)
                            elif op_usu == "3":
                                usuarios.modificar_usuario(nombres, apellidos, dnis, emails, telefonos, estados)
                            elif op_usu == "4":
                                vehiculos.ingresar_vehiculo(patentes, tipos, dni_vehiculos, dnis)
                            elif op_usu == "5":
                                vehiculos.mostrar_vehiculos(patentes, tipos, dni_vehiculos)
                            elif op_usu == "6":
                                usuarios.baja_usuarios(dnis, estados)
                            elif op_usu == "7":
                                usuarios.quitar_baja(nombres, apellidos, dnis, emails, telefonos, estados)
                            elif op_usu == "8":
                                vehiculos.eliminar_vehiculo(patentes, tipos, dni_vehiculos, reservar)
                                
                    # 4. TARIFAS Y COBROS
                    elif op_sub == "4":
                        op_tar = "-1"
                        while op_tar != "0":
                            print(f"\n--- TARIFAS Y COBROS ({nombre_actual}) ---")
                            print("1. Cobrar estacionamiento")
                            print("2. Mostrar historial de cobros")
                            print("0. Volver atrás")
                            op_tar = input("Opción: ")
                            
                            if op_tar == "1":
                                tarifas.cobrar_estacionamiento(patentes, tipos, lista_cobros, lista_patente_cobrada)
                            elif op_tar == "2":
                                tarifas.mostrar_cobros(lista_cobros, lista_patente_cobrada)

            else:
                print("\nNo hay estacionamientos registrados en el sistema. Por favor, cree uno primero.")

        # --- ESTADÍSTICAS GENERALES ---
        elif opcion_principal == "3":
            reportes.mostrar_reportes(estacionamientos, tipos, dnis, estados, reservar, reservas_canceladas, tarifas.lista_cobros)

        # --- ELIMINAR ESTACIONAMIENTO ---
        elif opcion_principal == "4":
            estacionamiento.eliminar_estacionamiento(estacionamientos, horarios)

        # --- SALIR ---
        elif opcion_principal == "0":
            print("\nCerrando sesión de administrador. ¡Hasta luego!")

menu_principal()