'''
Escriba un programa Python que reciba una fecha e imprima el día de la fecha.
Por ejemplo, si se recibe 02/08/2022, se debe imprimir 02 de Agosto del 2022.
'''

def dia_fecha (fecha):

    fecha_nueva = fecha.split("/")

    #print(fecha_nueva)

    #print(fecha_nueva[1])

    if fecha_nueva[1] == "01":
        print(fecha_nueva[0], "de Enero de ", fecha_nueva[2])

    elif fecha_nueva[1] == "02":
        print(fecha_nueva[0], "de Febrero de ", fecha_nueva[2])

    elif fecha_nueva[1] == "03":
        print(fecha_nueva[0], "de Marzo de ", fecha_nueva[2])

    elif fecha_nueva[1] == "04":
        print(fecha_nueva[0], "de Abril de ", fecha_nueva[2])

    elif fecha_nueva[1] == "05":
        print(fecha_nueva[0], "de Mayo de ", fecha_nueva[2])

    elif fecha_nueva[1] == "06":
        print(fecha_nueva[0], "de Junio de ", fecha_nueva[2])

    elif fecha_nueva[1] == "07":
        print(fecha_nueva[0], "de Julio de ", fecha_nueva[2])

    elif fecha_nueva[1] == "08":
        print(fecha_nueva[0], "de Agosto de ", fecha_nueva[2])

    elif fecha_nueva[1] == "09":
        print(fecha_nueva[0], "de Septiembre de ", fecha_nueva[2])

    elif fecha_nueva[1] == "10":
        print(fecha_nueva[0], "de Octubre de ", fecha_nueva[2])

    elif fecha_nueva[1] == "11":
        print(fecha_nueva[0], "de Noviembre de ", fecha_nueva[2])

    elif fecha_nueva[1] == "12":
        print(fecha_nueva[0], "de Diciembre de ", fecha_nueva[2])

    else:
        print("revisar")

# ***************----------------**********----------------------------

fecha = "16/12/2022"

dia = dia_fecha(fecha)






'''
meses = [1,2,3,4,5,6,7,8,9,10,11,12]
nombre_mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

fecha_nueva = fecha.split("/")

print(fecha_nueva)


print(fecha_nueva[1])


for i in meses:
    i = int(i)
    print(i)
    if i == fecha_nueva[1]:
        print(fecha_nueva[i], "de", nombre_mes[i], "del", fecha_nueva[2])
    else:
        continue
'''
