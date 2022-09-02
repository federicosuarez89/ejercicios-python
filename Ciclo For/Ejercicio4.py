# Escriba un programa que pregunte cuantos números se van a introducir, pida esos números
# (que puedan ser decimales) y calcule su suma.
numIntroducir = int(input("Ingrese la cantidad de numeros que se van a evaluar: "))
sumatoria = 0
for i in range(0, numIntroducir):
    numSumar = float(input("Ingrese el valor a sumar: "))
    sumatoria = numSumar + sumatoria
print(f"El resultado de la suma es {sumatoria}")
