# Crie uma função que mutiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variavel
def mutiplica (*args):
    total = 1
    for i in args:
        total *= i
    return total

resultado = mutiplica(2,5)
print(resultado)



# Crie uma função que diga se um número é par ou impar.
# retorne se o numero é par ou impar
def eh_par(numero):
    if numero%2 == 0:
        return f"O número {numero} é par "
    return f"O número {numero} é impar "

print(eh_par(5))