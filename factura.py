# Solicitar los datos de la compra
producto = input("Digite el nombre del producto: ")
precio = float(input("Digite el precio del producto: "))
cantidad = int(input("Digite la cantidad: "))

# Calcular el subtotal
subtotal = precio * cantidad

# Mostrar el resumen de la compra
print("\nResumen de la compra")
print("Producto:", producto)
print("Precio unitario: C$", precio)
print("Cantidad:", cantidad)
print("Subtotal: C$", subtotal)
