# Realiza un programa que pida un número por teclado y nos indique si es par o impar.

numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print(f"El numero ingresado {numero} es par")
else:
    print(f"El numero ingresado {numero} es impar")