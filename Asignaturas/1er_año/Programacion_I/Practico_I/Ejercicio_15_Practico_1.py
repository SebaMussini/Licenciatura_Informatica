# Defino todos los numeros enteros entre -15 y -3 a traves de la funcion
#  range (cuidado si toma o no los números limites)

for i in range(-15,-2):
    r = i % 3
    if r == 0:
        print(r)
