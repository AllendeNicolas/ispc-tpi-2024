import pandas as pd
import pickle
from datetime import datetime

# Función para cargar usuarios desde el archivo binario
def cargar_usuarios():
    try:
        with open('usuarios.ispc', 'rb') as file:
            usuarios = pickle.load(file)
    except FileNotFoundError:
        usuarios = pd.DataFrame(columns=['username', 'password'])
    return usuarios

# Función para registrar accesos
def registrar_acceso(username):
    acceso = pd.DataFrame({
        'usuario': [username],
        'acceso': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
    })
    try:
        with open('accesos.ispc', 'ab') as file:
            pickle.dump(acceso, file)
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
        registrar_acceso(username)
    else:
        print("Acceso denegado")
        registrar_intento_fallido(username, password)

'''# Pruebas de uso de aplicación
if __name__ == "__main__":
    # Datos de ingreso del usuario
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    control_acceso(username, password)'''
