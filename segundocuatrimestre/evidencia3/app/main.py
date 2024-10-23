from menu_evidencia2 import display_menu_ev2
import ordenamiento

def display_menu():
    while True:
        print("-" * 10 ,"Menu Principal","-" * 44)
        print("1. Ordenamiento de usuarios")
        print("2. Buscar usuario")
        print("3. Cargar registros pluviales de un año")
        print("4. Ver graficos de registros pluviales")
        print("5. Ir al menú de la evidencia 2")
        print("6. Salir")
        print("-" * 70)
        option = (input("Ingrese una opcion: "))
        print("-" * 70)
        
        if option == "1":
            ordenamiento.ordenar()

        elif option == "2":
            pass

        elif option == "3":
            pass
        
        elif option == "4":
            pass
        elif option == "5":
            display_menu_ev2()

        elif option == "6":
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    display_menu()
