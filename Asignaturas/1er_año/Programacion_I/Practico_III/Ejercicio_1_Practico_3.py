''' Escriba un programa en Python para encontrar la mediana entre tres números
dados. '''

# Crearemos una lista para los tres numeros

lista = [6,3,8,7,9,10]

# lista2 = [6,3,8,7,9]

# Para calcular la mediana, el primer paso es tener los datos ordenados
# de menor a mayor. Utilizamos el método "sort" para ordenar la lista

'''La forma más sencilla de ordenar una lista en Python es utilizar el método
 sort() de la clase list.
Este método modifica la propia lista, ordenando los elementos de manera
ascendente (el método siempre devuelve None) '''


def mediana (lista_numeros):

    # ordenada1 = lista.sort()

    # print(ordenada1)


# Por otro lado, Python define la función incorporada sorted() que se
# puede utilizar para ordenar cualquier iterable, no solo listas. Esta función
# es muy parecida al método sort() pero, a diferencia de este, sí que devuelve
# una nueva lista. '''

    ordenada2 = sorted(lista)

    print(ordenada2)


    cantidad = len(ordenada2)

    if cantidad % 2 != 0:
        posicion = int((cantidad+1)/2)
        #print(posicion)
        mediana = ordenada2[posicion-1]
        print(mediana)

    else:
        posicion1 = int(cantidad/2)
        #print(posicion1)
        posicion1 = ordenada2[posicion1-1]
        #print(posicion1)


        posicion2 = int((cantidad/2)+1)
        #print(posicion2)
        posicion2 = ordenada2[posicion2-1]
        #print(posicion2)

        mediana = (posicion1 + posicion2)/2
        print(mediana)

        #posicion_mediana = int( (ordenada2[posicion1]+ordenada2[posicion2] / 2) )
        #print(posicion_mediana)
        #mediana = ordenada2[posicion_mediana-1]
        #print(mediana)


        return(mediana)

calcular = mediana(lista)
