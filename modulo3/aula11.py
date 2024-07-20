# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self,host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self,user):
        self.user = user
    
    def set_password(self,password):
        self.password = password

    @classmethod #tem que usar cls n o self
    def create_with_auth(cls,user,password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def soma(x,y):
        return x + y
        # se fizer isso fora da classe da exatamente o mesmo resultado 

usuario1 = Connection.create_with_auth('teste',123)
print(usuario1.user)