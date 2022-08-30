# Crea un programa que pida al usuario dos números y muestre el resultado de su división.
# Si el segundo número es 0, debe mostrar un mensaje de error.
def resultado():
    operacion = num1/num2
    return operacion


num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese el segundo numero: "))
if num2==0:
    print(f"No se puede dividir por cero")
else:
    print(f"El resultado de la division es {resultado()}")
