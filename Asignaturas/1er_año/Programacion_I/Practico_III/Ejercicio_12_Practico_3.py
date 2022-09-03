'''
2. Escriba un programa en Python para calcular e imprimir la suma de dos enteros
dados (mayores o iguales a cero). Si se dan enteros o la suma tiene más de 10
dígitos, imprimir "overflow".
'''

def overflow (num1, num2):

    numSum = num1 + num2

    num1str = str(num1)
    print(len(num1str))

    num2str = str(num2)
    print(len(num2str))

    numSumstr = str(numSum)
    print(len(numSumstr))

    if len(num1str) > 10:
        print("Overflow")
    elif len(num2str) > 10:
        print("Overflow")
    elif len(numSumstr) > 10:
        print("Overflow")
    else:
        print(numSum)

    return(numSum)

# *-------------*-----------------*-----------------

a = 9999999
b = 999915989

over = overflow(a,b)


c = 9999999
d = 9999159899

over2 = overflow(c,d)
