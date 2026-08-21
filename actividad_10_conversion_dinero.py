dolares = float(input("Ingresa la cantidad en dólares: "))
tasa_cambio = float(input("Ingresa la tasa de cambio a córdobas: "))

cordobas = dolares * tasa_cambio
print(f"{dolares:.2f} dólares representan {cordobas:.2f} córdobas.")