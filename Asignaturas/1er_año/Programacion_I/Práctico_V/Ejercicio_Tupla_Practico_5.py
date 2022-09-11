'''Estructuras de datos de ejemplo:

tuple1 = (“Orange”, [1, 2, 3], 2022, “Septiembre”)

tuple2 = ((), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d'))

tuple3 = (('R', 'W', 'B'), ('G', 'P', 'L'), ('O', 'Y', 'L'))

set1a = {‘A’, ‘B’, ‘C’}, set1b = {‘A’}, set1c = {‘D’}

set2a = {10, 50, 20, 5}, set2b = {25, 33, 11, 3}

dict1a = {‘A’: 1, ‘B’: 2}, dict1b = {‘C’: 3, ‘D’: 4},

dict2 = {‘D’: 1, ‘B’: 5, ‘F’: 3, ‘A’: 7, ‘C’: 2}

dict3 = {‘s1’: {‘n1’:‘A’, ‘n2’:‘B’}, ‘s2’: {‘n1’:‘A’, ‘n2’:‘B’},
‘s3’: {‘n1’:‘C’, ‘n2’:‘D’}, ‘s4’: {‘n1’:‘E’, ‘n2’:‘F’}}

'''

'''TUPLAS:'''

'''
1. Escriba un programa de Python para eliminar un elemento de una tupla.
INPUT: pop_tuple(tuple1, 2022)
OUTPUT: (“Orange”, [1, 2, 3], “Septiembre”).
Debe retornar tuple1 si no existe el elemento indicado.
'''

# Las tuplas son INMUTABLES!!!!  No podemos cambiar, agregar ni eliminar
# elementos una vez la tupla ha sido creada.

tuple1 = ("Orange", [1, 2, 3], 2022, "Septiembre")

def pop_tuple (tupla, n):

    if n < len(tupla):

        # Convierto la tupla a lista
        lista = list(tupla)

        print(lista)

        # pop  elimina el elemento que ocupa el index señalado

        lista.pop(n)
        #print(list)

        # Convierto la lista a tupla
        tupla = tuple(lista)

        print(tuple)

    else:
        tupla = tuple1

    return(tupla)

#prueba = print(pop_tuple(tuple1, 3))

# *********************--------------------------*********************

'''
2. Escriba un programa de Python para separar una tupla dada una posición.
INPUT: split_tuple(tuple1, 2)
OUTPUT: [(“Orange”, [1, 2, 3]), (2002, “Septiembre”)].
Debe retornar tuple1 si no existe la posición indicada.
'''

tuple1 = ("Orange", [1, 2, 3], 2022, "Septiembre")

def split_tuple (tupla, n):

    if n < len(tupla):

        lista1 = list(tupla[0:n])
        #print(lista1)
        tuplaA = tuple(lista1)
        #print(tuplaA)

        lista2 = list(tupla[n:])
        #print(lista2)
        tuplaB = tuple(lista2)
        #print(tuplaB)

        tuplaFinal = [tuplaA, tuplaB]
        #print(tuplaFinal)
        tupla = tuplaFinal

    return (tupla)

#prueba = print(split_tuple (tuple1, 2))


# *********************--------------------------*********************

'''
3. Escriba un programa de Python para encontrar el índice de un elemento de una
tupla (similar a la función index).
INPUT: index_tuple(tuple1, 2022)
OUTPUT: 2
Debe retornar -1 si no existe el elemento indicado.
'''

# Al igual que las listas, las tuplas cuentan con los métodos
#   index     y     count

tuple1 = ("Orange", [1, 2, 3], 2022, "Septiembre")

def index_tuple (tupla, elemento):

    if elemento in tupla:
        elemento = (tupla.index(elemento))
    else:
        elemento = -1

    return(elemento)

#prueba = print(index_tuple (tuple1, 2022))


# *********************--------------------------*********************

