import pickle
import pandas as pd
import re
from operator import itemgetter

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


# FUNCION DE ORDENAMIENTO CON METODO BURBUJA HECHA POR NOSOTROS
def ordenar_burbuja():
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
    
        #CONVIERTE EL DATAFRAME EN UNA LISTA DE LISTAS
        usuarios_cargados_lista = df_usuarios.values.tolist()

    #EN CASO DE QUE NO ENCUENTRE COINCIDENCIA O NO EXISTA EL ARCHIVO MUESTRA MSJ DE ERROR
    except:
        print('El archivo usuarios.ispc o el usuario no existe')

    else:

        for i in range(len(usuarios_cargados_lista) - 1):

            for j in range(len(usuarios_cargados_lista) - 1):

                if usuarios_cargados_lista[j][1] > usuarios_cargados_lista[j+1][1]:
                    usuarios_cargados_lista[j], usuarios_cargados_lista[j+1] = usuarios_cargados_lista[j+1], usuarios_cargados_lista[j]


        # CONVIERTE LA LISTA EN DATAFRAME PASANDO NUEVAMENTE LOS NOMBRES DE LAS COLUMNAS
        df_usuarios = pd.DataFrame(usuarios_cargados_lista, columns=['id', 'username', 'dni', 'password', 'email'])

        # GUARDA EL DF MODIFICADO EN UN NUEVO ARCHIVO BINARIO
        with open('usuariosOrdenadosPorUsername.ispc', 'wb') as archivo:
            pickle.dump(df_usuarios, archivo)
        
        print('\nUSUARIOS ORDENADOS CON ÉXITO\n')
        input('\nPresiona una tecla para continuar...')


# FUNCION DE ORDENAMIENTO USANDO LIBRERIA DE PYTHON
def ordenar_con_sorted():
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))

        #CONVIERTE EL DATAFRAME EN UNA LISTA DE LISTAS
        usuarios_cargados_lista = df_usuarios.values.tolist()

    #EN CASO DE QUE NO ENCUENTRE COINCIDENCIA O NO EXISTA EL ARCHIVO MUESTRA MSJ DE ERROR
    except:
        print('El archivo usuarios.ispc o el usuario no existe')

    else:
        usuarios_cargados_lista = sorted(usuarios_cargados_lista, key=itemgetter(1))

        # CONVIERTE LA LISTA EN DATAFRAME PASANDO NUEVAMENTE LOS NOMBRES DE LAS COLUMNAS
        df_usuarios = pd.DataFrame(usuarios_cargados_lista, columns=['id', 'username', 'dni', 'password', 'email'])    

        # GUARDA EL DF MODIFICADO EN UN NUEVO ARCHIVO BINARIO
        with open('usuariosOrdenadosPorUsername.ispc', 'wb') as archivo:
            pickle.dump(df_usuarios, archivo)

        print('\nUSUARIOS ORDENADOS CON ÉXITO\n')
        input('\nPresiona una tecla para continuar...')

# FUNCION DE BUSQUEDA SECUENCIAL DE USUARIOS
def busqueda_secuencial(dato, posColumna):
    ''''
    Realiza una busqueda secuencial recibiendo por parametros el "dato" a comparar
    y la posición de la columna donde se va a busar dicho dato 
    '''

    try:

        #BANDERA PARA CONTROLAR SI ENCONTRO EL REGISTRO
        encontrado = False

        # ABRE EL ARCHIVO BINARIO DE USUARIOS
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
            
            # CONVIERTE EL DATAFRAME EN LISTA
            usuarios_cargados_lista = df_usuarios.values.tolist()

            for u in usuarios_cargados_lista:
                if u[posColumna] == dato:
                    # ALMACENA EL REGISTRO SI HAY COINCIDENCIA
                    usuario_cargado = u

                    print(f'''Datos del usuario
                            \n- ID: {usuario_cargado[0]}
                            \n- Nombre de usuario: {usuario_cargado[1]}
                            \n- DNI: {usuario_cargado[2]}
                            \n- Contraseña: {usuario_cargado[3]}
                            \n- Email: {usuario_cargado[4]}\n''')
                    
                    encontrado = True
                    break
                    
                    
                
            if not encontrado:
                # IMPRIME SI NO ENCUENTRA REGISTRO
                print('No se encontró usuario.')

        print("-" * 70)
        print('SE REALIZO MEDIANTE BUSQUEDA SECUENCIAL')
        print("-" * 70)
        input('Presiona una tecla para continuar...')

                                       
    #EN CASO DE QUE NO ENCUENTRE COINCIDENCIA O NO EXISTA EL ARCHIVO MUESTRA MSJ DE ERROR
    except:
        print('El archivo usuarios.ispc o el usuario no existe')

