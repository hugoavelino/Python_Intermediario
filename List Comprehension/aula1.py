# List comprehension em Python
# List comprehension é uma forma concisa de criar listas em Python
# a partir de iteráveis
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)