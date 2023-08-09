'''
repetiçoes 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira 
loop infinito -> Quando um códifo Não tem fim 
'''
contador = 0 

while contador <= 100:
    contador += 1
    
    if contador == 6:
     print(f'Não vou mostrar o {contador}')
     continue


    if contador >= 10 and contador <= 27 :
        print('Não vou mostrar', contador)
        continue
    print(contador)

