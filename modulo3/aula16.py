# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
# O objeto precisa um pouquinho de outro objeto para realiza determinada coisa mas eles pode viver separadamente
# O carro pode viver sem a roda, ea roda pode viver sem o carro. Mas o carro nao funciona bem sem a roda e roda não funciona muito bem sem o carro. -Professor Luiz Otávio 2022
class Carrinho:
    def __init__(self):
        self._produtos = []


    def total(self):
        return sum([p.preço for p in self._produtos])
    
    def inserir_produtos(self,*produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def Listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preço)

class Produto:
    def __init__(self,nome,preço):
        self.nome = nome #camisa
        self.preço = preço #20

carrinho = Carrinho()
p1 =Produto('camisa',20)
p2 = Produto('Caneta',1.20)

carrinho.inserir_produtos(p1,p2)
carrinho.Listar_produtos()
print(carrinho.total())
