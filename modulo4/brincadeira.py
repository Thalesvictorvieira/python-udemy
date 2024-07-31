from random import randint

numero_aleatorio = randint(1,10)
tentetiva_usuario = int(input('Tente adivinhar um numero entre 1 a 10:'))
sair_do_jogo = ''

while sair_do_jogo != False:
    if tentetiva_usuario != numero_aleatorio:
        print('noob voce errou')
        print(f'O numero era {numero_aleatorio}')
    else:
        print('PARABENS VOCÊ ACERTOU')
    sair_do_jogo = input('Você deseja sair do jogo s/n')
    if sair_do_jogo in 'Ss':
        sair_do_jogo = True
    else:
        sair_do_jogo = False
        #isso está mal feito propositalmente isso e uma PIADA ok ?