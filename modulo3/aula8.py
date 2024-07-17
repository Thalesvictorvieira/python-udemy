# __dict__ e vars para atributos de instâncias
class Pessoas:
    ano_atual = 2024

    def __init__(self, nome, Idade):
        self.nome = nome
        self.idade = Idade
    
    def Get_Ano_nascimento(self):
        return Pessoas.ano_atual - self.idade
    

pessoa1 = Pessoas('Jose',35)
pessoa1.nome = 'EITa '
print(pessoa1.nome)
print(pessoa1.__dict__)
print(vars(pessoa1))
pessoa1.__dict__['outra'] = 'coisa'
print(pessoa1.outra)