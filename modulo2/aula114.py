def criar(saudacao,nome):
    def saudar():
        return f'{saudacao},{nome}!'
    return saudar()


s1 = criar('bom dia', 'luiz')
s2 = criar('Boa noite','Luiz')
print(s1)
print(s2)