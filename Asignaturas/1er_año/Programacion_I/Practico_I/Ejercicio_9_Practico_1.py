# Calcularemos la media aritmética de dos números, solo si ambos son mayores
# que cero.

a = int(input("Número a =  "))
b = int(input("Número b =  "))

if (a and b > 0):
    media_aritmetica = (a + b) / 2
    print("La media aritmética es: ", media_aritmetica)
else:
    print("No se puede calcular la media aritmética")
