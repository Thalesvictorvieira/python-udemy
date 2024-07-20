# métodos de classes
# São métodos onde 'self' sera 'cls', ou seja,
# ao invés de receber a instancia no primeiro 
# parâmetro, receberemos a propiá classe.
class Pessoa:
    ano = 2023 # atributo de classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def chama_no_print(cls):
        print('Chamei')
    
    @classmethod
    def criar_com_50_anos(cls,nome):
        return cls(nome,50)
    
    @classmethod
    def criar_sem_nome(cls,idade):
        return cls('Anonimo',idade)
    

p1 = Pessoa('Thales',18)
p2 = Pessoa.criar_com_50_anos('Asael')
p3 = Pessoa.criar_sem_nome(18)
print(p3.nome)
print(p3.idade)