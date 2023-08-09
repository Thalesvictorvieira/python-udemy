x = 1

def escopo1():
    # global x =20 > vai para todo codigo
    x = 10
    
    def escopo2():
        x = 20
        y = 10
        print(x, y)
        