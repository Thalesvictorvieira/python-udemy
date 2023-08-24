dicionario = {
    'nome':'joao',
    'rua': 'seila'
}

d2 = dicionario # o valor d2 vai direcionar para o dicionario ele nao vai copiar 

d2 = copy.deepcopy(dicionario) # ele vai copiar o dicionario 


