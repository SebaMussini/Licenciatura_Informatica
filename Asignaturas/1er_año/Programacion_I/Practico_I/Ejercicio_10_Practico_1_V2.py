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

nro_hab = int(input("Elija el número de su habitación."))
if  0 < nro_hab < 6:
    nro_hab_index = habitacion [nro_hab - 1]
else:
    print("ERROR: ", nro_hab, " no está asociado a ninguna habitacion.")

num_asociado_hab = int(nro_hab_index[0])
# print(num_asociado_hab)

print("\n\n\n")
print("Ud. eligió la habitación llamada ", nro_hab_index, ", asociada con el número ", num_asociado_hab)

# -------------------------------------------------------------------------

# Punto  c)

# Indico que de la lista "planta" y "camas", me traiga el elemento que esté
# en el lugar (index) (numero elegido por el usario  -  1)

planta_hab = (planta[nro_hab - 1])
camas_hab = (camas[nro_hab - 1])

#print(planta_hab)
print("\n\n\n")
oracion_1 = print("La planta de la habitación ", nro_hab_index, "es la ", end =" ")
oracion_2 = print(planta_hab," planta.", end = " ")
oracion_3 = print("Dicha habitación tiene ", camas_hab, " camas.")

#print(oracion_1 + oracion_2 + oracion_3)
