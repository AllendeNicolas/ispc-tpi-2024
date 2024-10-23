from operator import itemgetter
import pickle
import pandas as pd

def ordenar():
    print('''ORDENAR USUARIOS, ELIJA LA FORMA EN QUE DESEA ORDENARLO\n
          1) Técnica propia (Burbuja)\n
          2) Ordenar por Python\n''')
    
    print('En la segunda opción usamos la función "sorted()" en lugar del metodo .sort, \nestamos trabajando con lista de listas y no encontramos la manera de ordenarlo con sort')
    print("-" * 70)

# FUNCION DE ORDENAMIENTO CON METODO BURBUJA HECHA POR NOSOTROS
def ordenar_burbuja ():
    try:
        with open('usuarios.ispc', 'rb') as archivo:
            df_usuarios = pd.DataFrame(pickle.load(archivo))
            print('\ndf MODIFICADO\n')
            print(df_usuarios)
    

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

        df_usuarios = pd.DataFrame(usuarios_cargados_lista, columns=['username', 'password', 'email'])    
        
        print('\ndf MODIFICADO\n')
        print(df_usuarios)
    

# FUNCION DE ORDENAMIENTO USANDO LIBRERIA DE PYTHON
def ordenar_lista_de_listas(lista_de_listas):

    sorted(lista_de_listas, key=itemgetter(1))

    return lista_de_listas


ordenar_burbuja()