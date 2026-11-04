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
    
    # 4. Lista de reservas
    reservar = []
    reservas_canceladas = []

    # 5. Lista de tarifas y cobros
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
                # El administrador elige sobre qué estacionamiento va a trabajar
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
                    
                    # 2. RESERVAS
                    elif op_sub == "2":
                        op_res = "-1"
                        while op_res != "0":
                            print(f"\n -------- MENU RESERVAS ({nombre_actual}) --------")
                            print("1. Generar una reserva.")
                            print("2. Consultar reservas.")
                            print("3. Modificar reserva.")
                            print("4. Cancelar una reserva.")
                            print("0. Volver atrás.")
                            op_res = input("Opción: ")
                            
                            if op_res == "1":
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
                                usuarios.alta(usuarios_registrados)
                            elif op_usu == "2":
                                usuarios.alta(usuarios_registrados)
                            elif op_usu == "3":
                                usuarios.alta(usuarios_registrados)
                            elif op_usu == "4":
                                vehiculos.ingresar_vehiculo(VHC_JSON, usuarios_registrados)
                            elif op_usu == "5":
                                vehiculos.mostrar_vehiculos(VHC_JSON, usuarios_registrados)
                            elif op_usu == "6":
                                usuarios.alta(usuarios_registrados)
                            elif op_usu == "7":
                                usuarios.alta(usuarios_registrados)
                            elif op_usu == "8":
                                vehiculos.eliminar_vehiculo(VHC_JSON)
                                
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
            reportes.mostrar_reportes(estacionamientos, tipos, dnis, estados, reservar, reservas_canceladas, lista_cobros)

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
                print("1. Imprimir informe de un estacionamiento")
                print("2. Imprimir todos los estacionamientos")
                print("3. Imprimir base de datos (Usuarios y Vehículos)")
                print("0. Volver al menú principal")
                print("="*60)
                
                op_txt = input("Seleccione una opción: ")
                while op_txt not in {"0", "1", "2", "3"}:
                    op_txt = input("Error: Opción inválida. Vuelva a seleccionar: ")

                if op_txt == "1":
                    reportes.imprimir_datos_estacionamiento(estacionamientos, reservar, lista_cobros)
                elif op_txt == "2":
                    reportes.imprimir_estacionamientos(estacionamientos, reservar, lista_cobros)
                elif op_txt == "3":
                    reportes.imprimir_usuarios(usuarios_registrados, VHC_JSON)

        # --- SALIR ---
        elif opcion_principal == "0":
            print("\nCerrando sesión de administrador. ¡Hasta luego!")

if __name__ == "__main__":
    menu_principal() 
