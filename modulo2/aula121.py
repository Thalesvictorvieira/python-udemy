p1 = {
    'nome' : 'joaquim',
    'sobrenome': 'seila'
}

p1.get('nome', 'Não tem') # ele tenta buscar o valor nome na chave p1, se ele não encontrar ele retorna 'Não tem'

#p1.popitem() ele remove a ultima chave presente no dicionario
'''
p1.update({
    'nome': 'coisa nova'# ele atualiza o valor do tem escolhido 
})

p1.update(nome = 'novo valor', idade = 30 ) # ele também pode ser escrito dessa maneira

tupla = ('nome', 'novo valor'),
p1.update(tupla)
'''