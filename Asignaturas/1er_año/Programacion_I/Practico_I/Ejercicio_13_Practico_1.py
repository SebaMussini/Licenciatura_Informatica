count = 0
suma = 0

# Las variables "count" y "suma" son para acumular

numero = int(input("Ingrese un número entero "))

count = count + 1
suma = suma + numero

print("Ud. ha introducido: ", count, "numeros y la suma es: ", suma)

otro_numero = input("¿Desea introducir otro número? Indique 'si'   o   'no' ")
while otro_numero == "si":
    numero = int(input("Ingrese un número entero "))
    count = count + 1
    suma = suma + numero
    otro_numero = input("¿Desea introducir otro número? Indique 'si'   o   'no' ")


print("Ud. ha introducido: ", count, "numeros y la suma es: ", suma)

media_aritmetica = suma/count

print("La media aritmética es: ", media_aritmetica)
