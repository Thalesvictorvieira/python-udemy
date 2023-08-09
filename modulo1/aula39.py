# Tuplas SAo imutaveis .
#Tuplas sao listas sem o [] e ela nao pode mudar as variaveis 
nomes = 'teste1', 'teste2', 'teste3'
#nomes = tuple(nomes) Conversão de lista para tupla
# nomes = list(nomes)conversão de Tuplas para listas 
nomes[1] = 'outro'
print(nomes)