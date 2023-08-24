def criar_multiplicador(multiplicador):# aqui recebeu o valor 4
    def multiplicar(numero):# aqui recebeu o valor 2 // aqui ele criou a função que multiplica o numero 4 pelo 2 
        return numero * multiplicador# aqui ele multiplicou 2 por 4
    return multiplicar


duplicar = criar_multiplicador(4)# esse valor foi para multiplicador
print(duplicar(2))
# dessa forma o valor pode ser variado tipo pode ser duplicar ou triplicar so tem que colocar o 3 ao enves do 2 