'''
4. Escriba un programa en Python para invertir una tupla (similar a función reverse).
INPUT: reverse_tuple(tuple1)
OUTPUT: (“Septiembre”, 2022, [1, 2, 3], “Orange”)
Debe retornar tuple1 si no es posible realizar la inversión.
'''

tuple1 = ("Orange", [1, 2, 3], 2022, "Septiembre")

def reverse_tuple (tupla):

    lista = list(tupla)
    lista_reversed = lista[::-1]
    #print(lista_reversed)
    tupla_reversed = tuple(lista_reversed)

    return(tupla_reversed)

#prueba = print(reverse_tuple (tuple1))



# *********************--------------------------*********************

'''
5. Escriba un programa en Python para eliminar tuplas vacías de una lista de tuplas.
INPUT: remove_spaces_from_tuple(tuple2)
OUTPUT: (('',), ('a', 'b'), ('a', 'b', 'c'), 'd')
Debe retornar tuple2 si no existe ninguna tupla vacía.
'''

tuple2 = ((), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d'))

def remove_spaces_from_tuple (tupla):

    # Creo dos listas auxiliares que voy a necesitar
    nueva_lista = []

    nueva_lista2 = []

    # Convierto el tuple principal a lista
    lista = list(tupla)
    #print(lista)

    # Convierto cada uno de los tuples dentro del tulple (ahora lista) a listas
    # y agrego aquellas NO vacias de forma individual a una de las listas auxiliares
    for tuplas in lista:
        sublista = list(tuplas)
        if sublista != []:
            nueva_lista.append(sublista)

    # Ahora tengo una lista de listas. Yo quiero una tupla de tuplas.
    # Por tanto, convertiré cada una de los elementos de la lista a tuplas.
    for elemento in nueva_lista:
        elemento = tuple(elemento)
        nueva_lista2.append(elemento)

    # Finalmente, tendré una lista de tuplas, la cual convertiré (la lista) a tupla.
    tuple_sin_espacios = tuple(nueva_lista2)

    return(tuple_sin_espacios)


#prueba = print(remove_spaces_from_tuple (tuple2))


# *********************--------------------------*********************

'''
6. Escriba un programa de Python que convierta un String dado en una tupla y
elimine los espacios en blanco.
INPUT: str_to_tuple(str1) con str1 = “Universidad Montevideo”
OUTPUT: (‘U’, ‘n’, ‘i’, ‘v’, ‘e’, ‘r’, ‘s’, ‘i’, ‘d’, ‘a’, ‘d’,
‘M’, ‘o’, ‘n’, ‘t’, ‘e’, ‘v’, ‘i’, ‘d’, ‘e’, ‘o’)
Debe retornar tupla vacía si el String indicado es vacío.
'''

str1 = "Universidad Montevideo"

def str_to_tuple (str):

# En este caso el método  "split" no funcionará, porque yo no quiero separar
# por un elemento, sino que quiero cada una de las letras por separado

    lista = []

    for letra in str:
        if letra != " ":
            lista.append(letra)

    tupla_str = tuple(lista)

    return(tupla_str)


#prueba = print(str_to_tuple (str1))

# *********************--------------------------*********************

'''

7. Escriba un programa de Python para verificar si un elemento específico se
presenta en una tupla de tuplas.
INPUT: is_element_in_tuple(tuple3, ‘G’)
OUTPUT: True
INPUT: is_element_in_tuple(tuple3, ‘F’)
OUTPUT: False
'''

tuple3 = (('R', 'W', 'B'), ('G', 'P', 'L'), ('O', 'Y', 'L'))

def is_element_in_tuple (tupla, letra):

    is_element = False

    for tup in tupla:
        #print(tupla)
        for tuplas in tup:
            if letra in tuplas:
                is_element = True


    return(is_element)


#prueba = print(is_element_in_tuple (tuple3, "G"))

#prueba = print(is_element_in_tuple (tuple3, "F"))
