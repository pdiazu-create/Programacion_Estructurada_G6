"""Lee dos matrices 2x2 y muestra su producto."""


def ejecutar():
    matrices = []
    for numero in range(1, 3):
        matriz = []
        print(f"Ingrese los valores de la matriz {numero} 2x2:")
        for i in range(2):
            fila = []
            for j in range(2):
                valor = float(input(f"Ingrese el valor de la posición ({i + 1},{j + 1}): "))
                fila.append(valor)
            matriz.append(fila)
        matrices.append(matriz)

    matriz_resultado = []
    for i in range(2):
        fila = []
        for j in range(2):
            suma = sum(matrices[0][i][k] * matrices[1][k][j] for k in range(2))
            fila.append(suma)
        matriz_resultado.append(fila)

    print("La matriz resultante es:")
    for fila in matriz_resultado:
        print(fila)


if __name__ == "__main__":
    ejecutar()
