'''

Escriba un programa en Python que acepte del usuario el radio de un círculo y
calcule el área. Puede servir función input().

'''

import math

# La fórmula del Área de un círculo es:    Área = Pi * (r)**2

def area (radio):

    area = math.pi * ((radio)**2)

    print("El área del círculo es: ", area)

    return(area)


calcular_area = area(int(input("Ingrese el radio del círculo")))
