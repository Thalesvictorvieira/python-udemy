# calculadora com wilhe



while True:
    numero_1 = float(input('Digite o primeiro numero'))
    numero_2 = float(input('Digite o outro numero'))
    operador = input('Queal eo operador (/,**,*,-,+)')
    if operador == '/':
        resultado_divisão = numero_1 / numero_2
        print(resultado_divisão)
    if operador == '**':
        resultado_da_potenciação = numero_1 ** numero_2
        print(resultado_da_potenciação)
    if operador == '*':
        resultado_da_multiplicação = numero_1 * numero_2
        print(resultado_da_multiplicação)
    if operador == '-':
        resultado_da_subtração = numero_1 - numero_2
        print(resultado_da_subtração)
    if operador == '+':
        resultado_da_adiçao = numero_1 + numero_2
        print(resultado_da_adiçao)
    