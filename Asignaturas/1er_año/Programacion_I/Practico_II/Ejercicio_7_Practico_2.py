# Un año es bisiesto si es divisible entre 4
# Si NO es divisible entre 4, es biciesto si a la vez es divisible por
# 100 y también por sea por 400

año = int(input("Ingrese año"))

if ((año % 4) == 0) or (((año % 100) == 0) and ((año % 400) == 0)):
    print(año, "es año bisiesto")
else:
    print("No es biciesto")
