import pandas as pd
import pickle
from datetime import datetime

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
        with open('usuarios.ispc', 'rb') as archivo:
            usuarios = pickle.load(archivo)
    except FileNotFoundError:
        usuarios = pd.DataFrame(columns=['username', 'password'])
    return usuarios

# Función para registrar accesos
def registrarAcceso(username):
    try:
        with open('accesos.ispc', 'rb') as archivo:
            df_accesos = pd.DataFrame(pickle.load(archivo))
            
    # SI DA ERROR ABRIR EL ARCHIVO CREA UN DF VACIO PARA CONTINUAR CON LA CARGA
    except:
        df_accesos = pd.DataFrame({'usuario': [], 'acceso': []})
    

    nuevo_acceso = {'usuario': username, 'acceso': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    
    df_accesos = df_accesos._append(nuevo_acceso, ignore_index=True)
    
    try:
        with open('accesos.ispc', 'wb') as archivo:
            pickle.dump(df_accesos, archivo)
    
    except Exception as e:
        print(f"Error al registrar acceso: {e}")

# Función para registrar intentos fallidos
def registrar_intento_fallido(username, password):
    intento = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Usuario: {username}, Clave: {password}\n"
    with open('logs.txt', 'a') as file:
        file.write(intento)

# Función principal para el control de acceso
def control_acceso(username, password):
    usuarios = cargar_usuarios()
    if not usuarios.empty and ((usuarios['username'] == username) & (usuarios['password'] == password)).any():
        print("Bienvenido ha ingresado a la aplicación")
        registrarAcceso(username)
    else:
        print("Acceso denegado")
        registrar_intento_fallido(username, password)

def mostrarAccesos():
    try:
        with open('accesos.ispc', 'rb') as archivo:
            accesos = pickle.load(archivo)
    except FileNotFoundError:
        print('El archivo no existe u ocurrió un error.')

    else:
        print("-" * 30 ,"REGISTROS DE ACCESOS","-" * 34)
        print(accesos)


def mostrarLogsFallidos():
    try:
        with open('logs.txt', 'r') as archivo:
            print("-" * 30 ,"INTENTOS FALLIDOS","-" * 34)
            for linea in archivo:
                print(linea)
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
