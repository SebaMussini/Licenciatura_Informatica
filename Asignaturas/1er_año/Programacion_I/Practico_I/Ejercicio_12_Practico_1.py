import math

radio = int(input("Ingrese el radio de la esfera"))

while radio <= 0:
    print("El radio debe ser mayor que cero")

    # Pido de nuevo el radio dentro del bucle porque sino queda corriendo
    # infinitamente.
    radio = int(input("Ingrese el radio de la esfera"))

pi = math.pi

area = 2 * pi * (radio**2)

print("El area es: ", area)
