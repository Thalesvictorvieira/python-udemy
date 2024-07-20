# @staticmethod (métedos estaticos ) são inuteis em python 
# metedos estaticos são metedos que estão dentro da Classe
# em resumo, são funções que existem dentro da sua Classe

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args,**kwargs): # ele n tem acesso ao self 
        print('dentro',args,kwargs)
        

def funcao_que_esta_fora_na_classe(*args): # fora da classe ele ia fazer a mesma coisa
        print('fora')

c1 = Classe()
c1.funcao_que_esta_na_classe(1,2,3)
funcao_que_esta_fora_na_classe()
