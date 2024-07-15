class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Thales','victor')
print(p1.nome) #retorna o valor Thales