'''
Escriba una función de Python que tome una secuencia de números y determine
si todos los números son diferentes entre sí.
'''



numero = 5012890

list = []

numero = str(numero)

for i in numero:
    if i in list:
        print(i,"Ya se encuentra en la lista. Es un numero repetido")
        print("La secuencia de números NO es única.")
        break
    else:
        list.append(i)
print("Si no se ha indicado lo contario antes, los números de la secuencia son únicos")





#print(list)



#print(list)

#print(numero)

'''for i in numero:
    i = int(i)
    j = (i+1)
    print(i)
    print(j)
    if i in numero[i:]:
        print("Numero se repite")
    else:
        print("Número es único")'''
