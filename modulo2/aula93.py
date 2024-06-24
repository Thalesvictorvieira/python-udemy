# Try, except, else e finally
string = 'Thales'
print(isinstance(string,str))
try:
    a = 10
    #b = 0 
    print('Linha 1')
    c = a / b
    print('Linha 2 ')

except ZeroDivisionError:
    print('Dividiu por zero')

except NameError:
    print('Nome b não está definido')

except (TypeError,IndexError) as error:
    print('TypeErro + IndexError')
    print('msg',error)
    print('msg',error.__class__.__name__)

except Exception:
    print('Erro Desconhecido.')

print('Continuar')
