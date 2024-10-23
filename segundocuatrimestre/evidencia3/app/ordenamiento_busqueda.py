from operator import itemgetter
import pickle
import pandas as pd



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

                if usuarios_cargados_lista[j][0] > usuarios_cargados_lista[j+1][0]:
                    usuarios_cargados_lista[j], usuarios_cargados_lista[j+1] = usuarios_cargados_lista[j+1], usuarios_cargados_lista[j]


        # CONVIERTE LA LISTA EN DATAFRAME PASANDO NUEVAMENTE LOS NOMBRES DE LAS COLUMNAS
        df_usuarios = pd.DataFrame(usuarios_cargados_lista, columns=['username', 'password', 'email'])

        # GUARDA EL DF MODIFICADO EN EL ARCHIVO BINARIO REEMPLAZANDO EL CONTENIDO ANTERIOR 
        with open('usuarios.ispc', 'wb') as archivo:
            pickle.dump(df_usuarios, archivo)
        
        print('\nASÍ QUEDARON LOS USUARIOS ORDENADOS POR USERNAME\n\n', df_usuarios)
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
        usuarios_cargados_lista = sorted(usuarios_cargados_lista, key=itemgetter(0))

        # CONVIERTE LA LISTA EN DATAFRAME PASANDO NUEVAMENTE LOS NOMBRES DE LAS COLUMNAS
        df_usuarios = pd.DataFrame(usuarios_cargados_lista, columns=['username', 'password', 'email'])    

        # GUARDA EL DF MODIFICADO EN EL ARCHIVO BINARIO REEMPLAZANDO EL CONTENIDO ANTERIOR 
        with open('usuarios.ispc', 'wb') as archivo:
            pickle.dump(df_usuarios, archivo)

        print('\nASÍ QUEDARON LOS USUARIOS ORDENADOS POR USERNAME\n\n', df_usuarios)
        input('\nPresiona una tecla para continuar...')




def ordenar():
    
    while True:
        print("-" * 70)
        print('''ORDENAR USUARIOS POR USERNAME, ELIJA LA FORMA EN QUE DESEA ORDENARLOS\n
              1) Técnica propia (Burbuja)\n
              2) Ordenar por Python\n
              3) Volver\n''')
    
        print('En la segunda opción usamos la función "sorted()" en lugar del metodo .sort, \nestamos trabajando con lista de listas y no encontramos la manera de ordenarlo con sort')
        print("-" * 70)
        option = (input("Ingrese una opcion: "))
        print("-" * 70)
        
        if option == "1":
            ordenar_burbuja()
            flag = True

        elif option == "2":
            ordenar_con_sorted()
            flag = True

        elif option == "3":
            break
        else:
            print("Opción inválida, intente nuevamente.")

        return flag


def busqueda_secuencial(valor):
    try:

        #BANDERA PARA CONTROLAR SI ENCONTRO EL REGISTRO
        encontrado = False

        # ABRE EL ARCHIVO BINARIO DE USUARIOS
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
            
            # CONVIERTE EL DATAFRAME EN LISTA
            usuarios_cargados_lista = df_usuarios.values.tolist()

            for u in usuarios_cargados_lista:
                if u[0] == valor:
                    # ALMACENA EL REGISTRO SI HAY COINCIDENCIA
                    usuario_cargado = u

                    print(f'''Datos del usuario
                            \n- ID: {(df_usuarios[df_usuarios['username'] == usuario_cargado[0]].index).to_numpy()[0]}
                            \n- Nombre de usuario: {usuario_cargado[0]}
                            \n- Contraseña: {usuario_cargado[1]}
                            \n- Email: {usuario_cargado[2]}\n''')
                    
                    encontrado = True
                    
                    
                
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


def busqueda_binaria(valor):

    try:
        #BANDERA PARA CONTROLAR SI ENCONTRO EL REGISTRO
        encontrado = False

        # ABRE EL ARCHIVO BINARIO DE USUARIOS
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
            
            # CONVIERTE EL DATAFRAME EN LISTA
            usuarios_cargados_lista = df_usuarios.values.tolist()

        inicio = 0
        fin = len(usuarios_cargados_lista) - 1 

        while inicio <= fin:
            puntero = (inicio + fin) // 2

            if valor == usuarios_cargados_lista[puntero][0]:
                usuario_cargado =  usuarios_cargados_lista[puntero]
                # PONE BANDERA EN VERDADERO
                encontrado = True
                break

            elif valor > usuarios_cargados_lista[puntero][0]:
                inicio = puntero + 1

            else:
                fin = puntero - 1   


        
        if encontrado:
            print(f'''Datos del usuario
                    \n- ID: {(df_usuarios[df_usuarios['username'] == usuario_cargado[0]].index).to_numpy()[0]}
                    \n- Nombre de usuario: {usuario_cargado[0]}
                    \n- Contraseña: {usuario_cargado[1]}
                    \n- Email: {usuario_cargado[2]}\n''')
        
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





      

def busqueda_usuario(flag_ordenado):
    
    print("-" * 70)
    print('BUSCAR USUARIOS POR USERNAME')

    dato = input('\nIngresa el username del usuario: ')
    print("-" * 70)

    
    # SI LA BANDERA ES VERDADERA EJECUTA LA BUSQUEDA BINARIA
    if flag_ordenado:
        busqueda_binaria(dato)

    # SI LA BANDERA ES FALSA EJECUTA LA BUSQUEDA SECUENCIAL
    else:
        busqueda_secuencial(dato)
        