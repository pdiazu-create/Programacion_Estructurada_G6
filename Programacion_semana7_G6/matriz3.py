"""Lee dos matrices 3x3 y muestra su suma."""


def ejecutar():
    matrices = []
    for numero in range(1, 3):
        matriz = []
        print(f"Ingrese los valores de la matriz {numero} 3x3:")
        for i in range(3):
            fila = []
            for j in range(3):
                valor = int(input(f"Ingrese el valor de [{i}][{j}]: "))
                fila.append(valor)
            matriz.append(fila)
        matrices.append(matriz)

    print("\nMatriz suma:")
    for i in range(3):
        fila_suma = [matrices[0][i][j] + matrices[1][i][j] for j in range(3)]
        print(fila_suma)


if __name__ == "__main__":
    ejecutar()

