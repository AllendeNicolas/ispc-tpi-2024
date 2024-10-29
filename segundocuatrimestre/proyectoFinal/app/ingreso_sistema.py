

def menu_ingreso_sist():
    print('')
    print("-" * 25 ,"INGRESAR  AL SIST CON LOS DATOS DE USUARIO","-" * 25)
    print('')

    # DEFINE BANDERA PARA EL CONTROL DE ACCESO
    usuario_ok = False

    user = input('Nombre de usuario: ')
    pass_user = input('Contraseña: ')
    # CON LOS DATOS DE USER Y PASS VALIDAMOS QUE LOS DATOS EXISTEN Y PONEMOS LA BANDERA usuario_ok EN True
    # EJECUTAMOS MENU, CON IF/ELSE SEGÚN LA CONDICION DE LA BANDERA
    # SI NO EXISTE EL USUARIO, PASS ERRONEA O DA ERROR INFORMAR CON MSJ Y DAR OPCIÓN DE VOLVER A INTENTAR O VOLVER AL MENÚ PRINCIPAL 


    # SI SE VALIDAN LOS DATOS CORRECTAMENTE
    if usuario_ok == True:
        while True:

            # IMPRIME MENÚ DE OPCIONES POR CONSOLA
            print('')
            print("-" * 25 ,"BASE DE DATOS","-" * 25)
            print("-" * 30 ,"Menú","-" * 34)
            print('''   
                        1) Ir a la Gestión de Base de datos\n
                        2) Volver al Menú principal\n
                        3) Salir de la aplicación\n''')
            
            print("-" * 80)

            option = (input("Ingrese una opción: "))
            
            print("-" * 70)
            
            # OPCIÓN 1 - 
            if option == "1":
                pass
            
            # OPCIÓN 2 - VUELVE AL MENÚ PRINCIPAL
            elif option == "2":
                pass

    # ANALIZAR SI ES CORRECTO QUE SALGA DE LA APP EN ESTA INSTANCIA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # OPCIÓN 3 - 
            elif option == "3":
                print("Saliendo de la aplicación.")
                break
            else:
                print("Opción inválida, intente nuevamente.")
    
    # ELSE CORRESPONDE A usuario_ok == False
    else:
        pass