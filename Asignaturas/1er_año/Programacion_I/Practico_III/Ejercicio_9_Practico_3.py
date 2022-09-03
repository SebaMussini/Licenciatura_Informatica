'''
Escriba un programa para aceptar una cadena del usuario y mostrar los
caracteres que están presentes en un número de índice par. Por ejemplo,
show_even(‘python’) debe imprimir caracteres ‘p’, ‘t’, ‘o’.
'''


def cadena (palabra):

    palabra = str(palabra)

    # Creo una lista vacia
    list = []

    # Itero sobre cada una de las letras de la palabra y las agrego de forma
    # individual a la lista
    for i in palabra:
        list.append(i)

    # Para cada elemento de la lista, verifico si la posiciòn que ocupa (es decir,
    # el índice) es par o impar. Si es par, la imprime. Si no es par, continúa.
    for n in list:
        # print([n])
        # print(list.index(n))
        if (list.index(n) % 2 == 0):
            print([n])
        else:
            continue

    return(n)




a = cadena(input("Ingrese una cadena de strings"))
