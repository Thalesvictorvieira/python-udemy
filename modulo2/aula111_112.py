# args - Argumentos não nomeados 
# Empacotamento de coisas 

def teste(*teste):
    total = 0 
    for numero in teste:
        print('Total', total,numero)
        total = total + numero
        print('Total ' , total)
        
teste(1,2,3,4,5,6)



