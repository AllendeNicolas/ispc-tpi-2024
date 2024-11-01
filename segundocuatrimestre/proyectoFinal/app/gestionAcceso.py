import pandas as pd
import pickle
from datetime import datetime
import os.path as path

# DEFINIMOS DIRECTORIO ACTUAL DE SCRIPT PRINCIPAL
ubicacionMain = path.abspath(__file__)
directorioApp, nombre = path.split(ubicacionMain)


# APLICAR LA CLASE A LOS REGISTROS DE ACCESOS Y MODIFCAR ATRIBUTOS A LOS QUE SE USAN EN LA APP
class Acceso:
    def __init__(self, fecha_ingreso, fecha_salida, usuario_logueado):
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = fecha_salida
        self.__usuario_logueado = usuario_logueado

    # MODIFICA ATRIBUTO PRIVADO usuario_logueado
    def set_usuario_logueado(self, usuario):
        self.__usuario_logueado = usuario
    
    # RETORNA ATRIBUTO PRIVADO usuario_logueado
    def get_usuario_logueado(self):
        return self.__usuario_logueado
    

# Función para cargar usuarios desde el archivo binario
def cargar_usuarios():
    try:
        with open(directorioApp + '/usuarios.ispc', 'rb') as archivo:
            usuarios = pickle.load(archivo)
    except FileNotFoundError:
        usuarios = pd.DataFrame(columns=['username', 'password'])
    return usuarios

# Función para registrar accesos
def registrarAcceso(username):
    try:
        with open(directorioApp + '/accesos.ispc', 'rb') as archivo:
            df_accesos = pd.DataFrame(pickle.load(archivo))
            
    # SI DA ERROR ABRIR EL ARCHIVO CREA UN DF VACIO PARA CONTINUAR CON LA CARGA
    except:
        df_accesos = pd.DataFrame({'usuario': [], 'acceso': []})
    

    nuevo_acceso = {'usuario': username, 'acceso': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    
    df_accesos = df_accesos._append(nuevo_acceso, ignore_index=True)
    
    try:
        with open(directorioApp + '/accesos.ispc', 'wb') as archivo:
            pickle.dump(df_accesos, archivo)
    
    except Exception as e:
        print(f"Error al registrar acceso: {e}")
        input('\nPresiona ENTER para continuar...')

# Función para registrar intentos fallidos
def registrar_intento_fallido(username, password):
    intento = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Usuario: {username}, Clave: {password}\n"
    with open(directorioApp + '/logs.txt', 'a') as file:
        file.write(intento)

# Función principal para el control de acceso
def control_acceso(username, password):
    usuarios = cargar_usuarios()
    if not usuarios.empty and ((usuarios['username'] == username) & (usuarios['password'] == password)).any():
        print('-' * 80)
        print("BIENVENIDO HA INGRESADO A LA APLICACIÓN")
        registrarAcceso(username)
        return True
    else:
        print('-' * 80)
        print("ACCESO DENEGADO")
        registrar_intento_fallido(username, password)
        return False

def mostrarAccesos():
    try:
        with open(directorioApp + '/accesos.ispc', 'rb') as archivo:
            accesos = pickle.load(archivo)
    except FileNotFoundError:
        print('El archivo no existe u ocurrió un error.')

    else:
        print("-" * 30 ,"REGISTROS DE ACCESOS","-" * 34)
        print(accesos)
        input('\nPresiona ENTER para continuar...')


def mostrarLogsFallidos():
    try:
        with open(directorioApp + '/logs.txt', 'r') as archivo:
            print("-" * 30 ,"INTENTOS FALLIDOS","-" * 34)
            for linea in archivo:
                print(linea)
        input('\nPresiona ENTER para continuar...')
        
    except FileNotFoundError:
        print('El archivo no existe u ocurrió un error.')

# MENÚ DE OPCIONES
def menuDatosAccesos():
    '''
    Muestra el menú de datos de acceso y las opciones disponibles
    '''
    while True:
        print("-" * 30 ,"DATOS DE ACCESOS","-" * 32)

        print('''   
                    1) Mostrar accesos\n
                    2) Mostrar los logs de intentos fallidos\n
                    3) Volver al menú anterior\n''')
        
        print("-" * 80)

        option = (input("Ingrese una opción: "))
        
        print("-" * 80)

       
        if option == "1":
            mostrarAccesos()
    
        elif option == "2":
            mostrarLogsFallidos()
        
        elif option == "3":
            break
        else:
            print("Opción inválida, intente nuevamente.")


def menuIngresoSist():
    from menu_conexion_bd import conectar_base_datos
    print('')
    print("-" * 25 ,"INGRESAR  AL SISTEMA CON LOS DATOS DE USUARIO","-" * 25)
    print('')

    # DEFINE BANDERA PARA EL CONTROL DE ACCESO
    usuario_ok = False

    user = input('Nombre de usuario: ')
    pass_user = input('Contraseña: ')
    
    usuario_ok = control_acceso(user, pass_user)


    # SI SE VALIDAN LOS DATOS CORRECTAMENTE
    if usuario_ok == True:
        conectar_base_datos()
