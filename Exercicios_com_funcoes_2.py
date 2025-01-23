# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def du_tri_quadruplicar(numero):
#     duplo = numero * 2
#     triplo = numero *3
#     quadruplo = numero * 4

#     return f"o dobro de {numero} é {duplo}, o triplo de {numero} é {triplo} e o quadruplo de {numero} é {quadruplo}"

# print(du_tri_quadruplicar(2))


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
