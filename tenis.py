a = int(input("Juegos ganados por A: ")) #Se piden los juegos ganados por A y B
b = int(input("Juegos ganados por B: "))


if (a > 7 or b > 7) or (a == 7 and b == 7): #Si alguno de los dos es mayor o ambos son iguales a 7, es inválido
    print("Inválido")
elif a==6 and b<5: #Si A gana 6 y la diferencia es menor a 2, gana A
    print("Ganó A")  
elif b==6 and a<5: #Si B gana 6 y la diferencia es menor a 2, gana B
    print("Ganó B")
elif a>=5 and b==7: #Si A es mayor 5 y B gana 7, gana B
    print("Ganó B")
elif b>=5 and a==7: #Si B es mayor 5 y A gana 7, gana A
    print("Ganó A")  
elif (a<=6 and b<=6) and (abs(a-b)<2): #Si ambos son menores a 6 y la diferencia es menor a 2, aún no termina
    print("Aún no termina")
else: #Si no se cumple ninguna de las anteriores, es inválido
    print("Inválido")