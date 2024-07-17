# Atributos de Classe
from datetime import datetime
AnoAtual = datetime.today().year




class Pessoa:
    atributo = 'valor'
    ano_atual = AnoAtual

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        

    def PegarAnoNascimento(self):
        return self.ano_atual - self.idade
    
pessoa1 = Pessoa('Thales',18)
print(pessoa1.PegarAnoNascimento())