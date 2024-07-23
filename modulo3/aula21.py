# Super() é a super classe na sub classe
# Classes principal (pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
'''class Minhastring(str):
    def upper(self):
        print('Chamou upper')
        retorno = super().upper()
        print('depois do uper')
        return retorno
    
string = Minhastring('teste')
print(string.upper())'''
class A:
    atributo_a = 'AAAAAAAAAAAAAAA'
    def metodo(self):
        print('a')

class b(A):
    atributo_b ='BBBBBBBBBBBBBBBBB'
    def metodo(self):
        
        print('b')

class c(b):
    atributo_c = 'CCCCCCCCCCCCCCCC'
    def metodo(self):
        super(c,self).metodo()
        print('c')