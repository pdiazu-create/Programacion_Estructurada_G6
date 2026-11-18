"""Dada una matriz cuadrada, convertirla a matriz de identidad."""
def crear_matriz_identidad(n):
    matriz_identidad = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        matriz_identidad.append(fila)
    return matriz_identidad


def ejecutar():
    try:
        tamaño = int(input("Ingrese el tamaño de la matriz identidad: "))
    except ValueError:
        print("El tamaño debe ser un número entero.")
        return

    if tamaño <= 0:
        print("El tamaño debe ser un número positivo.")
        return

    print("Matriz identidad:")
    for fila in crear_matriz_identidad(tamaño):
        print(fila)


if __name__ == "__main__":
    ejecutar()
