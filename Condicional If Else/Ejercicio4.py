# Realiza un programa que calcule la aceptación de una solicitud en base a
# los siguientes parámetros: edad Ynota
# se ingresa con mas de 18 años y con nota igual o mayor a 7

edad = int(input("Ingrese su edad: "))
nota = int(input("Ingrese la nota de su examen: "))
print("El aspirante puede ingresar")if edad >= 18 and nota >= 7 else print("El aspirante no puede ingresar")

