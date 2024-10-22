from operator import itemgetter




# FUNCION DE ORDENAMIENTO CON METODO BURBUJA
def ordenar_burbuja (lista):
    for i in range(len(lista) - 1):

        for j in range(len(lista) - 1):

            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista



def ordenar_lista_de_listas(lista_de_listas):
    
    sorted(lista_de_listas, key=itemgetter(1))

    return lista_de_listas