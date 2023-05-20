'''
Interável -> str,range,etc
Interador -> quem sabe entregar um valor por vez 
next -> me entregue o proximo valor 
inter -> me entregue seu interador 
'''
texto = iter('Teste') # iterável
interador = inter(texto) # iterador

while True:
    try:
        letra = next(interador)
        print(letra)
        except StopIteration:
            break
# ^ 
# |
#= for letra in texto :
    print(letra)