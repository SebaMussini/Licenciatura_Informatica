# Crearemos un método/función que nos permita comprobar si un número
# entero es par o impar

# Si el resto/módulo (cuyo símbolo operativo es   % ) de un número dividido
# entre 2  es  cero   numero % 2 = 0   , entonces será número par.
# Si  numero % 2 = 1  ,  entonces será número impar.

def par_impar (numero):

    if ((numero % 2) == 0 ):
        print("El número ", numero, " es Par")

    else:
        print("El número ", numero, " es Impar")


    return numero


# Probemos con varios números si nuestro método funciona correctamente.

numero = Par_Impar(97)
numero = Par_Impar(1002)
