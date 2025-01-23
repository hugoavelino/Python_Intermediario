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

# Exemplo de dicionário
# pessoa = {
#     'nome': 'Hugo',
#     'sobrenome': 'Motta',
#     'idade': 32
# }

# Adiciona a chave 'idade' com valor None se não existir
# pessoa.setdefault('idade', None)
# print(pessoa['idade'])  # Imprime o valor da chave 'idade'

# Imprime a quantidade de chaves no dicionário
# print(len(pessoa))
# Imprime uma lista com as chaves do dicionário
# print(list(pessoa.keys()))
# Imprime uma lista com os valores do dicionário
# print(list(pessoa.values()))
# Imprime uma lista de tuplas (chave, valor) do dicionário
# print(list(pessoa.items()))

# Itera sobre as chaves do dicionário e as imprime
# for chave in pessoa:
#     print(chave)

# Itera sobre as chaves e valores do dicionário e os imprime
# for chave, valor in pessoa.items():
#     print(chave, valor)

# Importa o módulo copy para fazer cópias de dicionários
# import copy

# Exemplo de cópia rasa (shallow copy) de dicionário
# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1,2]
# }
# d2 = d1.copy()  # Faz uma cópia rasa de d1
# d2['li'][1] = 999999  # Modifica um valor na lista dentro do dicionário copiado

# Modifica um valor no dicionário copiado
# d2['c1'] = 1000
# print(d1)  # Imprime o dicionário original
# print(d2)  # Imprime o dicionário copiado

# Exemplo de dicionário
p1 = {
    'nome': 'Hugo',
    'sobrenome': 'Motta'
}

# Tenta imprimir o valor associado à chave 'nome' no dicionário p1
# print(p1['nome'])
# Tenta obter o valor da chave 'nome', se não existir retorna 'Não existe'
# print(p1.get('nome', 'Não existe'))

# Remove a chave 'nome' do dicionário p1 e retorna seu valor
# nome = p1.pop('nome')
# Imprime o valor removido
# print(nome)
# Imprime o dicionário p1 após a remoção da chave 'nome'
# print(p1)
# Remove e retorna o último par chave-valor do dicionário p1
# ultima_chave = p1.popitem()
# Imprime o par chave-valor removido
# print(ultima_chave)
# Imprime o dicionário p1 após a remoção do último par chave-valor
# print(p1)

# Atualiza o dicionário p1 com novos valores para as chaves 'nome' e 'idade'
# p1.update({
#     'nome': 'novo valor',
#     'idade': 32
# })

# Outra forma de atualizar o dicionário p1 com novos valores para as chaves 'nome' e 'idade'
# p1.update(nome='novo valor', idade=32)

# Atualiza o dicionário p1 usando uma tupla de pares chave-valor
tupla = (('nome', 'novo valor'), ('idade', 32))
# Atualiza o dicionário p1 usando uma lista de pares chave-valor
lista = [['nome', 'novo valor'], ['idade', 32]]
p1.update(lista)  # Atualiza o dicionário p1 com os valores da lista
print(p1)  # Imprime o dicionário p1 atualizado