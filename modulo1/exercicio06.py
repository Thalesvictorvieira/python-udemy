nome = 'Thales'
indicie = 0
novo_nome = ''
while indicie < len(nome):
    letra = nome[indicie]
    novo_nome += f'*{letra}'
    indicie += 1

novo_nome +='*'
print(novo_nome)
# isso e uma acomulação