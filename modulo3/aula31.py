# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
from abc import ABC,abstractmethod

class Notificao(ABC):
    def __init__(self,mensagen) -> None:
        self.mensagen = mensagen
    
    @abstractmethod
    def enviar(self) -> bool:...



class NotificaoEmail(Notificao):
   
    def enviar(self) :
        print('E-mail: enviado',self.mensagen)
        return True

class NotificaoSMS(Notificao):
    
    def enviar(self) -> bool :
        print('SMS: enviado',self.mensagen)
        return False


def notificar(notificacao: Notificao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('enviada')
    else:
        print('nao enviada')

notificar(NotificaoEmail('ola'))