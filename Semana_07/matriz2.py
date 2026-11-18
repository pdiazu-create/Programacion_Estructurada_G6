"""Permite ingresar y mostrar una matriz de tamaño elegido."""


def ejecutar():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    if filas <= 0 or columnas <= 0:
        print("Las dimensiones deben ser números positivos.")
        return

    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el valor de la posición [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)

    print("\nMatriz ingresada:")
    for fila in matriz:
        print(fila)


if __name__ == "__main__":
    ejecutar()
