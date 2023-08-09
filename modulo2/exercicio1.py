# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.



def multiplicacao(*teste):
    global memoria
    memoria = 1
    for numero in teste:
        memoria *= numero
       
        print(memoria)   

multiplicacao(1,2)

def par_impar(variavel):
    resultado = variavel % 2 
    if resultado == 0:
        print(f'o valor ({variavel}) e par')
    else:
        print(f'O valor ({variavel}) e impar ')

par_impar(memoria)
par_impar(17)