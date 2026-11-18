
pila = []

def apilar():
    caja = input("Ingrese el nombre de la caja: ")
    pila.append(caja)
    print("Caja apilada correctamente.")

def desapilar():
    if len(pila) > 0:
        print("Caja retirada:", pila.pop())
    else:
        print("La pila esta vacia.")

def consultar_tope():
    if len(pila) > 0:
        print("Caja en el tope:", pila[-1])
    else:
        print("La pila esta vacia.")

def mostrar_pila():
    if len(pila) > 0:
        print("Cajas en la pila:")
        for caja in reversed(pila):
            print(caja)
    else:
        print("La pila esta vacia.")

def menu():
    while True:
        print("\n--- MENU DE PILA DE CAJAS ---")
        print("1. Apilar caja")
        print("2. Desapilar")
        print("3. Consultar tope")
        print("4. Mostrar pila")
        print("5. Salir")

        opciones = input("Ingrese la opcion: ")

        if opciones == "1":
            apilar()
        elif opciones == "2":
            desapilar()
        elif opciones == "3":
            consultar_tope()
        elif opciones == "4":
            mostrar_pila()
        elif opciones == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida.")

menu()
