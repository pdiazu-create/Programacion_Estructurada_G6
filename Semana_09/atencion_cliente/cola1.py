from collections import deque

cola = deque()

# Agregar
cola.append(10)
cola.append("diez")
cola.appendleft("embarazada")

print(cola)

# Sacar
cola.popleft()
print(cola)


def agregar(dato):
    cola.append(dato)


def trash():
    if cola:
        return cola.popleft()
    else:
        return "No hay nada en la cola"


def show():
    return cola


print(trash())
print(show())