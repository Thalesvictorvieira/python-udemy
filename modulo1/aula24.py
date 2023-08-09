'''
repetições 
while (enquanto)
executa um ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código Não tem fim 
'''
condicao = True
while condicao :
    nome = input('Qual e seu nome:')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair' and nome == 'Sair':
        break
   