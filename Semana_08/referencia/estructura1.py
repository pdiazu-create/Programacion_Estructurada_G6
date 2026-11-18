
lista = [1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 1, "hola"]
print(lista)

conjuntos = [1, 2, 3, 13, 4, 5, 6, 2, 0, 1, 2, 1, "hola"]
print(conjuntos)

tuplas = [1, 2, 3, 4, 5, 6, 2, 0, 1, 2, 1, "hola"]
print(tuplas)

diccionario = {
    "estudiante": "juanito",
    "sexo": "hombre",
    "nota": "85"
}
print(diccionario)

diccionario["nota"] = 80
print(diccionario)

nueva_lista = []
nueva_lista.append(lista)
nueva_lista.append(conjuntos)
nueva_lista.append(tuplas)
nueva_lista.append(diccionario)

print(nueva_lista)

for item in nueva_lista:
    print(item)

for item in nueva_lista:
    print(type(item))

with open ("texto.txt","+w",encoding="utf-8")as archivo:
    archivo.write(str(item) + "\n")



    
