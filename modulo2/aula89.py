# dir, hasattr e getattr em Python
string = 'Nome'
metedo = 'upper'

if hasattr(string, metedo):
    print('Existe upper')
    print(getattr(string,metedo)())
else:
    print('Não existe o métedo',metedo)

