# Creamos un método/función que calcule la distancia recorrida, dado que
# la velocidad es constante por una magnitud de 3.2 metros por segundo.


def distancia (tiempo_segundos):

    distancia_metros = 3.2*tiempo_segundos

    print("La distancia recorrida fue de: {0}".format(distancia_metros), "metros")

    return distancia_metros



tiempo = int(input("Ingrese el tiempo en segundos"))

distancia = distancia (tiempo)
