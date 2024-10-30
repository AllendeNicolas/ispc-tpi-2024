import pickle
import pandas as pd
import re

class Usuario:
    def __init__(self, username, dni, password, email):
        self.id = None
        self.username = username
        self.dni = dni
        self.__password = password
        self.email = email

    # MODIFICA ATRIBUTO PRIVADO CONTRASEÑA
    def set_password(self, password):
        self.__password = password
    
    # RETORNA ATRIBUTO PRIVADO CONTRASEÑA
    def get_password(self):
        return self.__password


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


# FUNCION PARA VALIDADAR EMAIL
def validar_email(msj):
    """Comprobar si el correo electronico tiene formato válido.
    Se pasa por parámetro un mensaje para mostrar en el input"""

    while True:
        email = input(msj)
        # Expresión regular para validar  Email
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

        # Si la cadena coincide con una expresión regular, es un correo electrónico válido.
        if re.match(regex, email):
            break
        else:
            print('EL FORMATO DEL EMAIL ES INCORRECTO, VUELVE A INTENTARLO\n')

    return email

'''
PARA RESOLVER EL ULTIMO ID CARGADO Y ASIGNAR ID VIEJO + 1 AL NUEVO REGISTRO
# DEVUELVE EL MAXIMO VALOR POR COLUMNA
print(dataframe.max()) SUPONGO QUE PARA QUE DEVUELVA EL MAYOR ID dataframe["id"].max() !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

'''
PARA ORDENAR EL DATAFRAME POR DNI
df.sort_values(by = "A") donde "A" es el nombre de una columna
'''

# FUNCION PARA AGREGAR USUARIO
def add_user(usuario):

    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
    
    # SI DA ERROR ABRIR EL ARCHIVO CREA UN DF VACIO PARA CONTINUAR CON LA CARGA
    except:
        df_usuarios = pd.DataFrame({'id':[], 'username':[], 'dni':[], 'password':[], 'email':[]})

    nuevoId = (df_usuarios['id'].max()) + 1

    nuevo_usuario = {'id': nuevoId, 'username': usuario.username, 'dni': usuario.dni, 'password': usuario.get_password(), 'email': usuario.email}
    
    df_final = df_usuarios._append(nuevo_usuario, ignore_index=True)
    
    # OREDENA EL DF POR DNI
    df_final.sortvalues(by = 'dni')

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
            
            print('''Que dato/s vas a modificar?
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
                nuevo_dato = validar_email('Ingresa el nuevo email:')

                df_usuarios.loc[usuario_cargado.index, 'email'] = nuevo_dato

            elif opcion == '4':
                # GUARDA EL DF MODIFICADO EN EL ARCHIVO BINARIO REEMPLAZANDO EL CONTENIDO ANTERIOR 
                with open('usuarios.ispc', 'wb') as archivo:
                    pickle.dump(df_usuarios, archivo)
        
                break

            else:
                print('Opción incorrecta')     
    

