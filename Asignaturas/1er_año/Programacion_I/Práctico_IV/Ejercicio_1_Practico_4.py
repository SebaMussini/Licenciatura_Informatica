'''
1. Escriba sentencias en Python que permitan representar lo siguiente:
a. Muestre el valor del séptimo elemento de una lista de caracteres.
b. Introduzca un valor en el elemento 4 de una lista de punto flotante.
c. Inicialice en 1 cada uno de los 1000 elementos de una lista de enteros.
d. Copie todos los valores de la lista “a”, partiendo de la tercera posición de la lista
“b”. Suponga la lista a de tamaño 10 y b tamaño 20;
e. Declare e inicialice la siguiente matriz:
1 2 3
4 5 6
7 8 9

'''

''' Operaciones comunes para Vectores/Arrays:
list.append(object)      agrega al vector el objeto señalado
list.pop(index = 5)      elimina el elemento que ocupa la posición 5, por ejemplo
list.insert(index = 5, object)   agrega el objeto que quiero en la posición 5
list.remove(value)      elimina de la lista el primer elemento que tenga el
valor señalado (ejemplo: si tengo [200, 200, 100]) y escribo list.remove(200)
eliminará el primer 200 y NO ambos
'''

list = [0,1,6,87,4,3,66,45,78,61,44]

# Parte a)

mostrar = list[6]

#print(mostrar)

# Parte b)

list.insert(3, 2.5656)

#print(list)

# Parte c)  Inicialice en 1 cada uno de los 1000 elementos de una lista de enteros

lista_unos = [1]*1000

#print(lista_unos)

# Parte d) Copie todos los valores de la lista “a”, partiendo de la tercera
# posición de la lista “b”. Suponga la lista a de tamaño 10 y b tamaño 20;


lista_a = [2]*10
#print(lista_a)

lista_b = [8]*20
#print(lista_b)

#lista_b.insert(3,lista_a[s :])
#print(lista_b)

lista_b.insert(3, [i for i in lista_a])
#print(lista_b)

#lista_b.append(lista_a)
#print(lista_b)


'''Parte e) Declare e inicialice la siguiente matriz:
1 2 3
4 5 6
7 8 9
'''

#matriz1 = [[]*3]*3
#print(matriz1)

# ¿Por qué los inserta en todas las columnas 1 si la fila es la 0 ?
#matriz1[0][1] = 1
#print(matriz1)
'''
matriz1[0].insert(0, 1)
matriz1[0].insert(0, 2)
matriz1[0].insert(0, 3)

matriz1[1].append(4)
matriz1[1].append(5)
matriz1[1].append(6)

matriz1[2].append(7)
matriz1[2].append(8)
matriz1[2].append(9)

print(matriz1)

'''
matriz2 = [[1,2,3],[4,5,6],[7,8,9]]

print(matriz2)
