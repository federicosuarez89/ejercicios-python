# Escriba un programa que pida dos números enteros y escriba qué números son pares
# y cuáles impares desde el primero hasta el segundo.

num1 = int(input("Ingrese el primer numero "))
num2 = int(input("Ingrese el segundo numero "))
for i in range(num1, num2+1):
    if i % 2 == 0:
        print(f"El numero {i} es par")
    if i % 2 != 0:
        print(f"El numero {i} es impar")