'''

listas em python 
tipo list - Mutavel
suporta vários valores de qualquer tipo
conhecimentos reutilizavis - indicies e fatiamento
metedos uteis : append, insert,pop,del,clear,extend
 01234  
   -54321
string = 'ABCDE' # 5 Caracteres (len)
 lista = [10,20,30,40]
 lista.append(50) vai adicionar o valor 50 na lista
append - Adicipna um item ao final 
insert - Adicioan um iten no índice escolhido 
pop - Remove do final ou do indicie escolhido 
del - apagaga um indicie
clear - apaga a lista 
extend - estende a lista 
- + concatena listas 
create Read Update Delete 
criar, ler, alternar, apagar = lista[i](CRUD)
''' 
#        0  1  2  3
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_d)