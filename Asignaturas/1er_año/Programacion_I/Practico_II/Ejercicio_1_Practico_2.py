# Creo una funcion que me convertirá grados Celsius a grados farenheit

# la estructura de una función siempre es:

#  def   nombre_de_la_funcion   (variable/argumento/insumo)
#  luego, se le indica qué es lo que tiene que hacer la función (el programa)
#  y el    return    SIEMPRE va al final, pues es la última línea que lee
#  antes de salir de la  función.

def conversion (temperatura_celcius):

    farenheit = ( (9/5) * (temperatura_celcius) ) + 32

    # print(farenheit)

    return farenheit


# ahora que he creado mi función llamada  "conversión", la haré funcionar.
# le pido al usuario que ingrese un número que asignaré a la variable
#  "temp_celsius"
# luego, creo una variable llamada   "temp_farenheit"  donde se guardará
# el resultado de aplicar la función "conversión" con el valor/insumo
# "temp_celsius".  El   return   de la función  "conversión", se guardará
# en la variable    "temp_farenheit"
temp_celsius = int(input("Ingrese la temperatura en grados Celsius"))


temp_farenheit = conversion(temp_celsius)

print(temp_farenheit)
