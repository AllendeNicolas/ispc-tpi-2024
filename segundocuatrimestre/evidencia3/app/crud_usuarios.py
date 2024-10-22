import pickle
import pandas as pd
import re

class UserManager:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class Acceso:
    def __init__(self, fecha_ingreso, fecha_salida, usuario_logueado):
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = fecha_salida
        self.usuario_logueado = usuario_logueado


# FUNCION PARA VALIDADAR EMAIL
def validar_email(email):
    """Comprobar si el correo electronico tiene formato válido."""

    # Expresión regular para validar  Email
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

    # Si la cadena coincide con una expresión regular, es un correo electrónico válido.
    if re.match(regex, email):
        return True

    else:
        return False




def add_user(usuario):

    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pickle.load(archivo)
    except:
        df_usuarios = pd.DataFrame({'username':[], 'password':[], 'email':[]})

    nuevo_usuario = {'username': usuario.username, 'password': usuario.password, 'email': usuario.email}
    df_final = df_usuarios._append(nuevo_usuario, ignore_index=True)
    
    with open('usuarios.ispc', 'wb') as archivo:
        pickle.dump(df_final, archivo)

# FUNCION PARA MODIFICAR DATOS DE USUARIO
def modify_user(usuario):

    # ABRE EL ARCHIVO BINARIO DE USUARIOS
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
        
        usuario_cargado = df_usuarios[df_usuarios['username'] == usuario]


        print(f'''Datos del usuario
              \n- Nombre de usuario: {usuario_cargado.to_numpy()[0][0]}
                \n- Email: {usuario_cargado.to_numpy()[0][2]}\n''')
        
    #EN CASO DE QUE NO ENCUENTRE COINCIDENCIA O NO EXISTA EL ARCHIVO MUESTRA MSJ DE ERROR
    except:
        print('El archivo usuarios.ispc o el usuario no existe')

    else:
        
        while True:
            
            print('''Que dato/s vas a modificar
              \n1) Nombre de usuario
              \n2) Contraseña
              \n3) Email
              \n4) Volver al menú principal\n''')
            
            opcion = input('Ingresa una opción:')

            
            if opcion == '1':
                nuevo_dato = input('Ingresa el nuevo nombre de usuario:')

                df_usuarios.loc[usuario_cargado.index, 'username'] = nuevo_dato

            elif opcion == '2':
                nuevo_dato = input('Ingresa la nueva contraseña:')

                df_usuarios.loc[usuario_cargado.index, 'password'] = nuevo_dato

            elif opcion == '3':
                nuevo_dato = input('Ingresa el nuevo email:')

                while not validar_email(nuevo_dato):
                    print('EL FORMATO DEL EMAIL ES INCORRECTO')
                    nuevo_dato = input('Ingresa email nuevamente:')

                df_usuarios.loc[usuario_cargado.index, 'email'] = nuevo_dato

            elif opcion == '4':
                # GUARDA EL DF MODIFICADO EN EL ARCHIVO BINARIO REEMPLAZANDO EL CONTENIDO ANTERIOR 
                with open('usuarios.ispc', 'wb') as archivo:
                    pickle.dump(df_usuarios, archivo)
        
                break

            else:
                print('Opción incorrecta')     
    

def delete_user(usuario):
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pickle.load(archivo)
    except:
        print('El archivo usuarios.ispc no existe')
    

def search_user(usuario):
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pickle.load(archivo)
    except:
        print('El archivo usuarios.ispc no existe')
    

def show_all_users():
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pickle.load(archivo)
            print(df_usuarios)
    except:
        print('El archivo usuarios.ispc no existe')