# FUNCION PARA ELIMINAR USUARIO
def delete_user():

    # ABRE EL ARCHIVO BINARIO DE USUARIOS
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
            
            while True:
            
                print('''Indique que parametro va a utilizar para eliminar usuario
                        \n1) Nombre de usuario
                        \n2) Email
                        \n3) Volver al menú principal\n''')
                print("-----------------------")

                opcion = input('Ingresa una opción:')
                print("-----------------------")


                if opcion == '1':
                    dato = input('Ingresa el nombre de usuario:')
                    usuario_cargado = df_usuarios[df_usuarios['username'] == dato]


                    print(f'''Datos del usuario
                            \n- Nombre de usuario: {usuario_cargado.to_numpy()[0][0]}
                            \n- Email: {usuario_cargado.to_numpy()[0][2]}\n''')
                    
                    df_usuarios = df_usuarios.drop(usuario_cargado.index)
                    # GUARDA EL DF MODIFICADO EN EL ARCHIVO BINARIO REEMPLAZANDO EL CONTENIDO ANTERIOR 
                    with open('usuarios.ispc', 'wb') as archivo:
                        pickle.dump(df_usuarios, archivo)
                    print('El usuario se eliminó con exito')

                    break

                elif opcion == '2':
                    dato = validar_email('Ingresa el email:')
                    usuario_cargado = df_usuarios[df_usuarios['email'] == dato]


                    print(f'''Datos del usuario
                            \n- Nombre de usuario: {usuario_cargado.to_numpy()[0][0]}
                            \n- Email: {usuario_cargado.to_numpy()[0][2]}\n''')
                    
                    df_usuarios = df_usuarios.drop(usuario_cargado.index)
                    # GUARDA EL DF MODIFICADO EN EL ARCHIVO BINARIO REEMPLAZANDO EL CONTENIDO ANTERIOR 
                    with open('usuarios.ispc', 'wb') as archivo:
                        pickle.dump(df_usuarios, archivo)
                    print('El usuario se eliminó con exito')

                    break

                elif opcion == '3':
                    break

                else:
                    print('Opción incorrecta')
        
        
    #EN CASO DE QUE NO ENCUENTRE COINCIDENCIA O NO EXISTA EL ARCHIVO MUESTRA MSJ DE ERROR
    except:
        print('El archivo usuarios.ispc o el usuario no existe')
    

# FUNCION PARA BUSCAR USUARIO
def search_user():
    # ABRE EL ARCHIVO BINARIO DE USUARIOS
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
            
            while True:
            
                print('''Indique que parametro va a utilizar para buscar usuario
                        \n1) Nombre de usuario
                        \n2) Email
                        \n3) Volver al menú principal\n''')
                print("-----------------------")

                opcion = input('Ingresa una opción:')
                print("-----------------------")


                if opcion == '1':
                    dato = input('Ingresa el nombre de usuario:')
                    usuario_cargado = df_usuarios[df_usuarios['username'] == dato]

                    print(f'''Datos del usuario
                            \n- ID: {usuario_cargado.index[0]}
                            \n- Nombre de usuario: {usuario_cargado.to_numpy()[0][0]}
                            \n- Contraseña: {usuario_cargado.to_numpy()[0][1]}
                            \n- Email: {usuario_cargado.to_numpy()[0][2]}\n''')
                    
                    input('Presiona una tecla para continuar...')
                    break

                elif opcion == '2':
                    dato = validar_email('Ingresa el email:')
                    usuario_cargado = df_usuarios[df_usuarios['email'] == dato]

                    
                    print(f'''Datos del usuario
                            \n- ID: {usuario_cargado.index[0]}
                            \n- Nombre de usuario: {usuario_cargado.to_numpy()[0][0]}
                            \n- Contraseña: {usuario_cargado.to_numpy()[0][1]}
                            \n- Email: {usuario_cargado.to_numpy()[0][2]}\n''')
                    
                    input('Presiona una tecla para continuar...')
                    break

                elif opcion == '3':
                    break

                else:
                    print('Opción incorrecta')
        
    #EN CASO DE QUE NO ENCUENTRE COINCIDENCIA O NO EXISTA EL ARCHIVO MUESTRA MSJ DE ERROR
    except:
        print('El archivo usuarios.ispc o el usuario no existe')
    


# FUNCION PARA MOSTRAR TODOS LOS USUARIOS
def show_all_users():
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pickle.load(archivo)
            print(df_usuarios)
        input('Presiona una tecla para continuar...')
        
    except:
        print('El archivo usuarios.ispc no existe')



def menuRegistrarUsuario():

    print("-" * 30 ,"REGISTRAR UN NUEVO USUARIO","-" * 34)
    print("-" * 22 ,"Por favor a continuación ingrese sus datos","-" * 26)

    usuario = input('Nombre de usuario:')
    dni = int(input('DNI:'))
    contrasena = input('Contraseña:')
    email = validar_email('Email')

    usuario_obj = Usuario(usuario, dni, contrasena, email)

    add_user(usuario_obj)

menuRegistrarUsuario()