from crud_usuarios import *
from accesos_funciones import *

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
            # Datos de ingreso del usuario
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            control_acceso(username, password)
        
        elif option == "2":
            usuario = input('Ingresa nombre de usuario:')
            contrasena = input('Ingresa una contraseña:')
            email = input('Ingresa tu email:')

            usuario_obj = UserManager(usuario, contrasena, email)
            add_user(usuario_obj)

        elif option == "3":
            print('Modificar usuario')
            usuario = input('Ingresa el username a modificar:')
            modify_user(usuario)
        elif option == "4":
            print('Eliminar usuario')
            usuario = input('Ingresa el username o email del usuario a eliminar:')
            delete_user(usuario)
        elif option == "5":
            print('Eliminar usuario')
            usuario = input('Ingresa el username o email del usuario a buscar:')
            search_user(usuario)
        elif option == "6":
            show_all_users()
            
        elif option == "7":
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción inválida, intente nuevamente.")
        """self es una referencia al objeto actual de una clase. 
        se llama a las funciones que serán creadas"""


if __name__ == "__main__":
    display_menu()
