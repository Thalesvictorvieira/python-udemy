''' higher oirder funcions 
Funçoes de primeira classe
'''

msg = 'oi'

def saudacao(msg):
    return msg

def executa(funcao,msg):
    return funcao(msg)


v = executa(saudacao,'bom dia')
print(v)

# funcoes pode receber valor de outras funções 