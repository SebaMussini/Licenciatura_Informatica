'''Escriba un programa en Python que acepte el nombre y apellido del usuario y
los imprima en orden inverso con una coma y espacio entre ellos. Usar input().'''


'''[indice_inicial: indice_final] Es lo que se conoce como rebanado (slicing),
permite básicamente obtener un fragmento (rebanada) de algún objeto indizable.
Es decir, seleccionará desde el item con el indice inicial que indiquemos,
hasta el elemento con el índice final (no incluido).

Ejemplo: cad = "abcdefghijklmnñopqrstuvwxyz"
cad[5:]   # Desde el índice 5 hasta el final
"fghijklmnñopqrstuvwxyz"

Por otro lado Python permite usar índices negativos, siendo -1 el índice
del último elemento, -2 el del penúltimo, etc:

>>> cad[-6: -2]
"uvwx"


Además tenemos un tercer parámetro, conocido como paso (step):

[indice_inicial: indice_final: paso]
'''



identificacion = input("Ingrese su nombre y apellido")

# Ahora sustituiré el espacio entre el nombre y apellido por una coma

identificacion = identificacion.replace(" ", " , ")

print(identificacion)

# Por ejemplo, si quiero el último caracter de toda la cadena de string,
# la pido de la siguiente manera:

print(identificacion[-1])

# Ahora le pediré toda la cadena de string pero comenzando desde el final.
# Es decir, le pido todo [start:stop:step] con un paso de 1, pero comenzando
# desde el final , y por eso arranca desde el MENOS 1

ident_inverse = identificacion[::-1]

print(ident_inverse)
