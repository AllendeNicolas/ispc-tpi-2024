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


# FUNCION PARA AGREGAR USUARIO
def add_user(usuario):

    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
            
            # CUANDO EXISTE EL ARCHIVO, ASIGNA VALOR PARA CUMPLIR LA CONDICION DEL IF E INCREMENTAR EL VALOR +1 
            nuevoId = 2
    
    # SI DA ERROR ABRIR EL ARCHIVO CREA UN DF VACIO PARA CONTINUAR CON LA CARGA
    except:
        df_usuarios = pd.DataFrame({'id':[], 'username':[], 'dni':[], 'password':[], 'email':[]})
        
        # ASIGNA VALOR AL PRIMER REGISTRO PARA QUE NO QUEDE COMO NaN
        nuevoId = 1

    # INCREMENTA EL VALOR DEL ID +1 EN FUNCIÓN DEL MAYOR ID REGISTRADO
    if nuevoId > 1:
        nuevoId = (df_usuarios['id'].max()) + 1

    nuevo_usuario = {'id': nuevoId, 'username': usuario.username, 'dni': usuario.dni, 'password': usuario.get_password(), 'email': usuario.email}
    
    df_usuarios = df_usuarios._append(nuevo_usuario, ignore_index=True)
    
    # OREDENA EL DF POR DNI
    df_usuarios = df_usuarios.sort_values('dni')

    with open('usuarios.ispc', 'wb') as archivo:
        pickle.dump(df_usuarios, archivo)


# FUNCION PARA MODIFICAR DATOS DE USUARIO
def modificarUsuarioConMenu():

    # ABRE EL ARCHIVO BINARIO DE USUARIOS
    try:
        usuario = input('Ingresa el username a modificar:')

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
              \n2) DNI
              \n3) Contraseña
              \n4) Email
              \n5) Volver al menú anterior\n''')
            
            opcion = input('Ingresa una opción:')

            
            if opcion == '1':
                nuevo_dato = input('Ingresa el nuevo nombre de usuario:')

                df_usuarios.loc[usuario_cargado.index, 'username'] = nuevo_dato

            if opcion == '2':
                nuevo_dato = input('Ingresa el nuevo DNI:')

                df_usuarios.loc[usuario_cargado.index, 'dni'] = nuevo_dato

            elif opcion == '3':
                nuevo_dato = input('Ingresa la nueva contraseña:')

                df_usuarios.loc[usuario_cargado.index, 'password'] = nuevo_dato
            
            elif opcion == '4':
                nuevo_dato = validar_email('Ingresa el nuevo email:')

                df_usuarios.loc[usuario_cargado.index, 'email'] = nuevo_dato
                

            elif opcion == '5':
                # GUARDA EL DF MODIFICADO EN EL ARCHIVO BINARIO REEMPLAZANDO EL CONTENIDO ANTERIOR 
                with open('usuarios.ispc', 'wb') as archivo:
                    pickle.dump(df_usuarios, archivo)
        
                break

            else:
                print('Opción incorrecta')     
    

# FUNCION PARA ELIMINAR USUARIO
def eliminarUsuarioConMenu():

    # ABRE EL ARCHIVO BINARIO DE USUARIOS
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
            
            while True:
                
                print("-" * 30 ,"ELIMINAR USUARIO","-" * 34)
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



# -----------------------------  MENÚS DE OPCIONES ------------------------------------


# PENDIENTE METER MENU DENTRO DE LA FUNCION ADD_USER Y MODIFICAR EL NOMBRE DE DICHA FUNCION
def menuRegistrarUsuario():
    '''
    Muestra el menú de registro de usuarios y sus campos para completar
    '''


    try:
        print("-" * 30 ,"REGISTRAR UN NUEVO USUARIO","-" * 34)
        print("-" * 22 ,"Por favor a continuación ingrese sus datos","-" * 26)

        usuario = input('Nombre de usuario:')
        dni = int(input('DNI:'))
        contrasena = input('Contraseña:')
        email = validar_email('Email: ')

        usuario_obj = Usuario(usuario, dni, contrasena, email)
    except:
        print('Ocurrió un error en la carga de datos, por favor vuelve a intentar.')
    
    else:
        add_user(usuario_obj)



def menuCrudUsuarios():
    '''
    Muestra el menú del CRUD de usuarios y las opciones disponibles
    '''
    

    while True:
        print("-" * 30 ,"CRUD DE USUARIOS","-" * 34)

        print('''   
                    1) Registrar usuario\n
                    2) Modificar usuario\n
                    3) Eliminar usuario\n
                    4) Volver al menú anterior\n''')
        
        print("-" * 80)

        option = (input("Ingrese una opción: "))
        
        print("-" * 80)

       
        if option == "1":
            menuRegistrarUsuario()
        
        elif option == "2":
            modificarUsuarioConMenu()
        
        elif option == "3":
            eliminarUsuarioConMenu()

        elif option == "4":
            break
        else:
            print("Opción inválida, intente nuevamente.")



