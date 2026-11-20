import estacionamiento
import tarifas
import reservas
import usuarios
import vehiculos
import reportes

def menu_principal():
    # --- INICIALIZACIÓN DE LA BASE DE DATOS EN MEMORIA Y ESTRUCTURAS ---
    
    # 1. Estacionamientos
    EST_JSON = 'estacionamientos.json'
    estacionamientos = estacionamiento.cargar_estacionamiento(EST_JSON)
    
    # 2. Usuarios
    usuarios.crea_archivo()
    usuarios_registrados = usuarios.cargar_usuarios()
    
    # 3. Vehículos
    VHC_JSON = 'vehiculos.json'
    vehiculos_registrados = vehiculos.cargar_vehiculosjson(VHC_JSON)
    
    # 4. Reservas
    RESER_JSON = 'reservas.json'
    RESER_CANCEL_JSON = 'reservas_canceladas.json'
    reservar = reservas.cargar_datos_json(RESER_JSON)
    reservas_canceladas = reservas.cargar_datos_json(RESER_CANCEL_JSON)

    # 5. Tarifas y Cobros
    TARIFAS_JSON = 'tarifas.json'
    TARIFAS_TXT = 'registro_cobros.txt'
    cobros_registrados = tarifas.cargar_cobros(TARIFAS_JSON, TARIFAS_TXT)

    # --- BUCLE DEL MENÚ PRINCIPAL ---
    opcion_principal = "-1"
    
    while opcion_principal != "0":
        # Se extraen las listas derivadas de vehículos actualizadas en cada ciclo
        tipos = [v["tipo"] for v in vehiculos_registrados] if vehiculos_registrados else []

        print("\n" + "="*60)
        print("PARK DIRECT - SISTEMA DE GESTIÓN - PANEL ADMINISTRADOR")
        print("="*60)
        print("1. Seleccionar un estacionamiento existente")
        print("2. Crear un estacionamiento nuevo")
        print("3. Ver estadísticas generales del sistema")
        print("4. Eliminar un estacionamiento")
        print("5. Exportar reportes a TXT")
        print("0. Salir del sistema")
        print("="*60)
        
        opcion_principal = input("Seleccione una opción: ")
        
        while opcion_principal not in {"0", "1", "2", "3", "4", "5"}:
            opcion_principal = input("Error: Opción inválida. Vuelva a seleccionar: ")

        # --- CREAR ESTACIONAMIENTO ---
        if opcion_principal == "2":
            estacionamiento.crear_estacionamiento(estacionamientos, EST_JSON)

        # --- SELECCIONAR ESTACIONAMIENTO ---
        elif opcion_principal == "1":
            if estacionamientos: 
                sel = estacionamiento.elegir_estacionamiento(estacionamientos)
                nombre_actual = estacionamientos[sel]['nombre']
                
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
                    while op_sub not in {"0", "1", "2", "3", "4"}:
                        op_sub = input("Error: Opción inválida. Vuelva a seleccionar: ")

                    # 1. DATOS DEL ESTACIONAMIENTO
                    if op_sub == "1":
                        estacionamiento.mostrar_informacion(sel, estacionamientos)
                        modificar = input("\n¿Desea modificar este estacionamiento? (y/n): ")
    
                        if modificar in {'y', 'Y', 's', 'S', 'si', 'SI', 'Si', 'sI', 'yes', 'YES', 'Yes'}:
                            estacionamiento.modificar(sel, estacionamientos, EST_JSON)
                    
                    elif op_sub == "2":
                        op_res = "-1"
                        while op_res != "0":
                            print(f"\n -------- MENU RESERVAS ({nombre_actual}) --------")
                            print("1. Generar una reserva. ")
                            print("2. Consultar reservas. ")
                            print("3. Modificar reserva. ")
                            print("4. Cancelar una reserva.")
                            print("5. Recuperar una reserva.")
                            print("0. Volver atrás.")
                            op_res = input("Opción: ")
                            
                            if op_res == "1":
                                reservas.generar_reserva(sel, estacionamientos, RESER_JSON, reservar)
                                estacionamiento.guardar_estacionamiento(EST_JSON, estacionamientos)

                            elif op_res == "2":
                                if len(reservar) <= 1:
                                    print("\n---------------- !IMPORTANTE¡ ---------------- \n")
                                    print("Debe cargarse una reserva previamente.\n")
                                else:
                                    reservas.consultar_reservas(reservar)

                            elif op_res == "3":
                                if len(reservar) <= 1:
                                    print("\n---------------- !IMPORTANTE¡ ---------------- \n")
                                    print("Debe cargarse una reserva previamente.\n")
                                else:
                                    reservas.modificar_reserva(sel, estacionamientos, RESER_JSON, reservar)
                                    estacionamiento.guardar_estacionamiento(EST_JSON, estacionamientos)

                            elif op_res == "4":
                                if len(reservar) <= 1:
                                    print("\n---------------- !IMPORTANTE¡ ---------------- \n")
                                    print("Debe cargarse una reserva previamente.\n")
                                else:
                                    reservas.cancelar_reserva(sel, estacionamientos, RESER_JSON, RESER_CANCEL_JSON, reservas_canceladas, reservar)
                                    estacionamiento.guardar_estacionamiento(EST_JSON, estacionamientos)

                            elif op_res == '5':
                                if len(reservas_canceladas) <= 1:
                                    print("\n---------------- !IMPORTANTE¡ ---------------- \n")
                                    print("No se puede recuperar ninguna reserva. Debido a que no hay reservas canceladas.\n")
                                else:
                                    reservas.recuperar_reserva(sel, estacionamientos, RESER_JSON, RESER_CANCEL_JSON, reservas_canceladas, reservar)
                                    estacionamiento.guardar_estacionamiento(EST_JSON, estacionamientos)
                    
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
                                usuarios.alta(usuarios_registrados)
                            elif op_usu == "2":
                                usuarios.mostrar_usuarios(usuarios_registrados)
                            elif op_usu == "3":
                                usuarios.modificar_usuario(usuarios_registrados)
                            elif op_usu == "4":
                                vehiculos.ingresar_vehiculo(VHC_JSON, usuarios_registrados)
                                vehiculos_registrados = vehiculos.cargar_vehiculosjson(VHC_JSON)
                            elif op_usu == "5":
                                vehiculos.mostrar_vehiculos(VHC_JSON, usuarios_registrados)
                            elif op_usu == "6":
                                usuarios.baja_usuarios(usuarios_registrados)
                            elif op_usu == "7":
                                usuarios.quitar_baja(usuarios_registrados)
                            elif op_usu == "8":
                                vehiculos.eliminar_vehiculo(VHC_JSON)
                                vehiculos_registrados = vehiculos.cargar_vehiculosjson(VHC_JSON)
                                
                    # 4. TARIFAS Y COBROS
                    elif op_sub == "4":
                        op_tar = "-1"
                        while op_tar != "0":
                            print(f"\n--- TARIFAS Y COBROS ({nombre_actual}) ---")
                            print("1. Cobrar estacionamiento a un vehículo")
                            print("2. Mostrar historial de cobros")
                            print("0. Volver atrás")
                            op_tar = input("Opción: ")
                            
                            if op_tar == "1":
                                patentes = [v["patente"] for v in vehiculos_registrados]
                                tipos_vhc = [v["tipo"] for v in vehiculos_registrados]
                                dni_vehiculos = [v["dni"] for v in vehiculos_registrados]
                                cobro = tarifas.cobrar_estacionamiento(nombre_actual, patentes, tipos_vhc, dni_vehiculos)
                                if cobro:
                                    cobros_registrados = tarifas.cargar_cobros()
                            elif op_tar == "2":
                                tarifas.mostrar_cobros(nombre_actual)

            else:
                print("\nNo hay estacionamientos registrados en el sistema. Por favor, cree uno primero.")

        # --- ESTADÍSTICAS GENERALES ---
        elif opcion_principal == "3":
            cobros_registrados = tarifas.cargar_cobros()
            reportes.mostrar_reportes(estacionamientos, tipos, usuarios_registrados, reservar, reservas_canceladas, cobros_registrados)

        # --- ELIMINAR ESTACIONAMIENTO ---
        elif opcion_principal == "4":
            estacionamiento.eliminar_estacionamiento(estacionamientos, EST_JSON)

        # --- EXPORTAR REPORTES A TXT ---
        elif opcion_principal == "5":
            op_txt = "-1"
            while op_txt != "0":
                print("\n" + "="*60)
                print(" MÓDULO DE EXPORTACIÓN A TXT")
                print("="*60)
                print("1. Imprimir informe de estacionamientos")
                print("2. Imprimir base de datos (Usuarios y Vehículos)")
                print("3. Imprimir datos de tarifas")
                print("0. Volver al menú principal")
                print("="*60)
                
                op_txt = input("Seleccione una opción: ")
                while op_txt not in {"0", "1", "2", "3"}:
                    op_txt = input("Error: Opción inválida. Vuelva a seleccionar: ")

                if op_txt == "1":
                    reportes.imprimir_datos_estacionamiento(estacionamientos)
                elif op_txt == "2":
                    reportes.imprimir_usuarios(usuarios_registrados, VHC_JSON)
                elif op_txt == "3":
                    if estacionamientos:
                        sel_est = estacionamiento.elegir_estacionamiento(estacionamientos)
                        nom_archivo = input("Ingrese el nombre del archivo TXT de salida: ").strip()
                        if not nom_archivo.endswith(".txt"):
                            nom_archivo += ".txt"
                        try:
                            with open(nom_archivo, "a", encoding="utf-8") as f_out:
                                reportes.reporte_tarifas_archivo(f_out, sel_est, estacionamientos)
                            print(f"Reporte impreso correctamente en '{nom_archivo}'.")
                        except OSError as err:
                            print(f"Error al escribir el archivo: {err}")
                    else:
                        print("\nNo hay estacionamientos disponibles.")

        # --- SALIR ---
        elif opcion_principal == "0":
            print("\nCerrando sesión de administrador. ¡Hasta luego!")

menu_principal()
