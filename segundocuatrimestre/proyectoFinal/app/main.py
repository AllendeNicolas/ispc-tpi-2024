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










# IMPORTAMOS LOS MODULOS
import gestionAcceso
import gestionUsuario
from ingreso_sistema import menu_ingreso_sist
from analisis_datos import menu_analisis_datos


def menuUsuariosAccesos():
    '''
    Muestra el menu de opciones par manipular datos de accesos y usuarios
    '''
    
    while True:

        # IMPRIME MENÚ DE OPCIONES POR CONSOLA
        print('')
        print("-" * 25 ,"USUARIOS Y ACCESOS DE LA APP","-" * 25)
        print('''   
                    1) Acceder al CRUD de los Usuarios en POO\n
                    2) Mostrar los datos de Acceso\n
                    3) Ordenamiento y Búsqueda de Usuarios\n
                    4) Volver al Menú principal\n''')
        
        print("-" * 80)

        option = (input("Ingrese una opción: "))
        
        print("-" * 80)
        
        # OPCIÓN 1 - CRUD USUARIOS POO
        if option == "1":
            gestionUsuario.menuCrudUsuarios()
    
        # OPCIÓN 2 - DATOS DE ACCESO
        elif option == "2":
            gestionAcceso.menuDatosAccesos()
        
        # OPCIÓN 3 - ORDENAMIENTO Y BUSQUEDA DE USUSARIOS
        elif option == "3":
            pass
        
        # OPCIÓN 4 - VUELVE AL MENÚ PRINCIPAL
        elif option == "4":
            break
        else:
            print("Opción inválida, intente nuevamente.")

def display_menu():

    print('')
    print("-" * 25 ,"BIENVENIDO AL PROYECTO FINAL","-" * 25)
    print('')

    while True:

        # IMPRIME MENÚ DE OPCIONES POR CONSOLA
        print("-" * 30 ,"Menú Principal","-" * 34)
        print('''   
                    1) Usuarios y Accesos de la Aplicación\n
                    2) Ingresar al sistema con los datos de usuario (GBD)\n
                    3)  Análisis de datos\n
                    4) Salir\n''')
        
        print("-" * 80)

        option = (input("Ingrese una opción: "))
        
        print("-" * 80)
        
        # OPCIÓN 1 - USUARIOS Y ACCESOS DE LA APP
        if option == "1":
            menuUsuariosAccesos()
        
        # OPCIÓN 2 - INGRESAR AL SIST CON USUARIO Y CONTRASEÑA
        elif option == "2":
            menu_ingreso_sist()
        
        # OPCIÓN 3 - ANALISIS DE DATOS, REGISTROS PLUVIALES
        elif option == "3":
            menu_analisis_datos()
        
        # OPCIÓN 4 - SALE DE LA APP
        elif option == "4":
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    display_menu()