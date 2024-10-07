import pickle
import pandas as pd

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

def modify_user():
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pickle.load(archivo)
    except:
        print('El archivo usuarios.ispc no existe')
    

def delete_user():
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pickle.load(archivo)
    except:
        print('El archivo usuarios.ispc no existe')
    

def search_user():
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
    
    
        
        

usuario1 = (UserManager('ema', 'xd', 'ema@xd'))
#usuario = Users(1, 'ema', 'xd', 'ema@xd')

#usuario2 = str(Users(2, 'juan', 'xdjuan', 'juan@xd')) + '\n'
usuario2 = UserManager('juan', 'xdjuan', 'juan@xd')


#add_user(usuario1)
#add_user(usuario2)

#print(f'usuario {usuario2}')
#add_user(usuario2)

#show_all_users()