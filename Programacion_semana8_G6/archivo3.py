nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
carrera = input("Ingrese su carrera: ")

datos = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nCarrera: {carrera}\n"

with open("mis_datos.txt", "w", encoding="utf-8") as file:
    file.write(datos)

print ("Datos guardados correctamente en mis_datos.txt")