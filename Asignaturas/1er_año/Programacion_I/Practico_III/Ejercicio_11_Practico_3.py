'''
Escriba un programa para encontrar cuántas veces aparece un substring dado
en el String de referencia. Por ejemplo, how_many(‘Montevideo’, ‘Universidad de
Montevideo ubicada en Montevideo’) devuelve 2 (dado que hay 2 repeticiones
de ‘Montevideo’ en String de referencia). Puede servir método count() y split().
'''

def cuantas (frase, subfrase):

    frase = str(frase)
    subfrase = str(subfrase)

    count = 0

    list = []

    # Cuando aplico el método  "split", automáticamente me construye una lista []
    # donde cada elemento de ella es uno de los items que separé de acuerdo al
    # separador elegido, que en este caso era un espacio en blanco " "
    frase = frase.split(" ")
    #print(frase)

    for i in frase:
        if i == subfrase:
            count = count + 1
        else:
            continue
    print(count)

    return(count)


oracion = "Tengo mucho pica pica en el pica pica y Tengo pica"
palabra = "pica"

howmany = cuantas(oracion, palabra)
