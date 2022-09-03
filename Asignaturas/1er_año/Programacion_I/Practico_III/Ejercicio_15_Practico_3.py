'''
Escriba un programa en Python para encontrar si el número de divisores de un
número entero es par o impar.
'''

def divisor (numero):

    count = 0

    divisores = [1,2,3,4,5,6,7,8,9]

    for i in divisores:
        i = int(i)
        if (numero % i) == 0:
            #print(i)
            count = count + 1
        else:
            continue
    #print(count)

    if count % 2 == 0:
        print("El número de divisores de ", numero, "es par y son: ", count)
    else:
        print("El número de divisores de ", numero, "es impar y son: ", count)

    return(count)

# ***-----------------**********----------------------**********------------

numero = 259

elegido = divisor(numero)
