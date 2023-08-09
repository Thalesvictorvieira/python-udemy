#Escopo 1<2<3
#Escopo1

def escopo2():
    x = 1
    funcao1 = 2
    print('o escopo2 consegue ler a funçao 1 mas nao a funcao2')
    def escopo3():
        funcao2 = 3
        print('o escopo 3 consegue ler de todo mundo ')
        global funcao3     
        funcao3 = 4
escopo2()
