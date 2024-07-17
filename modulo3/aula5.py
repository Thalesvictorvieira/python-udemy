# Escopo da classe e de metedos da classe 
class Animal:
    # nome = 'Leão'

    def __init__(self,nome):
        self.nome = nome
        
        variavel = 'valor'
        print(variavel)
    
    def comendo(self, alimento):
            return f'{self.nome} está comendo {alimento} '

leao = Animal(nome='leao')
print(leao.nome)

print(leao.comendo('maçã'))