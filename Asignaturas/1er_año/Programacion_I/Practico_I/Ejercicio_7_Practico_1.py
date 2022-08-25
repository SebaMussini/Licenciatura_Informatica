# El contenido de la variable "a" que ingresará el usuario, será
# del tipo "int" (interger): un número

a = int(input("Numero"))

resultado = 1

while (a > 1):
    resultado = resultado * a
    a = a - 1

print(resultado)
