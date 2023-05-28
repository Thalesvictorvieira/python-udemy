lista = []
while True:
    valor = input('Digite a opçao que vc quer\n[i]inserir [a]apagar [l]listar : ')
    if valor == 'i':
        ivalor = input('Você escolheu a opçao inserir \n Digite o valor que você quer inserir: ' )
        lista.append(ivalor)
        print(f'você adicionou {ivalor} na lista')
    elif valor == 'a':
        print('Você escolheu apagar ')
        avalor = input('Digite o indicie que Você quer apagar ')
        print(lista)
        
        try:
            indicie = int(valor)
            del lista[indicie] 
        except ValueError:
           print('Você so pode digitar numero inteiro ')