'''Defina un archivo que implemente una estructura de control de loop y muestre
por pantalla el avance de la iteración pero solo cuando (i % 9 == 0) y que se
corte cuando i = 74. La salida en pantalla tiene que ser la siguiente:
0
9
18
27
36
45
63
72'''



for i in range(200):

    # Mientra "i" sea menor o igual a 74
    while i <= 74:

        # ¿El resto de "i" divido 9 es idéntico a cero? En caso positivo
        # entonces imprimo "i" y luego break (salgo del loop).
        if (i % 9) == 0:
            print (i)
            break
        # Si el resto NO es idéntico a cero, entonces break (salgo de loop)
        else:
            break
