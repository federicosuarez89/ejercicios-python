# Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
num = int(input("Ingrese un numero mayor que cero "))
if num < 0:
    print("El numero ingresado es menor que cero")
else:
    print(f"El numero 0 es divisor de {num}")
    for i in range(1, num+1):

        if num % i == 0:
            divisores = i

            print(f"El numero {divisores} es divisor de {num}")
