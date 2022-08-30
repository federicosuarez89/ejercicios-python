# Realiza un programa que clasifique un triángulo por el tamaño de sus lados.
# Se debe clasificar como triángulo  isósceles, equilátero o escaleno.

lado1 = int(input("Ingrese el valor del primer lado: "))
lado2 = int(input("Ingrese el valor del segundo lado: "))
lado3 = int(input("Ingrese el valor del tercer lado: "))
if lado1 == lado2 & lado1 == lado3:
    print("El triangulo es equilatero")
elif lado1!= lado2 & lado1 != lado3:
    print("El triangulo es escaleno")
else:
    print("El triangulo es isosceles")
