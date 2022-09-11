'''
DICCIONARIOS

dict1a = {‘A’: 1, ‘B’: 2}, dict1b = {‘C’: 3, ‘D’: 4},
dict2 = {‘D’: 1, ‘B’: 5, ‘F’: 3, ‘A’: 7, ‘C’: 2}
dict3 = {‘s1’: {‘n1’:‘A’, ‘n2’:‘B’}, ‘s2’: {‘n1’:‘A’, ‘n2’:‘B’},
‘s3’: {‘n1’:‘C’, ‘n2’:‘D’}, ‘s4’: {‘n1’:‘E’, ‘n2’:‘F’}}


'''

'''
15. Escriba un programa Python para concatenar diccionarios para crear uno nuevo.
INPUT: concatenar_diccionarios(dict1a, dict1b)
OUTPUT: {‘A’: 1, ‘B’: 2, ‘C’: 3, ‘D’: 4}
Debe retornar {} si ambos diccionarios son vacíos, o
diccionario con contenido si el otro diccionario es vacío.
'''

''' Para crear un tercer diccionario a partir de los elementos de otros dos se puede utilizar el operador  **  '''

dict1a = {"A": 1, "B": 2}
dict1b = {"C": 3, "D": 4}
dict1c = {}


def concatenar_diccionarios (dict1, dict2):

    if len(dict1) == 0 or len(dict2) == 0:
        new_dict = "{}"
    else:
        new_dict = {**dict1, **dict2}

    return(new_dict)


#prueba = print(concatenar_diccionarios (dict1a, dict1b))
#prueba = print(concatenar_diccionarios (dict1a, dict1c))

# ********************************------------------------**************************


'''
16. Escriba un script de Python para verificar si una llave (key) determinada ya existe
en un diccionario.
INPUT: existe_key(dict1a, ‘A’)
OUTPUT: True
INPUT: existe_key(dict1a, ‘D’)
OUTPUT: False
Debe retornar False si el diccionario es vacío.
'''

dict1a = {"A": 1, "B": 2}

def existe_key (dict, key):

    key = key

    existe = key in dict.keys()

    return(existe)


#prueba = print(existe_key (dict1a, "A"))
#prueba = print(existe_key (dict1a, "D"))


# ********************************------------------------**************************
'''
17. Escriba un script de Python para verificar si un valor (value) determinado ya
existe en un diccionario.
INPUT: existe_value(dict1a, 1)
OUTPUT: True
INPUT: existe_value(dict1a, 4)
OUTPUT: False
Debe retornar False si el diccionario es vacío.
'''

dict1a = {"A": 1, "B": 2}

def existe_value (dict, value):

    valor = value

    existe = valor in dict1a.values()

    return(existe)


#prueba = print(existe_value (dict1a, 1))
#prueba = print(existe_value (dict1a, 4))


# ********************************------------------------**************************
'''
18. Escriba un script de Python para imprimir un diccionario donde las llaves son
números entre a y b (incluidos) y los valores son cuadrados de las llaves.
INPUT: generar_cuadrados_diccionario(5, 10)
OUTPUT: {5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
Debe retornar {} si a > b o si a < 0 o b > 20.
'''

def generar_cuadrados_diccionario (a, b):

    dict = {}

    if (a > b) or (a < 0) or (b > 20):
        resultado = "{}"
    else:
        for i in range(a, (b+1)):
            dict[i] = (i**2)
        resultado = dict

    return(resultado)


#prueba = print(generar_cuadrados_diccionario (5, 10))

# ********************************------------------------**************************
'''
19. Escriba un programa de Python para mapear dos listas en un diccionario.
INPUT: lists_to_dict([‘A’, ‘B’, ‘C’], [1, 2, 3])
OUTPUT: {‘A’: 1, ‘B’: 2, ‘C’: 3}
Debe retornar {} si el largo de las listas es diferente o si son
vacías (no tienen ningún elemento).
'''

listaPrim = ["A", "B", "C"]
listaSec = [1, 2, 3]
listaTerc = [1, 2, 3, 4]

def lists_to_dict(lista1, lista2):

    dict = {}

    if len(lista1) == len(lista2):
        for i in range(0, len(lista1)):
            for j in range(0, len(lista2)):
                if i == j:
                    dict[lista1[i]] = lista2[j]

    return(dict)


