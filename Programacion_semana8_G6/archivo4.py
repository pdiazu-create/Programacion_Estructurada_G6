#crea un programa que permita guardar n cantidad de notas en un archivo, leer las notas, calcular el promedio y, la nota más alta y la más baja.

def calcular_promedio(notas):
    return sum(notas) / len(notas)


def calcular_maxima(notas):
    return max(notas)


def calcular_minima(notas):
    return min(notas)


file_name = "notas.txt"
file = open(file_name, "a", encoding="utf-8")
notas = []
cantidad_notas = int(input("Ingrese la cantidad de notas que desea guardar: "))

for i in range(cantidad_notas):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)
    file.write(str(nota) + "\n")

file.close()

print(f"El promedio es: {calcular_promedio(notas)}")
print(f"La nota máxima es: {calcular_maxima(notas)}")
print(f"La nota mínima es: {calcular_minima(notas)}")
