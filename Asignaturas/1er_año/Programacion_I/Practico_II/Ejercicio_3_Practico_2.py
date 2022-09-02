# Defino la función que calcule la capacidad/tamaño del disco

# 1 kilo-byte = 1024 bytes
# 1 mega-byte = 1024 kilo-byte = (1024**2) bytes
# 1 giga-byte = 1024 mega-byte = (1024**2) kilo-bytes = (1024**3) bytes

def capacidad_disco (cilindros, pistas, sectores, bytes):

    capacidad = cilindros * pistas * sectores * bytes

    print("El tamaño del disco es: {0}".format(capacidad), " bytes")

    print("El tamaño del disco es: {0}".format((capacidad)/1024), " kilo-bytes")

    print("El tamaño del disco es: {0}".format((capacidad)/1024**2), " mega-bytes")

    print("El tamaño del disco es: {0}".format((capacidad)/1024**3), " giga-bytes")

    return capacidad


tamaño_disco = capacidad_disco (12000, 16, 8, 512)
