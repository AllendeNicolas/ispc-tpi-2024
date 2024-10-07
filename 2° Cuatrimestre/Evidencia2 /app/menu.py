from crud_usuarios import *

'''class Menu:
    def __init__(self):
        self.user_manager = UserManager() #esto hace referencia a la clase que debe ser creada para el CRUD de los usuarios
        self.current_user = None #currente_user es para  representar al usuario que está actualmente autenticado en el sistema
        #None indica que no hay ningun usuario autenticado al iniciar el sistema
        #con esto se puede almacenar el logueo de un usuario, para eso hay que agregar esa linea en otras funciones '''

def display_menu():
    while True:
        print("----Menu Principal----")
        print("1. Ingresar al sistema")
        print("2. Registrar usuario")
        print("3. Modificar usuario")
        print("4. Eliminar usuario")
        print("5. Buscar usuario")
        print("6. Ver todos los usuarios")
        print("7. Salir")
        print("-----------------------")
        option = (input("Ingrese una opcion: "))
        #nombres de funciones siguientes ficticios, hay que crearlas con POO
        
        if option == "1":
            pass
        
        elif option == "2":
            usuario = input('Ingresa nombre de usuario:')
            contrasena = input('Ingresa una contraseña:')
            email = input('Ingresa tu email:')

            usuario_obj = UserManager(usuario, contrasena, email)
            add_user(usuario_obj)

        elif option == "3":
            modify_user()
        elif option == "4":
            delete_user()
        elif option == "5":
            search_user()
        elif option == "6":
            show_all_users()
            
        elif option == "7":
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción inválida, intente nuevamente.")
        """self es una referencia al objeto actual de una clase. 
        se llama a las funciones que serán creadas"""

display_menu()
