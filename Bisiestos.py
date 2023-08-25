
años = int(input("Introduzca un año: "))

if años % 4 == 0 and años % 100 != 0:
    print("Es bisiesto")
elif años % 400 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")

    #primero se comprueba si el año es divisible entre 4, y si no es divisible entre 100 lo que significa que no es el ultimo
    #año del siglo, entonces es bisiesto. Luego si el ultimo año del siglo es divisible entre 400, entonces es bisiesto. 
    #Si no se cumple ninguna de las no es bisiesto.

    