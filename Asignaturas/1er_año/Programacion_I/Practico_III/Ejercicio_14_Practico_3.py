'''
Escriba un programa para extraer cada dígito de un número entero en el orden
inverso. Por ejemplo, reverse_number(1267) debe retornar 7621.
'''

def num_invertido (numero):

    print("El número original es: ", numero)

    # Declaro al número como string para poder iterar sobre cada uno de sus
    # dígitos

    numero = str(numero)

    # Creo una lista vacía y una variable llamada "num" a la que le asigno un
    # caracter string cero  "0", para utilizarlo más adelante.

    list = []

    num = "0"


    # Completo la lista con cada uno de los dígitos que componen el número.
    for i in numero:
        list.append(i)

    #print(list)

    # Creo una lista invertida como resultado de la inversión de la lista
    # original.   Con   [::-1]  le estoy diciendo "slice todo desde el final hacia
    # el principio"
    list_inv = list[::-1]

    #print(list_inv)

    # Ahora que tengo la lista invertida, debo tomar cada uno de sus elementos
    # y volverlos a juntar en una variable única, que será del tipo string en
    # esta etapa.
    for i in list_inv:
        #print(i)
        # A través de la variable "num", voy acumulando/concatenando cada elemento
        # "i", que en este caso son strings (es decir, que por ej al comienzo i = 9
        # num = 0 + 9 -->  num = 09    en la proxima vuelta,  i = 8    por lo que
        # num = 9 + 8  --> num = 098   porque es string y no int
        num = num + i
    #print(type(num))
    #print(num)

    # Para terminar, debo de eliminar el primer dígito de la string que es
    # un cero, dado que al comienzo definí  num = "0" para poder acumular # -*- coding: utf-8 -*-
    # esa variable. Por tanto, tomo una parte de num, que sea desde la posición
    # 1 hasta el final, así ya no veo el cero.
    num_final = num[1:]

    # Ahora paso el número a tipo int. Recordemos que era string, hasta ahora.
    num_final = int(num_final)
    #print(type(num_final))

    print("El número invertido es: ", num_final)

# ****------------------------***********-----------------------************

numero = 123456789

inverido = num_invertido(numero)
