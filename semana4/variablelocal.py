def calcular_pago(horas, tarifa):
    pago = horas * tarifa
    print("Pago dentro de la función: C$", pago)
    return pago


calcular_pago(40, 120)
print("Pago fuera de la función: C$", calcular_pago(40, 120))  # Esto imprimirá el valor retornado por la función
