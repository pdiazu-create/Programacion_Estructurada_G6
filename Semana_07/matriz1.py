"""Multiplica una matriz fija 2x2 por un escalar ingresado."""


def ejecutar():
    matriz = [[1, 2], [3, 4]]
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    escalar = float(input("Ingrese el escalar: "))
    matriz_resultado = [
        [escalar * valor for valor in fila]
        for fila in matriz
    ]

    print(f"\nMatriz multiplicada por {escalar:g}:")
    for fila in matriz_resultado:
        print(fila)


if __name__ == "__main__":
    ejecutar()
