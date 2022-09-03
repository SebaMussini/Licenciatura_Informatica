'''
 Escriba un programa en Python que resuelva el sistema de ecuaciones:
   𝑎𝑥 + 𝑏𝑦 = 𝑐
   𝑑𝑥 + 𝑒𝑦 = 𝑓
Imprimir los valores de x, y donde se conocen a, b, c, d, e y f

'''

a = 2
b = 5
c = 12
d = 6
e = 9
f = 15


resto = (d/a)
#print(resto)

ecu1 = ( (a*(-resto)) + (b*(-resto)) )
#print(ecu1)

ecu2 = ecu1 + (d+e)
#print(ecu2)

ecu3 = (c*(-resto)) + f
#print(ecu3)

y = ecu3 / ecu2
print("El valor de y es: ", y)

x = ((c - (b*y))/a)
print("El valor de x es: ", x)

control1 = print("El control de la primera ecuación (a*x)+(b*y) es: ", (a*x)+(b*y))
control1 = print("El contro de la segunda ecuación (d*x)+(e*y) es: ", (d*x)+(e*y))



'''

(a*x) + (b*y) = c

(d*x) + (e*y) = f


2x + 5y = 12
6x + 9y = 15
-------------
-15y + 9y = (12*(-3)) + 15

-6y = -36 +15
-6y = -21
y = 21/6

2x + (5*3.5) = 12
x = (12-(5*3.5))/2


'''
