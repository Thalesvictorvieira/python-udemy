# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
class Caneta:
    def __init__(self, cor):
        # private protected
        self._cor = cor
        self._cor_tampa = None #o _ antes do nome quer dizer aos progamadores que n e para mexer nessa

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor 
    
    @cor.setter
    def cor(self,valor):
        print('ESTOU NO SETTER',valor)
        self.cor = valor



canetinha = Caneta('Azul')
canetinha.cor = 'Rosa'
canetinha.cor_tampa = 'Azul'
print(canetinha.cor)
print(canetinha.cor_tampa)