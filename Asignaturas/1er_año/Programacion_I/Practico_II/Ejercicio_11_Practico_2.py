'''. En la siguiente tabla se muestra el número de camas de las habitaciones de
una casa rural, además de la planta donde está ubicada cada una de ellas:

Diseñe un archivo que
● Tenga un método que muestre el listado de las habitaciones de la casa rural.
● Tenga otro método que reciba como parámetro un número de habitación y
muestre por pantalla la planta y el número de camas de la habitación
seleccionada. (Utilice la estructura switch para resolverlo)
Nota: Si el número introducido por el usuario, no está asociado a ninguna
habitación, se mostrará el mensaje: "ERROR: El <número> no está asociado a
ninguna habitación.".

'''












# Ingreso las habitaciones, camas y plantas en formato de lista, utilizando
# para ello los paréntesis rectos   [ ]

habitacion = ["1. Azul", "2. Roja", "3. Verde", "4. Rosa", "5. Gris"]
camas = ["2", "1", "3", "2", "1"]
planta = ["Primera", "Primera", "Segunda", "Segunda", "Tercera"]

# -------------------------------------------------------------------------

# Punto a)   Muestro el listado de habitaciones

print(habitacion)
print("\n\n\n")

# -------------------------------------------------------------------------

# Punto b)

# Solicito al usuario que me indique el número de la habitación que desea,
# con la restriccin que debe ser MAYOR que cero y MENOR estricto que 6
# pues solo tengo 5 habitaciones.

def listado (nro_hab):

    if  0 < nro_hab < 6:
        nro_hab_index = habitacion [nro_hab - 1]
    else:
        print("ERROR: ", nro_hab, " no está asociado a ninguna habitacion.")

    num_asociado_hab = int(nro_hab_index[0])
# print(num_asociado_hab)

    print("\n\n\n")
    print("Ud. eligió la habitación llamada ", nro_hab_index, ", asociada con el número ", num_asociado_hab)

    return (num_asociado_hab)


cliente = listado(int(input("Elija su habitación")))







# -------------------------------------------------------------------------

# Punto  c)

# Indico que de la lista "planta" y "camas", me traiga el elemento que esté
# en el lugar (index) (numero elegido por el usario  -  1)

def descripcion (num_asociado_hab):


    if num_asociado_hab == 1:
        print("La habitación tiene 2 camas y se encuentra en la primera planta")
    elif num_asociado_hab == 2:
        print("La habitación tiene 1 cama y se encuentra en la primera planta")
    elif num_asociado_hab == 3:
        print("La habitación tiene 3 camas y se encuentra en la segunda planta")
    elif num_asociado_hab == 4:
        print("La habitación tiene 2 camas y se encuentra en la segunda planta")
    elif num_asociado_hab == 5:
        print("La habitación tiene 1 cama y se encuentra en la tercera planta")

    return(num_asociado_hab)


descrip = descripcion(int(input("Ingrese el número de su habitación")))
