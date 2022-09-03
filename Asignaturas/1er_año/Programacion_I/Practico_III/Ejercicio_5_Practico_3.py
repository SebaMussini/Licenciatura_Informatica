'''Escriba un programa en Python que acepte un número positivo y reste de este
número la suma de sus dígitos y así sucesivamente. Continuar esta operación
hasta que el número sea negativo y mostrar el resultado.
'''

def digito (numero):

    suma = 0

    resultado = 0

    # Para poder descomponer el número total en cada uno de sus dígitos,
    # debo convertirlo a string y luego append a una lista, para poder
    # iterar sobre sus elementos de forma individual.

    numero = str(numero)

    # Verifico que efectivamente "numero" sea del tipo string.
    print(type(numero))

    # Es bien pero bien importante pensar en las variables que estará
    # afectando al bucle while! Observar que itera el while si "resultado" es
    # mayor o igual que cero, por lo que debo definirlo antes del bucle, al
    # igual que la variable "suma", para acumular los valores.

    while int(resultado) >= 0:

        # Creo una lista vacía
        lista = []

        resultado = numero

        #print(type(numero))


        # Ahora adjunto a la lista cada uno de los dígitos que componen
        # el número.
        for i in numero:
            lista.append(int(i))

        #print(lista)


        # Teniendo ya mi lista conformada, itero sobre sus elementos para
        # asi obtener la suma de los dígitos del número ingresado.
        for i in lista:
            suma = suma + i

        #print(suma)

        # Calculo ahora el resultado como el número ingresado menos la suma
        # de sus dígitos. Ese resultado, será lo que evaluará el while hasta
        # que resultado sea menor que cero.
        resultado = int(numero) - suma

    print(resultado)


a = digito(25000)
