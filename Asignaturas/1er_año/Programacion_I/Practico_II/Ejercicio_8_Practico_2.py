# Defina un archivo que permita representar una serie aritmética.
# Una serie aritmética viene caracterizada por el primer elemento de la serie
# y el incremento o diferencia entre dos elementos sucesivos de la serie.
# Implemente un método que permita calcular la suma de los n primeros
# elementos de la serie (utilice un bucle para realizar esta operación).



# "numero" es el valor en el que comienza y "n" el incremento constante
# que acumula en la progresión.

def serie (numero, n):

    # Defino una variable "suma" para que luego acumule dentro del bucle
    suma = 0

    # Defino el primer número con el cual comenzará la progresión
    serie_geom = numero


    # El bucle funcionará hasta que el penúltimo valor de la progresión sea
    # menor que 20 (porque entrado ese valor, aún calculará uno más)
    while (serie_geom < 20):

        # Acumulo en la variable "serie_geom"
        serie_geom = serie_geom + n

        # Acumulo en la variable suma
        suma = suma + serie_geom

        print(serie_geom)

    print("La suma de toda la serie geométrica es", suma)


    return(serie_geom)


serie_1 = serie(2, 4)
