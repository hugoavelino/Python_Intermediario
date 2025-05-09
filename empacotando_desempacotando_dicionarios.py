# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Hugo',
    'sobrenome': 'Motta',
}

dados_pessoa = {
    'idade': 30,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa, dados_pessoa)
# a,b = pessoa
# a,b = pessoa.values()
# a,b = pessoa.items()

# args e kwargs
# args ( já vimos)
#kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args , **kwargs):
    print('NÃO NOMEADOS:', args)
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(nome='Hugo', qlq=123)

# mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)