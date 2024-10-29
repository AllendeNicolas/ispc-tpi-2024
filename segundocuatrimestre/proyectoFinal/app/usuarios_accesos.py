

def menu_usuarios_accesos():

    while True:

        # IMPRIME MENÚ DE OPCIONES POR CONSOLA
        print('')
        print("-" * 25 ,"USUARIOS Y ACCESOS DE LA APP","-" * 25)
        print("-" * 30 ,"Menú","-" * 34)
        print('''   
                    1) Acceder al CRUD de los Usuarios en POO\n
                    2) Mostrar los datos de Acceso\n
                    3) Ordenamiento y Búsqueda de Usuarios\n
                    4) Volver al Menú principal\n''')
        
        print("-" * 80)

        option = (input("Ingrese una opción: "))
        
        print("-" * 70)
        
        # OPCIÓN 1 - CRUD USUARIOS POO
        if option == "1":
            pass
        
        # OPCIÓN 2 - DATOS DE ACCESO
        elif option == "2":
            pass
        
        # OPCIÓN 3 - ORDENAMIENTO Y BUSQUEDA DE USUSARIOS
        elif option == "3":
            pass
        
        # OPCIÓN 4 - VUELVE AL MENÚ PRINCIPAL
        elif option == "4":
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción inválida, intente nuevamente.")
