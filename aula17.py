""" 
interpolação e básica de strings 
S - string 
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""
nome = 'Thales'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f ' % (nome,preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500,1500)) 