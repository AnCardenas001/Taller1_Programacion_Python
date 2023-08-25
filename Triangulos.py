lado_a = float(input("a: "))
lado_b = float(input("b: ")) 
lado_c = float(input("c: "))

if lado_a + lado_b <= lado_c or lado_a + lado_c <= lado_b or lado_b + lado_c <= lado_a:
  print("No es un triángulo válido")
elif lado_a == lado_b and lado_b == lado_c:
  print("El triángulo es equilátero")
elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c: 
  print("El triángulo es isósceles")
else:
  print("El triángulo es escaleno")