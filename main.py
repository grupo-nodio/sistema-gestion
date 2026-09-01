import estacionamiento
import tarifas
import reservas
import usuarios
import vehiculos
import reportes

def menu_principal():
    # --- INICIALIZACIÓN DE LA BASE DE DATOS EN MEMORIA ---
    
    # 1. Listas de Estacionamientos
    estacionamientos = [[None], [None], [None], [None]] 
    horarios = [None]
    
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

    # --- BUCLE DEL MENÚ PRINCIPAL (NIVEL 1) ---
    opcion_principal = "-1"
    
    while opcion_principal != "0":
        print("\n" + "="*60)
        print("PARK DIRECT - SISTEMA DE GESTIÓN - PANEL ADMINISTRADOR")
        print("="*60)
        print("1. Seleccionar un estacionamiento existente")
        print("2. Crear un estacionamiento nuevo")
        print("0. Salir del sistema")
        print("="*60)
        
        opcion_principal = input("Seleccione una opción: ")
        while opcion_principal not in ["0", "1", "2"]:
            opcion_principal = input("Error: Opción inválida. Vuelva a seleccionar: ")

        # --- CREAR ESTACIONAMIENTO ---
        if opcion_principal == "2":
            estacionamiento.crear_estacionamiento(estacionamientos, horarios)

        # --- SELECCIONAR ESTACIONAMIENTO (NIVEL 2 - SUBSISTEMAS) ---
        elif opcion_principal == "1":
            if len(estacionamientos[0]) > 1: 
                # El administrador elige sobre qué estacionamiento va a trabajar
                sel = estacionamiento.elegir_estacionamiento(estacionamientos)
                nombre_actual = estacionamientos[0][sel]
                
                op_sub = "-1"
                while op_sub != "0":
                    print("\n" + "="*40)
                    print(f" ADMINISTRANDO: {nombre_actual.upper()}")
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
                        if modificar.lower() in ['y', 's', 'si', 'yes']:
                            estacionamiento.modificar(sel, estacionamientos, horarios)
                    
                    # 2. RESERVAS
                    elif op_sub == "2":
                        op_res = "-1"
                        while op_res != "0":
                            print(f"\n--- RESERVAS ({nombre_actual}) ---")
                            print("1. Crear reserva manual")
                            print("0. Volver atrás")
                            op_res = input("Opción: ")
                            if op_res == "1":
                                reservas.generar_reserva()
                    
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
                            print("6. Dar de baja al usuario.")
                            print("7. Reactivar usuario dado de baja")
                            print("0. Volver atrás")
                            op_usu = input("Opción: ")
                            
                            if op_usu == "1":
                                usuarios.alta(nombres, apellidos, dnis, emails, telefonos, estados)
                            elif op_usu == "2":
                                usuarios.mostrar_usuarios(nombres, apellidos, dnis, emails, telefonos, estados)
                            elif op_usu == "3":
                                usuarios.modificar_usuario(nombres, apellidos, dnis, emails, telefonos, estados)
                            elif op_usu == "4":
                                # Acá se ve la conexión: el vehículo pide un DNI que debe existir en usuarios
                                vehiculos.ingresar_vehiculo(patentes, tipos, dni_vehiculos, dnis)
                            elif op_usu == "5":
                                vehiculos.mostrar_vehiculos(patentes, tipos, dni_vehiculos)

                            elif op_usu=="6":
                                usuarios.baja_usuarios(dnis,estados)

                            #Para dar de alta nuevamente a un usuario antiguo.    
                            elif op_usu=="7":
                                usuarios.quitar_baja(nombres,apellidos,dnis,emails,telefonos,estados)
                                
                    # 4. TARIFAS Y COBROS
                    elif op_sub == "4":
                        print(f"\n[ Módulo Tarifas para {nombre_actual} - En desarrollo ]")
                        # Aquí podrás enlazar tus funciones de tarifas.py

            else:
                print("\nNo hay estacionamientos registrados en el sistema. Por favor, cree uno primero.")

        # --- SALIR ---
        elif opcion_principal == "0":
            print("\nCerrando sesión de administrador. ¡Hasta luego!")

if __name__ == "__main__":
    menu_principal()