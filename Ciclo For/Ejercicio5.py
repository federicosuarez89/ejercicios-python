# Escriba un programa que pida dos números enteros y escriba la suma de todos los enteros
# desde el primer número hasta el segundo.
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
sumatoria = 0
for i in range(num1, num2+1):
    sumatoria = sumatoria + i
print(f"La sumatoria de los numeros entre {num1} y {num2} es: {sumatoria}")
