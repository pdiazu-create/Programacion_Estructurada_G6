import notas


def pedir_notas():
    cantidad = int(input("Cuantas notas desea ingresar: "))
    lista_notas = []

    for i in range(cantidad):
        nota = float(input("Digite la nota " + str(i + 1) + ": "))
        lista_notas.append(nota)

    return lista_notas


def mostrar_notas():
    lista_notas = pedir_notas()
    notas_clasificadas = notas.classify_notes(lista_notas)

    print("\nNotas ingresadas:")
    for nota, clasificacion in notas_clasificadas:
        print("Nota:", nota, "-", clasificacion)


mostrar_notas()