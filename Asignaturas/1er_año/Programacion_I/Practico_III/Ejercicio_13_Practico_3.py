'''
Escriba un programa en Python que acepte cuatro números como entrada y los
clasifique en orden descendente.
'''

'''
The sorted() function sorts the elements of a given iterable in a specific
order (ascending or descending) and returns it as a list.

The syntax of the sorted() function is:
sorted(iterable, key=None, reverse=False)

The sorted() function accepts a reverse parameter as an optional argument.
Setting reverse = True sorts the iterable in the descending order.
'''

def sorted_list (num1, num2, num3, num4):

    list = [num1, num2, num3, num4]

    print("La lista Original es: ", list)

    list_asc = sorted(list)
    print("La lista ordenada de forma ascendente es: ", list_asc)

    list_desc = sorted(list, reverse = True)
    print("La lista ordenada de forma descendente es: ",list_desc)


    return(list_desc)

# *---------------------*-----------------------*-----------------


lista_desc = sorted_list (29, 1004, 1, 4305)
