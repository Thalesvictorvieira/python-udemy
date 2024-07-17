# Mantendo estados dentro da classe
class Camera:
    def __init__(self,nome,filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):
        if self.filmando == True:
            print(f'{self.nome} Já está filmando!')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = True


    def Fotografar(self):
        if self.filmando == True:
            print(f'{self.nome} Não pode fotografar filmando')
            return
        print(f'{self.nome} está tirando foto...')
        
    def PararFilmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando... ')
            return
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False
            



Camera1 = Camera('Canon')
Camera2 = Camera('sony')
Camera1.filmar()
Camera1.filmar()
Camera1.Fotografar()
#print(c1.filmando)
#print(c2.filmando)