# FUNCION DE BUSQUEDA BINARIA DE USUARIOS
def busqueda_binaria(dato, posColumna):
    ''''
    Realiza una busqueda binaria recibiendo por parametros el "dato" a comparar
    y la posición de la columna donde se va a busar dicho dato 
    '''

    try:
        #BANDERA PARA CONTROLAR SI ENCONTRO EL REGISTRO
        encontrado = False

        # ABRE EL ARCHIVO BINARIO DE USUARIOS
        with open('usuariosOrdenadosPorUsername.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
            
            # CONVIERTE EL DATAFRAME EN LISTA
            usuarios_cargados_lista = df_usuarios.values.tolist()

        inicio = 0
        fin = len(usuarios_cargados_lista) - 1 

        while inicio <= fin:
            puntero = (inicio + fin) // 2

            if dato == usuarios_cargados_lista[puntero][posColumna]:
                usuario_cargado =  usuarios_cargados_lista[puntero]
                # PONE BANDERA EN VERDADERO
                encontrado = True
                break

            elif dato > usuarios_cargados_lista[puntero][posColumna]:
                inicio = puntero + 1

            else:
                fin = puntero - 1   


        
        if encontrado:
            print(f'''Datos del usuario
                    \n- ID: {usuario_cargado[0]}
                    \n- Nombre de usuario: {usuario_cargado[1]}
                    \n- DNI: {usuario_cargado[2]}
                    \n- Contraseña: {usuario_cargado[3]}
                    \n- Email: {usuario_cargado[4]}\n''')
        
        else:
                # IMPRIME SI NO ENCUENTRA REGISTRO
                print('No se encontró usuario.')
        
            
        print("-" * 70)
        print('SE REALIZO MEDIANTE BUSQUEDA BINARIA')
        print("-" * 70)
            
        input('Presiona una tecla para continuar...')
                                       
    #EN CASO DE QUE NO ENCUENTRE COINCIDENCIA O NO EXISTA EL ARCHIVO MUESTRA MSJ DE ERROR
    except:
        print('El archivo usuarios.ispc o el usuario no existe')


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

# FUNCION PARA VALIDADAR EXISTENCIA DE ARCHIVO
def verificarExistenciaArchivo(nombreArchivo):
    '''
    Verifica si exites un archivo pasando su nombre por parametro de tipo str y anteponiendo "/"
    Ejemplo "/nombreArchivo"
    retorna valor bool True/False
    '''
    
    # DEFINIMOS DIRECTORIO ACTUAL DE SCRIPT PRINCIPAL
    ubicacionMain = path.abspath(__file__)
    directorioApp, nombre = path.split(ubicacionMain)

    flag_existe = path.exists(directorioApp + nombreArchivo)

    return flag_existe

# FUNCION PARA AGREGAR USUARIO
def add_user(usuario):

    try:
        with open('/app/usuarios.ispc', 'rb') as archivo:
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

    with open('/app/usuarios.ispc', 'wb') as archivo:
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
def buscarUsuario():
    
    try:
        # ABRE EL ARCHIVO BINARIO DE USUARIOS
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
            
            while True:
                print("-" * 30 ,"BUSCAR USUARIOS","-" * 34)
                print('''Indique que parametro va a utilizar para buscar usuario
                        \n1) DNI
                        \n2) Nombre de usuario
                        \n3) Email
                        \n4) Mostrar todos
                        \n5) Volver al menú anterior\n''')
                print("-" * 80)

                opcion = input('Ingresa una opción:')
                print("-" * 80)


                if opcion == '1':
                    try:
                        dato = int(input('Ingresa el DNI:'))
                    except:
                        print('Dato incorrecto, vuelve a intentarlo')
                        input('Presiona una tecla para continuar...')
                        break
                    else:
                        
                        busqueda_binaria(dato, 2) # LE PASA COMO ARGUMENTO EL DATO CARGADO Y EL 2 QUE ES EL INDICE DE LA COLUMNA DNI
                        break

                elif opcion == '2':
                    dato = input('Ingresa el nombre de usuario:')

                    if verificarExistenciaArchivo('/usuariosOrdenadosPorUsername.ispc'):
                        busqueda_binaria(dato, 1)                    
                    else:
                        busqueda_secuencial(dato, 1)
                    break

                elif opcion == '3':
                    dato = validar_email('Ingresa el email:')
                    usuario_cargado = df_usuarios[df_usuarios['email'] == dato]

                    
                    print(f'''Datos del usuario
                                \n- ID: {usuario_cargado.to_numpy[0][0]}
                                \n- Nombre de usuario: {usuario_cargado.to_numpy()[0][1]}
                                \n- DNI: {usuario_cargado.to_numpy()[0][2]}
                                \n- Contraseña: {usuario_cargado.to_numpy()[0][3]}
                                \n- Email: {usuario_cargado.to_numpy()[0][4]}\n''')
                    
                    input('Presiona una tecla para continuar...')
                    break
                
                elif opcion == '4':
                    ("-" * 30 ,"TODOS LOS USUARIOS REGISTRADOS","-" * 34)
                    show_all_users()

                elif opcion == '5':
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

def menuOrdenarUsuario():
    '''
    Ordena el archivo usuarios.ispc con sorted o burbuja y crea un archivo usuariosOrdenadosPorUsername.ispc con el resultado
    '''

    while True:
        print("-" * 80)
        print('''ORDENAR USUARIOS POR USERNAME, ELIJA LA FORMA EN QUE DESEA ORDENARLOS\n
              1) Técnica propia (Burbuja)\n
              2) Ordenar por Python\n
              3) Volver al menú anterior\n''')
    
        print("-" * 80)
        option = (input("Ingrese una opcion: "))
        print("-" * 80)
        
        if option == "1":
            ordenar_burbuja()

        elif option == "2":
            ordenar_con_sorted()

        elif option == "3":
            break
        else:
            print("Opción inválida, intente nuevamente.")


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



def menuOrdenarBuscarUsuarios():
    '''
    Muestra el menú de ordenamiento y busqueda de usuarios y las opciones disponibles
    '''
    

    while True:
        print("-" * 30 ,"ORDENAMIENTO Y BUSQUEDA DE USUARIOS","-" * 34)

        print('''   
                    1) Ordenar por username\n
                    2) Buscar usuario\n
                    3) Volver al menú anterior\n''')
        
        print("-" * 80)

        option = (input("Ingrese una opción: "))
        
        print("-" * 80)

       
        if option == "1":
            menuOrdenarUsuario()
        
        elif option == "2":
            buscarUsuario()
        
        elif option == "3":
            break
        else:
            print("Opción inválida, intente nuevamente.")