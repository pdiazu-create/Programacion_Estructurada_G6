try:
    edad = int(input("Edad: "))
    print("Edad registrada:", edad)
except ValueError:
    print("Ingrese un valor numerico.")
    