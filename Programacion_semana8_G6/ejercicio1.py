# Cree una aplicacion que lea los datos de un estudiante: nombres, apellidos, nota.
# Calcular el promedio de las notas, la nota mas alta y la nota mas baja.
# Mostrar los 3 estudiantes con mayor nota.

lista_estudiantes = []

cantidad = int(input("Ingrese la cantidad de estudiantes: "))

for i in range(cantidad):
    print(f"\nEstudiante {i + 1}")
    nombre = input("Ingrese los nombres: ")
    apellido = input("Ingrese los apellidos: ")
    nota = float(input("Ingrese la nota: "))

    estudiante = {
        "nombres": nombre,
        "apellidos": apellido,
        "nota": nota,
    }
    lista_estudiantes.append(estudiante)

notas = [estudiante["nota"] for estudiante in lista_estudiantes]

promedio = sum(notas) / len(notas) if notas else 0
nota_mas_alta = max(notas) if notas else 0
nota_mas_baja = min(notas) if notas else 0

top_3 = sorted(lista_estudiantes, key=lambda e: e["nota"], reverse=True)[:3]

print("\n=== RESULTADOS ===")
print(f"Promedio de notas: {promedio:.2f}")
print(f"Nota más alta: {nota_mas_alta}")
print(f"Nota más baja: {nota_mas_baja}")

print("\nTop 3 estudiantes con mayor nota:")
if top_3:
    for posicion, estudiante in enumerate(top_3, start=1):
        print(f"{posicion}. {estudiante['nombres']} {estudiante['apellidos']} - Nota: {estudiante['nota']}")
else:
    print("No hay estudiantes registrados.")