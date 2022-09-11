'''
Suponga una matriz entera de 2 por 5 de nombre t.
a. Escriba una declaración para t.
b. Cuántas filas tiene t?
c. Cuántas columnas tiene t?
d. Cuántos elementos tiene t?
e. Exprese con la sintaxis correcta todos los elementos de la segunda fila de t.
f. Que pasa si ponemos la siguiente instrucción t[2][5] = 0?
'''

# a. Escriba una declaración para t.

# t  es una matriz de dimensiones 2x5:  2 filas y 5 columnas (es decir,
# que la matriz será:
'''
num1  num2  num3  num4  num5
num6  num7  num8  num9  num10
'''

t = [["n"]*5]*2

print(t)

# b. Cuántas filas tiene t?
# Tiene 2 filas

# c. Cuántas columnas tiene t?
# Tiene 5 columnas

# d. Cuántos elementos tiene t?
# Tiene 10 elementos (2x5)

# e. Exprese con la sintaxis correcta todos los elementos de la segunda fila de t.

#print(t[1][:])

# f. Que pasa si ponemos la siguiente instrucción t[2][5] = 0?

# Nos dirá que no es posible hacerlo, pues estaremos fuera de las dimensiones
# de la matriz, que tiene dos filas  [0]  y  [1] y cinco columnas [0] [1] [2] [3] [4]
#  [2][5] hace referencia a la columna 5 de la fila 3, las cuales no existen.
# Si escribieramos t[1][4] = 1, entonces añadiría un "1" a TODAS las columnas
# 5 y no solo a la correspondiente a la fila 2 que es [1]

t[1][4] = 1

print(t)

t[0][4] = 2

print(t)
