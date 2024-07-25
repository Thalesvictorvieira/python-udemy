import abc

class Conta(abc.ABC):
    def __init__(self,agencia: int, Conta: int, saldo: float = 0 ):
        self.agencia = agencia       
        self.Conta = Conta
        self.saldo = saldo
    @abc.abstractmethod
    def sacar(self,valor: float) -> float:...

    def depositar(self,valor : float) -> None:
        self.saldo += valor
        self.detalhes(f'(Depositos {valor})')

    def detalhes(self,msg: str ='') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
    
    def __repr__(self) -> str:
         class_name = type(self).__name__
         attrs = f'{self.agencia!r},{self.Conta!r}, {self.saldo!r}'
         return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'saque {valor}')
            return self.saldo    
        print('Nao foi possivel sacar o valor desejado')
        self.detalhes(f'Saque negado ({valor})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, Conta: int, saldo:float=0,limite:float=0):
        super().__init__(agencia, Conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'saque {valor}')
            return self.saldo    
        print('Nao foi possivel sacar o valor desejado')
        self.detalhes(f'Saque negado ({valor})')
        return self.saldo
    def __repr__(self) -> str:
         class_name = type(self).__name__
         attrs = f'{self.agencia!r},{self.Conta!r}, {self.saldo!r},{self.limite!r}'
         return f'{class_name}{attrs}'



if __name__ == '__main__':
    '''cp1 = Conta poupança 1 '''
    cp1 = ContaPoupanca(111,222,0)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
    print('##')

    cc1 = ContaCorrente(111,222,0,100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(5.5)


