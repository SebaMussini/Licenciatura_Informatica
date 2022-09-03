'''
Escriba un programa para eliminar caracteres de una cadena desde cero hasta
n y devolver una nueva cadena. Por ejemplo, remove_chars(‘python’, 2) debe
imprimir ‘hon’
'''


def slice (palabra, start):

    palabra = str(palabra)


    # La palabra recortada con la que me quedaré será el slice de la palabra
    # original desde el caracter "start" hasta el final
    palabra_recortada = palabra[start:]

    print(palabra_recortada)

    return(palabra_recortada)


a = slice("python", 3)
