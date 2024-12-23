import pickle
import pandas as pd
import re
from operator import itemgetter
import os
from datetime import datetime
from gestionAcceso import menuDatosAccesos


# DEFINIMOS DIRECTORIO ACTUAL DE SCRIPT PRINCIPAL
ubicacionMain = os.path.abspath(__file__)
directorioApp, nombre = os.path.split(ubicacionMain)

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
        with open(directorioApp + '/usuarios.ispc', 'rb') as archivo:
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
        with open(directorioApp + '/usuariosOrdenadosPorUsername.ispc', 'wb') as archivo:
            pickle.dump(df_usuarios, archivo)
        
        print('\nUSUARIOS ORDENADOS CON ÉXITO\n')
        input('\nPresiona ENTER para continuar...')

# FUNCION DE ORDENAMIENTO USANDO LIBRERIA DE PYTHON
def ordenar_con_sorted():
    try:
        with open(directorioApp + '/usuarios.ispc', 'rb') as archivo:
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
        with open(directorioApp + '/usuariosOrdenadosPorUsername.ispc', 'wb') as archivo:
            pickle.dump(df_usuarios, archivo)

        print('\nUSUARIOS ORDENADOS CON ÉXITO\n')
        input('\nPresiona ENTER para continuar...')

# FUNCION DE BUSQUEDA SECUENCIAL DE USUARIOS
def busqueda_secuencial(dato, posColumna):
    ''''
    Realiza una busqueda secuencial recibiendo por parametros el "dato" a comparar
    y la posición de la columna donde se va a busar dicho dato 
    '''

    try:

        #BANDERA PARA CONTROLAR SI ENCONTRO EL REGISTRO
        encontrado = False

        contadorIntentos = 0

        # ABRE EL ARCHIVO BINARIO DE USUARIOS
        with open(directorioApp + '/usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))

            print(f'Buscando el {df_usuarios.columns[posColumna]} “{dato}” ')
            
            # CONVIERTE EL DATAFRAME EN LISTA
            usuarios_cargados_lista = df_usuarios.values.tolist()

            for u in usuarios_cargados_lista:
                contadorIntentos += 1

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
                    
                else:
                    print(f'Intento {contadorIntentos}: {dato} es distinto a {u[posColumna]}')
                
                
            if not encontrado:
                # IMPRIME SI NO ENCUENTRA REGISTRO
                print('No se encontró usuario.')

        print("-" * 70)
        print('SE REALIZO MEDIANTE BUSQUEDA SECUENCIAL')
        print("-" * 70)
        input('\nPresiona ENTER para continuar...')

                                       
    #EN CASO DE QUE NO ENCUENTRE COINCIDENCIA O NO EXISTA EL ARCHIVO MUESTRA MSJ DE ERROR
    except:
        print('El archivo usuarios.ispc o el usuario no existe')

# FUNCION DE BUSQUEDA BINARIA DE USUARIOS
def busqueda_binaria(dato, posColumna, nombreArchivo):
    ''''
    Realiza una busqueda binaria recibiendo por parametros el "dato" a comparar, 
    la posición de la columna donde se va a busar dicho dato y el nombre del archivo binario anteponiendo "/"
    Ejemplo "/nombreArchivo"
    '''

    try:
        #BANDERA PARA CONTROLAR SI ENCONTRO EL REGISTRO
        encontrado = False
        registroLista = []

        # ABRE EL ARCHIVO BINARIO DE USUARIOS
        with open(directorioApp + nombreArchivo, 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
            
            # CONVIERTE EL DATAFRAME EN LISTA
            usuarios_cargados_lista = df_usuarios.values.tolist()

        inicio = 0
        fin = len(usuarios_cargados_lista) - 1 
        contadoIntentos = 0

        registroLista.append(f'Búsqueda Binaria por {df_usuarios.columns[posColumna]}:')
        
        registroLista.append(f'Buscando el {df_usuarios.columns[posColumna]} {dato} en el archivo {nombreArchivo} que contiene {len(usuarios_cargados_lista)} usuarios.')

        while inicio <= fin:
            contadoIntentos += 1
            puntero = (inicio + fin) // 2

            if dato < usuarios_cargados_lista[0][posColumna]:
                registroLista.append(f'El {df_usuarios.columns[posColumna]} a buscar es más CHICO que el más chico de los registrados')
                break

            elif dato > usuarios_cargados_lista[-1][posColumna]:
                registroLista.append(f'El {df_usuarios.columns[posColumna]} a buscar es más GRANDE que el más grande de los registrados')
                break

            registroLista.append(f'Intento {contadoIntentos}: {df_usuarios.columns[posColumna]} del usuario de la posición {puntero} es {usuarios_cargados_lista[puntero][posColumna]}')

            if dato == usuarios_cargados_lista[puntero][posColumna]:
                registroLista.append(f'por lo tanto se encontró el usuario en {contadoIntentos} intentos.')
                registroLista.append('-'*80)

                usuario_cargado =  usuarios_cargados_lista[puntero]
                # PONE BANDERA EN VERDADERO
                encontrado = True
                break

            elif dato > usuarios_cargados_lista[puntero][posColumna]:

                inicio = puntero + 1
                registroLista.append(f'''por lo tanto se buscará en la subsecuencia de la derecha ({df_usuarios.columns[posColumna]} más grandes) (posición {inicio} a {fin}).''')


            else:
                fin = puntero - 1
                
                # USAR ESTA INFORMACION PARA REGISTRAR EN ARCHIVO DE REGISTROS ***************************************************************************************************
                registroLista.append(f'por lo tanto se buscará en la subsecuencia de la IZQUIERDA ({df_usuarios.columns[posColumna]} más chicos) (posición {inicio} a {fin}).')


        
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
                registroLista.append('No se encontró usuario.')
                registroLista.append('-'*80)

        crearArchivoRegistroBusquedasBin(df_usuarios.columns[posColumna], registroLista)
            
        print("-" * 70)
        print('SE REALIZO MEDIANTE BUSQUEDA BINARIA')
        print("-" * 70)
            
        input('\nPresiona ENTER para continuar...')
                                       
    #EN CASO DE QUE NO ENCUENTRE COINCIDENCIA O NO EXISTA EL ARCHIVO MUESTRA MSJ DE ERROR
    except:
        print('El archivo usuarios.ispc o el usuario no existe')

# FUNCION PARA CREAR LOS REGISTROS DE BUSQUEDAS BINARIAS
def crearArchivoRegistroBusquedasBin(columna, registro):
    '''
    Crea los archivos de registros de  busquedas binarias: "/busquedasYordenamientos/buscandoUsuarioPorDNI-fecha.ispc" y 
    "/busquedasYordenamientos/buscandoUsuarioPorUsername-fecha.txt"recibiendo por parametro el nombre de la columna "dni" o "username"
    '''

    os.makedirs(directorioApp + '/busquedasYordenamientos', exist_ok=True)  # Crear carpeta si no existe


    columnas = ('id', 'username', 'dni', 'password', 'email')
    fecha = datetime.now().strftime('%Y-%m-%d %Hh %Mm %Ss')

    try:
        if columna == 'dni':
            with open(directorioApp + f'/busquedasYordenamientos/buscandoUsuarioPorDNI-{fecha}.txt', 'a', encoding='utf-8') as archivo:
                
                for r in registro:
                    archivo.write(r + '\n')

        
        elif columna == 'username':
            with open(directorioApp + f'/busquedasYordenamientos/buscandoUsuarioPorUsername-{fecha}.txt', 'a', encoding='utf-8') as archivo:
                
                for r in registro:
                    archivo.write(r + '\n')

        else:
            print('El nombre de la columna ingresada es incorrecto.')
    except:
        print('ERROR "crearArchivoRegistroBusquedasBin": el directorio donde se desea crear el archivo no existe.')
        input('\nPresiona ENTER para continuar...')

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

    flag_existe = path.exists(directorioApp + nombreArchivo)

    return flag_existe

# FUNCION PARA AGREGAR USUARIO
def add_user(usuario):

    try:
        with open((directorioApp + '/usuarios.ispc'), 'rb') as archivo:
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

    with open(directorioApp + '/usuarios.ispc', 'wb') as archivo:
        pickle.dump(df_usuarios, archivo)


# FUNCION PARA MODIFICAR DATOS DE USUARIO
def modificarUsuarioConMenu():

    # ABRE EL ARCHIVO BINARIO DE USUARIOS
    try:
        usuario = input('Ingresa el username a modificar:')

        with open(directorioApp + '/usuarios.ispc', 'rb') as archivo:
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
                with open(directorioApp + '/usuarios.ispc', 'wb') as archivo:
                    pickle.dump(df_usuarios, archivo)
        
                break

            else:
                print('Opción incorrecta')     
    

# FUNCION PARA ELIMINAR USUARIO
def eliminarUsuarioConMenu():

    # ABRE EL ARCHIVO BINARIO DE USUARIOS
    try:
        with open(directorioApp + '/usuarios.ispc', 'rb') as archivo:
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
                            \n- Nombre de usuario: {usuario_cargado.to_numpy()[0][1]}
                            \n- Email: {usuario_cargado.to_numpy()[0][2]}\n''')
                    
                    df_usuarios = df_usuarios.drop(usuario_cargado.index)
                    # GUARDA EL DF MODIFICADO EN EL ARCHIVO BINARIO REEMPLAZANDO EL CONTENIDO ANTERIOR 
                    with open(directorioApp + '/usuarios.ispc', 'wb') as archivo:
                        pickle.dump(df_usuarios, archivo)
                    print('El usuario se eliminó con exito')
                    input('\nPresiona ENTER para continuar...')

                    break

                elif opcion == '2':
                    dato = validar_email('Ingresa el email:')
                    usuario_cargado = df_usuarios[df_usuarios['email'] == dato]


                    print(f'''Datos del usuario
                            \n- Nombre de usuario: {usuario_cargado.to_numpy()[0][0]}
                            \n- Email: {usuario_cargado.to_numpy()[0][2]}\n''')
                    
                    df_usuarios = df_usuarios.drop(usuario_cargado.index)
                    # GUARDA EL DF MODIFICADO EN EL ARCHIVO BINARIO REEMPLAZANDO EL CONTENIDO ANTERIOR 
                    with open(directorioApp + '/usuarios.ispc', 'wb') as archivo:
                        pickle.dump(df_usuarios, archivo)
                    print('El usuario se eliminó con exito')
                    input('\nPresiona ENTER para continuar...')

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
        with open(directorioApp + '/usuarios.ispc', 'rb') as archivo:
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
                        
                    else:
                        
                        busqueda_binaria(dato, 2, '/usuarios.ispc') # LE PASA COMO ARGUMENTO EL DATO CARGADO Y EL 2 QUE ES EL INDICE DE LA COLUMNA DNI
                        

                elif opcion == '2':
                    dato = input('Ingresa el nombre de usuario:')

                    if verificarExistenciaArchivo('/usuariosOrdenadosPorUsername.ispc'):
                        busqueda_binaria(dato, 1, '/usuariosOrdenadosPorUsername.ispc')                    
                    else:
                        busqueda_secuencial(dato, 1)

                elif opcion == '3':
                    dato = validar_email('Ingresa el email:')
                    busqueda_secuencial(dato, 4)

                
                elif opcion == '4':
                    print("-" * 30 ,"MOSTRAR TODOS LOS USUARIOS REGISTRADOS","-" * 34)

                    print("\n", "-" * 30 ,"USUARIOS REGISTRADOS EN 'usuarios.ispc'","-" * 34)
                    show_all_users('/usuarios.ispc')

                    print("\n", "-" * 30 ,"USUARIOS REGISTRADOS EN 'usuariosOrdenadosPorUsername.ispc'","-" * 34)
                    show_all_users('/usuariosOrdenadosPorUsername.ispc')

                elif opcion == '5':
                    break


                else:
                    print('Opción incorrecta')
        
    #EN CASO DE QUE NO ENCUENTRE COINCIDENCIA O NO EXISTA EL ARCHIVO MUESTRA MSJ DE ERROR
    except:
        print('El archivo usuarios.ispc o el usuario no existe')
    

# FUNCION PARA MOSTRAR TODOS LOS USUARIOS
def show_all_users(nombreArchivo):
    '''
    Muestra el contenido de los archivos binarios de registros de usuarios
    Recibe como parametro el nombre del archivo con tipo srt anteponiendo "/"
    Ejemplo "/nombreArchivo"
    '''
    try:
        with open(directorioApp + nombreArchivo, 'rb') as archivo:
            df_usuarios = pickle.load(archivo)
            print(df_usuarios)
        input('\nPresiona ENTER para continuar...')
        
    except:
        print(f'El archivo {nombreArchivo} no existe')
        input('\nPresiona ENTER para continuar...')



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


def menuUsuariosAccesos():
    '''
    Muestra el menu de opciones par manipular datos de accesos y usuarios
    '''
    
    while True:

        # IMPRIME MENÚ DE OPCIONES POR CONSOLA
        print('')
        print("-" * 25 ,"USUARIOS Y ACCESOS DE LA APP","-" * 25)
        print('''   
                    1) Acceder al CRUD de los Usuarios en POO\n
                    2) Mostrar los datos de Acceso\n
                    3) Ordenamiento y Búsqueda de Usuarios\n
                    4) Volver al Menú principal\n''')
        
        print("-" * 80)

        option = (input("Ingrese una opción: "))
        
        print("-" * 80)
        
        # OPCIÓN 1 - CRUD USUARIOS POO
        if option == "1":
            menuCrudUsuarios()
    
        # OPCIÓN 2 - DATOS DE ACCESO
        elif option == "2":
            menuDatosAccesos()
        
        # OPCIÓN 3 - ORDENAMIENTO Y BUSQUEDA DE USUSARIOS
        elif option == "3":
            menuOrdenarBuscarUsuarios()
        
        # OPCIÓN 4 - VUELVE AL MENÚ PRINCIPAL
        elif option == "4":
            break
        else:
            print("Opción inválida, intente nuevamente.")


#menuRegistrarUsuario()

#menuOrdenarBuscarUsuarios()

#buscarUsuario()