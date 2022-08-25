# Un número primo es un numero natural que tiene unicamente dos divisores
# positivos distintos:  él mismo y 1


num = int(input("Ingrese un número natural mayor que 1     "))

r = num % num
h = num % 1
j = num % 2

if ( (r == 0) and (h == num) and (j != 0) ):
    print(num, "es número primo")
else:
    print(num, "NO ES número primo")
