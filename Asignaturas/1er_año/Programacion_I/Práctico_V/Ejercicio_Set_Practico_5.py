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
'''
SETS:
'''


'''
8. Escriba un programa en Python para verificar si un conjunto es un subconjunto
de otro conjunto.
INPUT: is_subset_conjuntos(set1a, set1b)
OUTPUT: True
INPUT: is_subset_conjuntos(set1a, set1c)
OUTPUT: False
'''

set1a = {"A", "B", "C"}
set1b = {"A"}
set1c = {"D"}


def is_subset_conjuntos (set1, set2):

    subset = False

    interseccion = set1.intersection(set2)

    if interseccion == set2:
        subset = True

    return(subset)

#prueba = print(is_subset_conjuntos (set1a, set1b))

#prueba = print(is_subset_conjuntos (set1a, set1c))

# *****************------------------------**************************

'''
9. Escriba un programa de Python para eliminar todos los elementos de un conjunto
dado.
INPUT: clear_conjunto(set1a)
OUTPUT: set()
También debe retornar set() si el conjunto de entrada es vacío.
'''

'''
La clase set ofrece cuatro métodos para eliminar elementos de un conjunto.
Son: discard(), remove(), pop() y clear().
'''


def clear_conjunto(set):

    retornar = "set()"

    nuevo_set = set.clear()

    return(retornar)


#prueba = print(clear_conjunto (set1a))


# *****************------------------------**************************

'''
10. Escriba un programa en Python para encontrar el valor máximo y mínimo en un
conjunto.
INPUT: max_conjunto(set2a)
OUTPUT: 50
INPUT: min_conjunto(set2a)
OUTPUT: 5
'''

set2a = {10, 50, 20, 5}

def max_conjunto (set):

    max = 0

    for i in set:
        if i > max:
            max = i
        else:
            continue

    return(max)



def min_conjunto (set):

    min = 10000000000

    for i in set:
        if i < min:
            min = i
        else:
            continue

    return(min)


#prueba = print(max_conjunto (set2a))

#prueba = print(min_conjunto (set2a))


# *****************------------------------**************************

'''
11. Escriba un programa en Python para verificar si dos conjuntos dados no tienen
elementos en común.
INPUT: is_disjoint_conjuntos(set1a, set1b)
OUTPUT: False
INPUT: is_disjoint_conjuntos(set1a, set1c)
OUTPUT: True
'''


set1a = {"A", "B", "C"}
set1b = {"A"}
set1c = {"D"}


def is_disjoint_conjuntos (set1, set2):

    disjunto = set1.isdisjoint(set2)

    return(disjunto)


#prueba = print(is_disjoint_conjuntos (set1a, set1b))

#prueba = print(is_disjoint_conjuntos (set1a, set1c))


# *****************------------------------**************************

'''
12. E Escriba un programa en Python para encontrar los elementos en un conjunto
dado que no están en otro conjunto.
INPUT: difference_conjuntos(set1a, set1b)
OUTPUT: {‘B’, ‘C’, ‘D’}
Debe retornar set() si todos los elementos se encuentran en ambos
conjuntos.
'''

set1a = {"A", "B", "C"}
set1b = {"A"}
set1c = {"D"}

def difference_conjuntos (set1, set2):

    elem_unicos = (set1.symmetric_difference(set2))

    return (elem_unicos)


#prueba = print(difference_conjuntos (set1a, set1b))


# *****************------------------------**************************

'''
13. Escriba un programa de Python para eliminar los elementos pares de un conjunto
y agregarlos a un segundo conjunto.
INPUT: trasladar_pares(set2a, {33, 17, 24})
OUTPUT: {10, 17, 24, 20, 50, 33}
Debe retornar set() si no existe ningún elemento par en conjunto.
'''

set2a = {10, 50, 20, 5}
set3 = {33, 17, 24}

def trasladar_pares (set1, set2):

    for i in set1:
        if i % 2 == 0:
            print(i)
            set2.add(i)

    return (set2)


#prueba = print(trasladar_pares (set2a, set3))



# *****************------------------------**************************
'''
14. Escriba un programa de Python para verificar que todos los elementos de una
lista se encuentran en un conjunto.
INPUT: todos_en_conjunto(set2a, [10, 50])
OUTPUT: True
INPUT: todos_en_conjunto(set2a, [13, 50])
OUTPUT: False
Debe retornar False si el conjunto o la lista son vacíos.
'''


set2a = {10, 50, 20, 5}

lista = [10, 50]

lista2 = [13, 50]


def todos_en_conjunto (set, lista):

    todos = False

    if len(set2a.intersection(lista)) == len(lista):
        todos = True

    return (todos)


#prueba = print(todos_en_conjunto (set2a, lista))

#prueba = print(todos_en_conjunto (set2a, lista2))
