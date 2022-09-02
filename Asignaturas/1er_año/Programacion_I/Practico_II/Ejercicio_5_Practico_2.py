# Crearemos un método/función que calcule el factorial de un número

def factorial (numero):

    if (numero == 0):
        resultado = 0
        print("El resultado es: ", resultado)


    # Ahora viene el caso donde sí tendremos resultados:
    elif (numero > 0):

        # Genero un valor de comienzo para la variable "factorial"
        fac = 1

        while (numero > 0):

            # fac guardará el resultado de fac por el número.
            # Ejemplo: el primer caso será fac = 1 * número, por lo cual
            # fac pasará a tener el valor de número.
            # enseguida, número pasa a tener el valor de  "número - 1"  y vuelve
            # a ser evaluado por fac, que ahora será
            # fac = (fac con el valor de numero) * (numero -1)
            fac = fac * numero

            numero = (numero - 1)

        print("El resultado es: ", fac)

        return fac

    else:

        print("El Factorial solo existe para números enteros no-negativos")


# Probemos si nuestra función calcula correctamente el factorial de 5  (5!)

numero = factorial(5)
