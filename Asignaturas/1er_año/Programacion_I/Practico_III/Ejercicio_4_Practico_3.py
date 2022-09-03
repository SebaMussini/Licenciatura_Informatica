'''Escriba un programa en Python para probar si un carácter o letra dada
(mayúscula o minúscula) es una vocal o no.'''

def caracter (caracter):

    if caracter in ("a","A","e","E","i","I","o","O","u","U"):
        print("Es vocal")
    else:
        print("No es vocal")

    return(caracter)

prueba = caracter("O")
