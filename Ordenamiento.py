numeros = []
for i in range(4):
    numeros.append(int(input("Número " + str(i + 1) + ": ")))

for i in range(4):
    for j in range(i + 1, 4):
        if numeros[i] > numeros[j]:
            temp = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = temp

#numeros.sort()

print("El orden es: ", numeros)