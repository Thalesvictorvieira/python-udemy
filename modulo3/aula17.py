# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self,nome) :
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self,rua,numero):
        self.enderecos.append(Endrecos(rua,numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
         print('Apagando', self.nome)

class Endrecos:
    def __init__(self,rua, numero):
        self.rua = rua
        self.numero = numero
    def __del__(self):
        print('Apagando', self.rua, self.numero)

cliente1 = Cliente('Joao')
cliente1.inserir_enderecos('AVENIda',54)
cliente1.inserir_enderecos('Rua sao jorge',6745)



cliente1.listar_enderecos()
print('-'*20)
