''' VER!!!!!!!!!

https://www.cartagena99.com/recursos/alumnos/apuntes/introduccion%20matrices.pdf

'''


'''
Tenemos que realizar un conjunto de operaciones de utilidad para trabajar con matrices.
Las operaciones son:
'''

'''
a. def desplegar(matriz);
i. Despliega en salida estándar el contenido de la matriz.
'''

matriz = [[i for i in range(0,3)]]*3
#print("La matriz es: ", matriz)

matriz2 = [[1]*3]*3
#print("La matriz2 es: ", matriz2)

# De la fila que ocupa la primera posición, quiero ver el elemento que ocupa la 2da posición
#print(matriz[1][2])


# Matriz de 3x5     3 filas  y  5 columnas
matriz3 =  [ [0 for i in range(5)] for j in range(3) ]
#print("La matriz3 es: ", matriz3)


def crear (n, m):

    a = [0]*m

    matriz4 = [a]*n

    #print(matriz4)

#matriz4 = crear(3,3)

#  *************-----------------------**************------------------------

'''
b. def esCuadrada(matriz);
i. Retorna true si la matriz es cuadrada.
'''

def esCuadrada (matrix):

    Cuadrada = False

    cant_filas = len(matrix)
    print("La cantidad de filas es: ", cant_filas)


    for i in range(0,len(matrix)):
        cant_columnas = len(matrix[i])
        if cant_filas != cant_columnas:
            #print(Cuadrada)
            break
        else:
            Cuadrada = True

    #print(Cuadrada)

    print("La cantidad de columnas es: ", cant_columnas)

    return(Cuadrada)


#prueba = print(esCuadrada (matriz2))

#prueba2 = esCuadrada (matriz3)


#  *************-----------------------**************------------------------

'''
c. def filas(matriz);
i. Retorna la cantidad de filas de la matriz
'''

def filas (matrix):

    cantidad_filas = len(matrix)

    print("La cantidad de filas es: ", cantidad_filas)

    return(cantidad_filas)


#prueba = filas(matriz2)

#prueba = filas(matriz3)

#  *************-----------------------**************------------------------

'''
d. def columnas(matriz);
i. Retorna la cantidad de columnas de la matriz
'''

def columnas (matrix):

    cantidad_columnas = len(matrix[0])

    print("La columnas de filas es: ", cantidad_columnas)

    return(cantidad_columnas)


#prueba = columnas(matriz2)

#prueba = columnas(matriz3)


#  *************-----------------------**************------------------------

'''
e. def es_ordenado_fila(matriz, nro_fila);
i. Retorna true si la fila nro_fila se encuentra ordenada en forma creciente (de
menor a mayor) y false en caso contrario.
'''

matrizzz = [[1,3,6,1,4,9],[0,5,6,7,7,9,],[4,5,8,4]]
#print(matrizzz)


def es_ordenado_fila (matriz, nro_fila):

    ordenada = True

    valor_ant = 0

    print(matriz[0])

    for i in matriz[nro_fila]:
        print(i)

        if i >= valor_ant:
            #print(ordenada)
            valor_ant = i
        else:
            ordenada = False
            #print(ordenada)
            break

    print("¿Se encuentra la fila numero", nro_fila, "ordenada?", ordenada)

    return(ordenada)


#prueba = es_ordenado_fila(matrizzz, 0)


#  *************-----------------------**************------------------------

'''
f. def tiene_duplicado_fila(matriz, nro_fila);
i. Retorna true si la columna nro_fila tiene al menos un valor duplicado y false
en caso contrario.
'''


def tiene_duplicado_fila (matrix, nro_fila):

    #dup = True

    for nro_fila in range(0, len(matrix)):

        for j in range(0, len(matrix[nro_fila])):

            value = matrix[nro_fila][j]
            #print(value)
            cuenta = matrix[nro_fila].count(value)
            #print(matrizzz[i][j], "aparece", cuenta, "veces")

            if cuenta > 1:
                print("La fila", nro_fila, "que es", matrix[nro_fila], "tiene el valor", value, "repetido al menos una vez")
                #print("Valor duplicado = ", dup)
                print("--------")
                break

#prueba = tiene_duplicado_fila (matrizzz, 0)


#  *************-----------------------**************------------------------

'''
f. def tiene_duplicado_col(matriz, nro_col);
i. Retorna true si la columna nro_col tiene al menos un valor duplicado y false
en caso contrario.
'''

matriZ =[[1,2,6,7],[6,5,6,1],[5,7,6,9]]

'''
print(matrizzz[0][2])
print(matrizzz[1][2])
print(matrizzz[0][3])
print(matrizzz[2][3])
'''

