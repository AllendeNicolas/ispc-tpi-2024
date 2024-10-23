from menu_evidencia2 import display_menu_ev2
from ordenamiento_busqueda import ordenar
from registros_pluviales import registros_pluviales


def display_menu():
    while True:
        print("-" * 25 ,"Menu Principal","-" * 29)
        print('''   
                    1) Ordenar usuarios\n
                    2) Buscar usuario\n
                    3) Registros pluviales\n
                    4) Ir al menú de la evidencia 2\n
                    5) Salir\n''')
        
        print("-" * 70)

        option = (input("Ingrese una opcion: "))
        
        print("-" * 70)
        
        if option == "1":
            ordenar()

        elif option == "2":
            pass

        elif option == "3":
            registros_pluviales()

        elif option == "4":
            display_menu_ev2()

        elif option == "5":
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    display_menu()