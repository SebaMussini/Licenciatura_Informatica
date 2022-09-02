# Escriba un archivo con un método que permite dibujar una pirámide como la de
# la figura:
#      *
#     ***
#    *****
#   *******
#  *********
# El método tendrá que recibir como argumento la altura de la pirámide


altura = 5

lista = []

for i in range(altura+1):

    lista.append(i)

print(lista)

for n in lista:

    h = lista.index(n) + lista.index(n+1)

    print(h)



    # n = range.index (i) + range.index(i+1)
