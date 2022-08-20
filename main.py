# Programa que toma las 3 notas de un alumno y diga la notal final del curso.
# Tener en cuenta que la nota 1 y 2 valen el 30% de la final y la nota 3 un 40%.
def note1y2(nota):
    resultado=nota*0.3
    return resultado


def note3(nota):
    resultado=nota*0.4
    return resultado


nota1 = float(input("Ingrese su primer nota: "))
nota2 = float(input("Ingrese su segunda nota: "))
nota3 = float(input("Ingrese su tercer nota: "))
notaFinal = note1y2(nota1)+note1y2(nota2)+note3(nota3)
print(f"La nota final es {notaFinal}")
