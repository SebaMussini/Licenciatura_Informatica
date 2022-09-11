'''
3. Tenemos que realizar un conjunto de operaciones de utilidad para trabajar con listas de
enteros. Las operaciones son:

a. def desplegar(vecEnteros)
i. Despliega en salida estándar el contenido de la lista

b. def maximo(vecEnteros)
i. Retorna el número máximo que está contenido en la lista.

c. def suma(vecEnteros)
i. Retorna el valor de sumar todos los números enteros contenido en la lista.

d. def suma(vecEnteros, a, b);
i. Retorna la suma de todos los enteros que están desde el índice a hasta el
índice b.

e. def veces(vecEnteros, n)
i. Retorna la cantidad de ocurrencias del número n dentro de la lista.

f. def lugares(vecEnteros, n)
i. Retorna una lista conteniendo las posiciones dentro de la lisa vecEnteros
que se encuentra el número “n”. La lista resultante no tiene que tener
espacios vacíos.

g. def es_ordenado(vecEnteros, n)
i. Retorna true si los primeros n enteros de la lista vecEnteros se encuentran
ordenados de forma creciente (de menor a mayor) y false en caso contrario

h. def tiene_duplicados(vecEnteros, n)
i. Retorna true si los primeros n enteros de la lista vecEnteros tiene al menos
un valor duplicado y false en caso contrario.

i. def multiplicar_pares(vecEnteros, n)
i. Retorna el valor resultante de multiplicar todos los elementos pares de las
primeras n posiciones de la lista vecEnteros.

j. def reemplazar_pos(vecEnteros, pos_obj, nro_new)
i. Retorna una lista con los elementos de vecEnteros reemplazados en la
posición pos_obj por el valor nro_new.

'''

# ****************------------*****************---------------************


''' Creo una lista de ejemplo para probar todas las funciones a ser creadas '''

#list = [i for i in range(5,26)]
list = [25,45498,13,1214,9786,315,789,64,1212,4]




# ****************------------*****************---------------************

'''
a. def desplegar(vecEnteros)
i. Despliega en salida estándar el contenido de la lista
'''

def desplegar (vecEnteros):

    print(vecEnteros)

    return(vecEnteros)


#prueba = desplegar(list)

# ****************------------*****************---------------************

'''
b. def maximo(vecEnteros)
i. Retorna el número máximo que está contenido en la lista.
'''

def maximo (vecEnteros):

    maximo = 0

    for i in vecEnteros:
        if i >= maximo:
            maximo = i
        else:
            maximo = maximo

    print(maximo)

    return(maximo)


#prueba = maximo(list)


# ****************------------*****************---------------************

'''
c. def suma(vecEnteros)
i. Retorna el valor de sumar todos los números enteros contenido en la lista.
'''

def suma (vecEnteros):

    suma = 0

    for i in vecEnteros:
        suma = suma + i

    print(suma)

    return(suma)


#prueba = suma(list)


# ****************------------*****************---------------************

'''
d. def suma(vecEnteros, a, b);
i. Retorna la suma de todos los enteros que están desde el índice "a" hasta el
índice "b".
'''

def suma (vecEnteros, a, b):

    vecEnteros2 = vecEnteros[a:b]

    suma = 0

    for i in vecEnteros2:
        suma = suma + i

    print(suma)

    return(suma)


#prueba = suma(list, 2, 6)


# ****************------------*****************---------------************

'''
e. def veces(vecEnteros, n)
i. Retorna la cantidad de ocurrencias del número n dentro de la lista.
'''

list2 = [0,1,1,1,1,1,2,2,2,3,3]



def veces (vecEnteros, n):

    count = 0

    for i in vecEnteros:
        if i == n:
            count = count + 1
        else:
            continue

    print(count)

    return(count)


#prueba = veces(list2, 1)

# ****************------------*****************---------------************

'''
f. def lugares(vecEnteros, n)
i. Retorna una lista conteniendo las posiciones dentro de la lisa vecEnteros
que se encuentra el número “n”. La lista resultante no tiene que tener
espacios vacíos.
'''

