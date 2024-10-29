def menu_analisis_datos():

    while True:

        # IMPRIME MENÚ DE OPCIONES POR CONSOLA
        print('')
        print("-" * 25 ,"ANÁLISIS DE DATOS","-" * 25)
        print("-" * 30 ,"Menú","-" * 34)
        print('''   
                    1) El usuario elige el año para analizar los registros pluviales\n
                    2) Volver al Menú principal\n''')
        print("-" * 80)

        option = (input("Ingrese una opción: "))
        
        print("-" * 70)
        
        # OPCIÓN 1 - CRUD USUARIOS POO
        if option == "1":
            pass
        
        # OPCIÓN 2 - VUELVE AL MENÚ PRINCIPAL
        elif option == "2":
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción inválida, intente nuevamente.")