def tiene_duplicado_col (matriz, nro_col):

    dup = False

    numero = None

    for i in range(0, (len(matriz))):
        print(matriz[i][nro_col])
        if matriz[i][nro_col] == numero:
            dup = True
            #print(dup)
            break
        numero = matriz[i][nro_col]

    return(dup)

#prueba = print(tiene_duplicado_col (matriZ, 2))


#  *************-----------------------**************------------------------

'''
g. def sumar_diagonales(matriz)
i. Retorna el valor resultado de sumar los elementos de la diagonal principal y
secundaria de la matriz.
'''

matriZZ =[[1,2,6],[6,5,6],[5,7,6]]

'''
# Diagonal principal:
print(matriZZ[0][0])
print(matriZZ[1][1])
print(matriZZ[2][2])

# Diagonal Secundaria:
print(matriZZ[0][2])
print(matriZZ[1][1])
print(matriZZ[2][0])
'''

def sumar_diagonales (matrix):

# Diagonal Principal:

    suma = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            #print(i,j)
            if i == j:
                #print(matrix[i][j])
                suma = matrix[i][j] + suma

    print("**********--------------***********")

    return(suma)


#prueba = print(sumar_diagonales(matriZZ))


'''
Para crear un objeto de tipo range, se pueden usar dos constructores :

range(fin): Crea una secuencia numérica que va desde 0 hasta fin - 1.

range(inicio, fin, [paso]): Crea una secuencia numérica que va desde inicio
hasta fin - 1. Si además se indica el parámetro paso, la secuencia genera los
números de paso en paso.

# DIAGONAL SECUNDARIA

count = 0


for fila in matriZZ:
    print(fila[len(fila)-1], -1, count)


    #print(fila[len(fila)]-1)

print("**********--------------***********")

'''

#  *************-----------------------**************------------------------

'''
def num_perdidos(matriz, vecSecuencia)
i. Retorna una lista con los elementos de la matriz que no se encuentran
(faltantes) en la lista vecSecuencia.
'''

matriZZ =[[1,2,6],[6,5,6],[5,7,6]]

vecsec = [1,0,6,5,10,11]

def num_perdidos (matriz, vecSec):

    matriz_a_lista = []

    listaf = []

    #listaf = [listaf.append(x) for x in matriZZ if not in (vecsec)]
    #print(listaf)

    for fila in range(0, len(matriz)):
        for columna in range(0, len(matriz[fila])):
            matriz_a_lista.append(matriz[fila][columna])
            #print(matriZZ[fila][columna])

    for val in matriz_a_lista:
        if val not in vecSec:
            listaf.append(val)

    #print(matriz_a_lista)

    return(listaf)


#prueba = print(num_perdidos (matriZZ, vecsec))


#  *************-----------------------**************------------------------

'''
i. def reemplazar_val(matriz, nro_obj, nro_new)
i. Retorna la matriz con sus elementos de valor nro_obj reemplazados por el
valor nro_new.
'''

matriZZ =[[1,2,6],[6,5,6],[5,7,6]]


def reemplazar_val (matriz, nro_obj, nro_new):

    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            valor = matriz[i][j]
            if valor == 6:
                matriz[i][j] = 0

    return(matriz)


#prueba = print(reemplazar_val(matriZZ, 6, 0))

#  *************-----------------------**************------------------------

'''
j. def sumar(matrizA, matrizB);
i. Retorna la matriz resultado de sumar matrizA+matrizB (elemento a
elemento). En caso que las matrices tengan distintas dimensiones se debe
retornar null.
'''

matriz1 =[[1,2,6],[6,5,6],[5,7,6]]

matriz2 =[[1,1,1],[1,1,1],[1,1,1]]

list = []

matriz3 = []


filas1 = filas(matriz1)
filas2 = filas(matriz2)

columnas1 = columnas(matriz1)
columnas2 = columnas(matriz2)

if (filas1 == filas2) and (columnas1 == columnas2):
    print("Matrices tienen mismas dimensiones")
    for i in range(0, len(matriz1)):
        for j in range(0, len(matriz1[i])):
            valor1 = matriz1[i][j]
            #print(valor1)
            for h in range(0, len(matriz2)):
                for w in range(0, len(matriz2[h])):
                    valor2 = matriz2[h][w]
                    #print(valor2)
                    valor3 = valor1 + valor2
            list.append(valor3)
            #print(valor3)
else:
    print("NULL")

print(list)

#for i in range(0, len(list)):



#  *************-----------------------**************------------------------

'''
k. def multiplicar(matrizA, matrizB);
i. Retorna la matriz resultado de multiplicar matrizA con matrizB (producto
matricial). En caso que las matrices tengan dimensiones incompatibles se
debe retornar null.
'''

#  *************-----------------------**************------------------------

'''
l. def trasponer(matriz)
i. Retorna la matriz traspuesta
'''
