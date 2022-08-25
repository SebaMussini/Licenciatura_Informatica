# Debe contar SOLO los números mayores que cero y sumarlos.
# Los negativos NO los cuenta ni los suma.
# Sale del bucle "while"  SOLAMENTE cuando el numero ingresado es CERO

count = 0
suma = 0

num = int(input("Ingrese un número "))
if num > 0:
    count = count + 1
    suma = suma + num

while num != 0:
    num = int(input("Ingrese un número "))
    if num > 0:
        count = count + 1
        suma = suma + num

print(count)
print(suma)
