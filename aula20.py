numero_str = input(
    'digite um numero '
    )

try :
    print('STR:', numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro do de {numero_str} é {numero_float * 2:.02f}')
except:
        print('Isso não é um número ')
