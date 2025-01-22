# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def du_tri_quadruplicar(numero):
    duplo = numero * 2
    triplo = numero *3
    quadruplo = numero * 4

    return f"o dobro de {numero} é {duplo}, o triplo de {numero} é {triplo} e o quadruplo de {numero} é {quadruplo}"

print(du_tri_quadruplicar(2))
