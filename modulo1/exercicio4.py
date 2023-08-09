nome = input('Digite seu nome ')
idade = input('Digite a sua idade ')

if nome and idade :
    print(f'Seu nome e {nome}')
    print(f'seu nome invertido e {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu possui espaço ')
    else :
      print('Seu nome não comtém espaço ')
    
    print(f'Seu nome possui {len(nome)} letras') #len e usado para contar coisas das str
    print(f'A primeira letra do seu nome é {nome[0]} ')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Você deixou epaços em branco ')