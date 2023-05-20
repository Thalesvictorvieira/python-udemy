#laço de repetição for 
texto = 'python'

#i = 0 
#tamanho_string = len(texto)

#while i < tamanho_string:
#    print(texto[i], 1)
#    i += 1
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*' )