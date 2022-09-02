# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números
# y diga al final cuántos han sido pares y cuántos impares.

contadorPares = 0
contadorImpares = 0
contadorNum = int(input("Cuantos numeros va a ingresar para ser evaluados: "))
for i in range(0, contadorNum):
    num = int(input("Ingrese un valor para saber si es par o impar: "))
    if num % 2 == 0:
        contadorPares += 1
    else:
        contadorImpares += 1
print(f"Se ingresaron {contadorPares} numeros pares y {contadorImpares} impares")



