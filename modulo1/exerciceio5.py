'''
numero = input('Digite um numero inteiro para eu descobrir se ele e impar ou par ')
try:
    numero_checado_que_e_inteiro = int(numero)
    numero_par = numero_checado_que_e_inteiro % 2 == 0
    numero_par_texto = 'ímpar'

    if numero_par:
        numero_par_texto = 'par'
    print(f'O número {numero} é {numero_par_texto}')
except:
    print('Você não digitou um número inteiro ')
'''
"""
hora = int(input('Digite que horas são para que eu possa saudalo '))
if hora >= 0 and hora <= 11:
    print('bom dia ')

if hora >= 12 and hora <= 17:
    print('boa tarde')
if hora >=18 and hora<= 23:
    print('Boa noite')
Exception()
    print('valor invalido ')
    """

nome = input('Digite seu nome ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if tamanho_nome <= 4 :
        print('seu nome e curto')
    elif tamanho_nome <=5 and tamanho_nome <=6:
        print('Seu nome e normal')
    elif tamanho_nome >= 6 :
     print('seu nome e grande')
else:
    print('digite um nome com mais de 1 letra') 
