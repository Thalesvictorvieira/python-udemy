#Dicionario
pessoa ={
    'nome':'Thales Victor',
    'Sobrenome':'Vieira',
    'endereço':[
        {'rua':'nome da rua','numero':123},
        {'trabalho':' loja','numero':456},
    ],
}

#print(pessoa['nome'])

for chave in pessoa:
    print(chave,pessoa)