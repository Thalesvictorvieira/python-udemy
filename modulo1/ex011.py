lista = []
while True:
    valor = input('Digite a opçao que vc quer\n[i]inserir [a]apagar [l]listar : ')
    if valor == 'i':
        ivalor = input('Você escolheu a opçao inserir'
                       ' Digite o valor que você quer inserir: ' )
        lista.append(ivalor)
        print(f'você adicionou ({ivalor}) na lista')
    elif valor == 'a':
        print('Você escolheu apagar ')
        avalor = input('Digite o indicie que Você quer apagar:')
        print(lista)
        try:
            indicie = int(avalor)
            del lista[indicie] 
        except ValueError:
           print('Você so pode digitar numero inteiro ')
        except IndexError:
            print('esse indicie nao existe')
        except Exception:
            print('Erro desconhecido ')
        
    elif valor == 'l':
        print('Você escolheu a opçao ler lista')
        
        if len(lista) == 0:
         print('Não tem nada para eu listar.')
        for i, valor in enumerate(lista):
            print(i,valor)
    else:
        print('Digite a opçpes [i] ou [a] ou [l] '
              '')