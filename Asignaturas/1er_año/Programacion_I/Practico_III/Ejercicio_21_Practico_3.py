'''
Escriba un programa en Python para crear todas las permutaciones posibles a
partir de una colección determinada de números distintos.
'''



numeros = ("1","2","3","4")


for n in numeros:
    for j in numeros:
        for m in numeros:
            for k in numeros:
                combinacion = n+j+m+k
                print(combinacion)
