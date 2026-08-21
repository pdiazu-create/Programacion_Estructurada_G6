precio = float(input("Ingresa el precio del producto: "))
porcentaje_descuento = float(input("Ingresa el porcentaje de descuento: "))

descuento = precio * porcentaje_descuento / 100
precio_final = precio - descuento
print(f"Descuento aplicado: {descuento:.2f}")
print(f"Precio final: {precio_final:.2f}")