'''
Escriba un programa en Python para encontrar divisores comunes entre dos
números en un par dado.
'''


def divisor (numero1, numero2):

    count = 0

    divisores = [1,2,3,4,5,6,7,8,9]

    for i in divisores:
        i = int(i)
        if ((numero1 % i) == 0) and ((numero2 % i) == 0):
            #print(i)
            count = count + 1
        else:
            continue

    print("La cantidad de divisores en comun son ", count)

    return(count)

# *****--------------***********-------------------------****************

a = 575765
b= 2057330

prueba = divisor(a,b)
