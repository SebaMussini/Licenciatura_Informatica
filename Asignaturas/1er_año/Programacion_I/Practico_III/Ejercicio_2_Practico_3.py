'''Escriba un archivo donde, dados dos números enteros, devuelva su producto
solo si el producto es igual o menor que 1000, de lo contrario, devuelve su suma'''

def calculo (a, b):

    if (a*b) <= 1000:
        producto = a*b
        print(producto)

        return(producto)

    else:
        suma = a + b
        print(suma)

        return(suma)




prueba = calculo(10,990)
