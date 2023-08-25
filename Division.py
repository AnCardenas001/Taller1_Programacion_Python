dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

if(dividendo % divisor == 0):
    print("La división es exacta.")
else:
    print("La división no es exacta")

Cociente = dividendo // divisor;
Residuo = dividendo % divisor;

print("Cociente: ", Cociente)
print("Residuo: ", Residuo)