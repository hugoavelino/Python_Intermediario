def divisaoFn(x, y):
    return x / y

def multiplicacaoFn(x, y):
    return x * y

def potenciacaoFn(x, y):
    return x ** y


numeros = [1, 2, 3, 4, 5]
divisao = [divisaoFn(numero,2) for numero in numeros]
multiplicacao = [multiplicacaoFn(numero , 2) for numero in numeros]
quadrado = [potenciacaoFn(numero, 2) for numero in numeros]


print(numeros)
print(divisao)
print(multiplicacao)
print(quadrado)