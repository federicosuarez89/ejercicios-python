# Programa que calcula el IVA de una compra, siendo el IVA el 21% del total de la compra
def iva(compra):
    resultado=compra*1.21
    return resultado


compra=float(input("Ingrese el valor de su compra: "))
print(f"El precio final con el IVA incluido es {iva(compra)} ")