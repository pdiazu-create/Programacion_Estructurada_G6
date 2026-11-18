import aritmetica as arit


def menu():
    print("Bienvenido a mi calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("0. Salir")


def readValues():
    num1 = float(input("Digite el primer numero: "))
    num2 = float(input("Digite el segundo numero: "))
    return num1, num2


def showAdd(num1, num2):
    result = arit.add(num1, num2)
    print(f"El resultado de la suma es: {result}")


def showSub(num1, num2):
    print(f"la diferencia de {num1} - {num2} es: {arit.sub(num1, num2)}")


def showMult(num1, num2):
    print(f"la multiplicacion de {num1} * {num2} es: {arit.mult(num1, num2)}")


def showDiv(num1, num2):
    print(f"la division de {num1} / {num2} es: {arit.div(num1, num2)}")


def chooseOp(op):
    if op == 1:
        num1, num2 = readValues()
        showAdd(num1, num2)
    elif op == 2:
        num1, num2 = readValues()
        showSub(num1, num2)
    elif op == 3:
        num1, num2 = readValues()
        showMult(num1, num2)
    elif op == 4:
        num1, num2 = readValues()
        showDiv(num1, num2)
    elif op == 0:
        print("Saliendo del programa...")
        return False
    else:
        print("Opcion invalida. Por favor, elige una opcion del 1 al 4")
    return True


def main():
    while True:
        menu()
        try:
            op = int(input("Digita el numero de la operacion que deseas realizar: "))
        except ValueError:
            print("Opcion invalida. Debes ingresar un numero.")
            input("Presiona Enter para continuar...")
            continue

        if not chooseOp(op):
            break

        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    main()
