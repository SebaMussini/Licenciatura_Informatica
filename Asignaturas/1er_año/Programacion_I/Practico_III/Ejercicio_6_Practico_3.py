'''
Escriba un programa en Python para verificar la prioridad y precedencia de los
cuatro operadores aritméticos (+, -, *, /) y tres booleanos (and, or, not).
'''

'''
Python sigue la regla de PEMDAS. PEMDAS significa paréntesis, exponentes,
multiplicación y división, y suma y resta.

Aquí está la tabla de precedencia completa, de la precedencia más baja a la más
alta. Una fila tiene la misma precedencia y cadenas de izquierda a derecha

 0. :=
 1. lambda
 2. if – else
 3. or
 4. and
 5. not x
 6. in, not in, is, is not, <, <=, >, >=, !=, ==
 7. |
 8. ^
 9. &
 10. <<, >>
 11. +, -
 12. *, @, /, //, %
 13. +x, -x, ~x
 14. **
 14. await x
 15. x[index], x[index:index], x(arguments...), x.attribute
 16. (expressions...), [expressions...], {key: value...}, {expressions...}

 '''

def prioridad (operacion):

    list = []

    for i in operacion:
        list.append(i)

    print(list)

    for i in list:
        if i in ("+", "-","*","/"):
            print("Los operadores matemáticos tienen prioridad sobre los booleanos")
            print("Entre los matemáticos, ('*' y '/') tienen prioridad sobre ('+','-')")

        elif i in ("not","and","or"):
            print("Entre los booleanos, 'not' tiene prioridad sobre 'and' y éste sobre 'or'")

        else:
            continue

    return(operacion)


a = prioridad("250+800 or 200+90")