#prueba = print(lists_to_dict (listaPrim, listaSec))
#prueba = print(lists_to_dict (listaPrim, listaTerc))

# ********************************------------------------**************************
'''
20. Escriba un programa de Python para ordenar un diccionario dado por llave.
INPUT: ordenar_por_llave(dict2)
OUTPUT: {‘A’: 7, ‘B’: 5, ‘C’: 2, ‘D’: 1, ‘F’: 3}
Debe retornar {} si el diccionario de entrada es vacío.
'''

dict2 = {"D": 1, "B": 5, "F": 3, "A": 7, "C": 2}
dict3 = {}



def ordenar_por_llave (dictio):

    dictio_sorted = {}

    if len(dictio) > 0:

        sort = sorted(dictio.items())
        #print(sorted)

        dictio_sorted = dict(sort)
        #print(dict2_sorted)

    return(dictio_sorted)

#prueba = print(ordenar_por_llave (dict2))
#prueba = print(ordenar_por_llave (dict3))

# ********************************------------------------**************************
'''
21. Escriba un programa de Python para ordenar un diccionario dado por valor.
INPUT: ordenar_por_valor(dict2)
OUTPUT: {‘D’: 1, ‘C’: 2, ‘F’: 3, ‘B’: 5, ‘A’: 7}
Debe retornar {} si el diccionario de entrada es vacío.
'''

dict2 = {"D": 1, "B": 5, "F": 3, "A": 7, "C": 2}
dict3 = {}


def ordenar_por_valor (dictio):

    dictio_sorted = {}


    sorted_values = sorted(dictio.values())


    for value in sorted_values:

        for key in dictio.keys():
            # dict2[k]  nos muestra el VALOR asociado a esa KEY, que coincide con i
            if dictio[key] == value:
                # agregamos al diccionario "dictio_sorted"  la key y su valor
                dictio_sorted[key] = value

    return(dictio_sorted)


#prueba = print(ordenar_por_valor (dict2))
#prueba = print(ordenar_por_valor (dict3))


# ********************************------------------------**************************
'''
22. Escriba un programa de Python para eliminar duplicados de un diccionario.
INPUT: eliminar_duplicados_dict(dict3)
OUTPUT: {‘s1’: {‘n1’:‘A’, ‘n2’:‘B’}, ‘s3’: {‘n1’:‘C’, ‘n2’:‘D’},
‘s4’: {‘n1’:‘E’, ‘n2’:‘F’}}
Debe retornar el diccionario original en caso de no tener
elementos duplicados, o {} si el diccionario es vacío.
'''

dict3 = {"s1": {"n1":"A", "n2":"B"}, "s2": {"n1":"A", "n2":"B"},
"s3": {"n1":"C", "n2":"D"}, "s4": {"n1":"E", "n2":"F"}}


def eliminar_duplicados_dict (dictio):

    #print(dict3.keys())
    #print(dict3.values())
    #print(dict3.items())

    if (dictio["s1"]["n1"] == dictio["s2"]["n1"]) and (dictio["s1"]["n2"] == dictio["s2"]["n2"]):
        print("Duplicados")
        dictio.pop("s2")

    return(dictio)


# prueba = print(eliminar_duplicados_dict (dict3))

# ********************************------------------------**************************
'''
23. Escriba un programa en Python para convertir una lista en un diccionario anidado
de llaves (keys).
INPUT: list_to_nested_dict([1, 2, 3, 4]})
OUTPUT: {1: {2: {3: {4: {}}}}}
Debe retornar {} si la lista de entrada es vacía.
'''

lista = [1, 2, 3, 4]

dic = {}


# ********************************------------------------**************************
'''
24. Escriba un programa Python para dividir un diccionario dado de listas en una
lista de diccionarios.
INPUT: 'Math': [88, 89, 62, 95], 'Physics': [77, 78, 84, 80]}
OUTPUT: [{'Math': 88, 'Physics': 77}, {'Math': 89, 'Physics': 78},
{'Math': 62, 'Physics': 84}, {'Math': 95, 'Physics': 80}]
Debe retornar {} si el diccionario de entrada es vacío.
'''
