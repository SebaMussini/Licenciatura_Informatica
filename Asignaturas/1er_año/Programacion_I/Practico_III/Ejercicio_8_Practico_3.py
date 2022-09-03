'''Escriba un programa para iterar los primeros 10 números y en cada iteración,
imprima la suma del número actual y anterior. Puede servir función range().
'''


def iteracion (valor):

    suma = 0

    for i in range(1,valor):

        count = i
        print("La iteracion actual es: ", count)

        print("La suma anterior es: ", suma)
        suma = suma + i

        print("La suma actual es: ", suma)
        print("\n")

    return(suma)


a = iteracion(11)
