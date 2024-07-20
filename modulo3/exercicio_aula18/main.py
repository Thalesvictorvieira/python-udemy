class Carro():
    def __init__(self,nome):
        self._carro = nome
        self._motor = None
        self._nome_fabricante = None

    def inserir_motor(self,motor):
        self._motor = motor
        
    def mostrar_motor(self):
        print(f'O carro {self._carro} tem o motor {self._motor.nome_do_motor}')

    def inserir_nome_fabricante(self,fabricante):
        self._nome_fabricante = fabricante
    
    def mostrar_fabricante(self):
        print(f'o carro {self._carro} tem o fabricante {self._nome_fabricante.nome_fabricante}')

########################################################

class Motor():
    def __init__(self,nome_do_motor):
        self._nome_do_motor = nome_do_motor
    
    @property
    def nome_do_motor(self):
        return self._nome_do_motor
    
########################################################
class Fabricante:
    def __init__(self,nome_fabricante):
        self._nome_do_fabricante = nome_fabricante
    
    @property
    def nome_fabricante(self):
        return self._nome_do_fabricante

carro = input('Qual eo nome do carro ?')
carro = Carro(carro) 

motor_fusca = input('Qual eo nome do motor do carro ?')
motor_fusca = Motor(motor_fusca) 

fabricante_fusca = input('Qual eo nome do fabricante do carro ?')
fabricante_fusca = Fabricante(fabricante_fusca)

carro.inserir_motor(motor_fusca)
carro.inserir_nome_fabricante(fabricante_fusca)

carro.mostrar_motor()
carro.mostrar_fabricante()


