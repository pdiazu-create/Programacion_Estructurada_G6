"""Menú principal para ejecutar los ejercicios de matrices."""

import matriz1
import matriz2
import matriz3
import matriz4
import matrizidentidad


def menu():
	"""Muestra el menú y ejecuta el ejercicio seleccionado."""
	opciones = {
		"1": ("Multiplicar una matriz por un escalar", matriz1.ejecutar),
		"2": ("Ingresar y mostrar una matriz", matriz2.ejecutar),
		"3": ("Sumar dos matrices 3x3", matriz3.ejecutar),
		"4": ("Multiplicar dos matrices 2x2", matriz4.ejecutar),
		"5": ("Crear una matriz identidad", matrizidentidad.ejecutar),
	}

	while True:
		print("\n=== MENÚ DE MATRICES ===")
		for numero, (descripcion, _) in opciones.items():
			print(f"{numero}. {descripcion}")
		print("0. Salir")

		seleccion = input("Seleccione una opción: ").strip()
		if seleccion == "0":
			print("¡Hasta luego!")
			break

		opcion = opciones.get(seleccion)
		if opcion is None:
			print("Opción no válida. Intente de nuevo.")
			continue

		print(f"\n--- {opcion[0]} ---")
		opcion[1]()


if __name__ == "__main__":
	menu()