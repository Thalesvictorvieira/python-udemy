#Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6 7 8 9
# T H A L E S
# -6-5-4-3-2-1
nome = 'Thales'
#print(nome[2])
#print(nome[-4])
#print('á' in nome)
#print('T' in nome)
#print ('T' not in nome)
nome = input('Digite seu nome:')
encontrar = input('Digite o que deseja encontrar:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')