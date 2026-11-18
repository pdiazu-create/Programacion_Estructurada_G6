import time


def generar_peor_caso(cantidad):
    inicio = time.perf_counter()
    datos = list(range(cantidad, 0, -1))
    return datos, time.perf_counter() - inicio


def ordenamiento_burbuja(lista):
    inicio = time.perf_counter()
    n = len(lista)
    for i in range(n):
        intercambio = False
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:
            break
    return time.perf_counter() - inicio


def busqueda_lineal(lista, objetivo):
    inicio = time.perf_counter()
    for elemento in lista:
        if elemento == objetivo:
            break
    return time.perf_counter() - inicio


def main():
    try:
        cantidad = int(input("Cantidad de elementos: "))
    except ValueError:
        print("Ingresá un número entero positivo.")
        return
    if cantidad <= 0:
        print("Ingresá un número entero positivo.")
        return

    datos, tiempo_gen = generar_peor_caso(cantidad)
    print(f"Tiempo de generación: {tiempo_gen:.6f} segundos")

    objetivo = datos[-1]
    tiempo_busqueda = busqueda_lineal(datos, objetivo)
    print(f"Tiempo búsqueda lineal (peor caso): {tiempo_busqueda:.6f} segundos")

    print("Ordenando con burbuja...")
    tiempo_burbuja = ordenamiento_burbuja(datos)
    print(f"Tiempo ordenamiento burbuja (peor caso): {tiempo_burbuja:.6f} segundos")


if __name__ == "__main__":
    main()
