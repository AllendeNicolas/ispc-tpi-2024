"""se invoca esta funcion en los puntos del sistema que se desee 
tener la opcion volver al menu principal"""""

def logged_in_menu(self):
        while True:
            print("\n--- Menú de Usuario ---")
            print("1. Volver al menú principal")
            print("2. Salir de la aplicación")
            option = input("Seleccione una opción: ")

            if option == "1":
                break
            elif option == "2":
                print("Saliendo de la aplicación.")
                exit()
            else:
                print("Opción inválida, intente nuevamente.")



# esta es la manera de invocarla: self.logged_in_menu()
