# Closeure e funcoes que retornan outras funcoes 

def criar_comprimentacao(comprimentos):
    def comprimentar(nome):
        return f'{comprimentos},{nome}'
    return comprimentar

falar_bom_dia = criar_comprimentacao('Bom dia ')
falar_boa_noite = criar_comprimentacao('Boa noite')

for nome in ['Maria','Asael','Thales']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))