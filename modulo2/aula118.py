# Manipulando chaves e valores em dicionarios 
pessoa = {}

chave = 'nome'

pessoa[chave] = 'Teste'
pessoa['sobrenome'] = 'teste'
print(pessoa[chave])

pessoa[chave] = 'joaquim'
print(pessoa)


del pessoa['sobrenome']
print(pessoa,'11')
