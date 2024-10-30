'''
1. Usuarios y Accesos de la Aplicación
    
    a. Acceder al CRUD de los Usuarios en POO
        
        i. Agregar un nuevo usuario,
        
        ii. Modificar un usuario,
        
        iii. Eliminar un usuario (dado su username o email)
        
        iv. Volver al Menú principal o al anterior
    
    
    b. Mostrar los datos de Accesos
        
        i. Mostrar los Accesos (datos de accesos.ispc)
        
        ii. Mostrar los logs de intentos fallidos (datos de logs.txt)
        
        iii. Volver al Menú principal o al anterior
    
    
    c. Ordenamiento y Búsqueda de Usuarios
        
        i. Ordenar los Usuarios
            1. Ordenar por username
        
        ii. Buscar y Mostrar los Usuarios
            
            1. Búsqueda de Usuarios por DNI y mostrar los datos de ese
            usuario si existe o dejar un mensaje que no existe el usuario
            buscado.
            
            2. Búsqueda de Usuarios por username y mostrar los datos de ese
            usuario si existe o dejar un mensaje que no existe el usuario
            buscado.
            
            3. Buscar por email y mostrar los datos de ese usuario si existe o
            dejar un mensaje que no existe el usuario buscado.
            
            4. Mostrar todos los usuarios:
                
                a. Los usuarios del archivo usuarios.ispc
                
                b. Los usuarios del archivo usuariosOrdenadosPorUsername.ispc (si existe)
        
        iii. Volver al Menú principal o al anterior

    
    d. Volver al Menú principal'''



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
