'''
Cuidados com dados mutaveis 
= - copiado valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutavel )
'''
lista_a = ['joao', 'Maria']
lista_b = lista_a.copy()

lista_b[0] = 'teste'
print(lista_b, lista_a)