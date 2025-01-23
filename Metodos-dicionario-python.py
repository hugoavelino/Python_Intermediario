# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# pessoa = {
#     'nome': 'Hugo',
#     'sobrenome': 'Motta',
#     'idade': 32
# }

# pessoa.setdefault('idade', None)
# print(pessoa['idade'])

#print(len(pessoa))
# print(list(pessoa.keys()))
#print(list(pessoa.values()))
# print(list(pessoa.items()))

# for chave in pessoa:
#     print(chave)

# for chave, valor in pessoa.items():
#     print(chave, valor)
# import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1,2]
# }
# d2 = d1.copy()
# d2['li'][1] = 999999

# d2['c1'] = 1000
# print(d1)
# print(d2)

p1 = {
    'nome': 'Hugo',
    'sobrenome': 'Motta'
}

# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 32
# })

# p1.update(nome='novo valor', idade=32)
tupla = (('nome', 'novo valor'), ('idade', 32))
lista = [['nome', 'novo valor'], ['idade', 32]]
p1.update(lista)
print(p1)