pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Hugo'
pessoa['sobrenome'] = 'Motta'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('NÂO EXISTE')
else:
    print(pessoa['sobrenome'])
