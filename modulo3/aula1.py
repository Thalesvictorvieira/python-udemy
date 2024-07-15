# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instancias) que podem ter sus próprios atributos e métedos
# Os objetos gerados pela classes podem usar seus dados internos para realizar varias ações
#por convenção, usamos Pascalcase para nomes de classes.

'''string = 'nome' #Classe str
print(string.upper())''' # Ela e uma instancia da classe str por isso ele pode ser alterada pela função upper()

class Pessoa: # assim voce declara a classe Pessoa sendo o nome da classe
    ... 

p1 = Pessoa()
p1.nome ='Nome'
p1.sobrenome ='Sobrenome'
print(p1.nome,p1.sobrenome)