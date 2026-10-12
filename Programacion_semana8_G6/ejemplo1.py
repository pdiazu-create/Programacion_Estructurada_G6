listas = [1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 3,"hola"]
print(listas)

conjuntos = [1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 3, "hola"]
print(conjuntos)

tuplas = (1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 3, "hola")
print(tuplas)

diccionario = {"estudiante": "Juan", "edad": 20, "carrera": "Ingeniería"}

print(diccionario)

diccionario["nota"] = 80

nuevaslistas = []
nuevaslistas.append(listas)
nuevaslistas.append(conjuntos)
nuevaslistas.append(tuplas)
nuevaslistas.append(diccionario)
print(diccionario)

for item in nuevaslistas:
    print(item)

for item in nuevaslistas:
    print(type(item))

with open("archivo.txt", "+w" , encoding="utf-8") as archivo:

    for item in nuevaslistas:
     archivo.write(str(item) + "\n")
