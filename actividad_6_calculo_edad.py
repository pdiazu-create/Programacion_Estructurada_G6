from datetime import date


ano_nacimiento = int(input("Ingresa tu año de nacimiento: "))
ano_actual = date.today().year
edad = ano_actual - ano_nacimiento

print(f"Tu edad aproximada es: {edad} años.")