nueva_lista = []

# Este algoritmo NO funcionará, pues el metodo .index tomará siempre
# la primera posición que encuentre para el número "n".
'''
for i in list2:
    if i == 2:
        pos = list2.index(i)
        nueva_lista.append(pos)
'''

# Para poder hacerlo, no iteraré sobre los elementos de la lista, sino
# que iteraré sobre las POSICIONES que ocupan:

# Mi list2 tiene  11 elementos, por lo que las posiciones van del 0 al 10.
# El rango para que itere las Posiciones, tiene que ser del 0 al 10
# Por tanto, aplico la función range al largo de la lista
# Largo de la lista = 11
# range(11) va del 0 al 10, inclusive


#print(len(list2))

# si el elemento que está en la POSICION "i" == n, entonces agrega
# a "lista2" ese número "i" que resulta ser la Posición del número "n"

def lugares (vecEnteros, n):

    for i in range (len(vecEnteros)):
        if vecEnteros[i] == n:
            nueva_lista.append(i)

    print(nueva_lista)

    return(nueva_lista)


#prueba = lugares(list2, 1)

# ****************------------*****************---------------************

'''
g. def es_ordenado(vecEnteros, n)
i. Retorna true si los primeros n enteros de la lista vecEnteros se encuentran
ordenados de forma creciente (de menor a mayor) y false en caso contrario
'''


def es_ordenado (list, n):

    sub_list = []

    for i in list:
        if i < n:
            sub_list.append(i)

    print(sub_list)

    for h in range(len(sub_list)):
        if sub_list[h] < sub_list[h+1]:
            print("True")
        else:
            print("False. La lista no está ordenada")
            break

    return(sub_list)

'''   Si en lugar de  "<"   fuera   ">" , entonces  "list index out of range" '''

#prueba = es_ordenado(list, 35)



'''
for h in sub_lista:
    while h < int(len(sub_lista)):
        if sub_lista[h] < sub_lista[h+1]:
            print("True")
        else:
            print("La lista no está ordenada")
            break
'''


# ****************------------*****************---------------************

'''
h. def tiene_duplicados(vecEnteros, n)
i. Retorna true si los primeros n enteros de la lista vecEnteros tiene al menos
un valor duplicado y false en caso contrario.
'''


list3 = [1,2,3,50,55,101,101,235,289,289]

def tiene_duplicados (list3, n):

    sub_list = [i for i in list3 if i < n]

    dup = False

    print(sub_list)

    for j in sub_list:
        #list3.count(j))
        if sub_list.count(j) > 1:
            dup = True
            break

    print(dup)

    return dup


#prueba = tiene_duplicados(list3, 110)


# ****************------------*****************---------------************

''' def multiplicar_pares(vecEnteros, n)
i. Retorna el valor resultante de multiplicar todos los elementos pares de las
primeras n posiciones de la lista vecEnteros.
'''

list4 = [1,2,3,4,5,6,7,15,20]

def multiplicar_pares (list4, n):

    valor = 1

    sub_list = []

    # O LO PUEDO HACER CON LIST COMPREHENSION:
    '''
    sub_list = [i for i in list4 if i < 18]
    '''

    for i in list4:
        if i < n:
            sub_list.append(i)

    print(sub_list)

    for j in sub_list:
        if j % 2 == 0:
            valor = j * valor

    print (valor)

    return (valor)



#prueba = multiplicar_pares (list4, 18)

# ****************------------*****************---------------************

'''
j. def reemplazar_pos(vecEnteros, pos_obj, nro_new)
i. Retorna una lista con los elementos de vecEnteros reemplazados en la
posición pos_obj por el valor nro_new.
'''

list4 = [1,2,3,4,5,6,7,15,20]

#for pos, val in enumerate(list4):
    #print(pos,val)

def reemplazar_pos (vecEnteros, pos_obj, nro_new):


    vecEnteros[pos_obj] = nro_new

    print (vecEnteros)

    return(vecEnteros)


#prueba = reemplazar_pos(list4, 2, 68)
