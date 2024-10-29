# IMPORTAMOS LOS MODULOS
from usuarios_accesos import menu_usuarios_accesos
from ingreso_sistema import menu_ingreso_sist
from analisis_datos import menu_analisis_datos


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
            menu_usuarios_accesos()
        
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