cpf = '746.824.890-70'.replace('.','').replace('-','')#.replace e usado para tirar coisa da str como . -
novedig = cpf[:9]
contadorreg = 10
contadorregressivo11 = 11
memoria1 = 0
memoria2 = 0

for digito in novedig:
    memoria1 += int(digito) * contadorreg
    contadorreg -= 1
primeironumero = ((memoria1 * 10) % 11)
primeironumero = primeironumero if primeironumero <= 9 else 0

# pt2 segundo digito 
dezdig = novedig + str(primeironumero)
for digito1 in dezdig:
    memoria2 += int(digito1) * contadorregressivo11
    contadorregressivo11 -= 1
segundonumero = (memoria2 * 10) % 11
novocpf =f'{novedig}{primeironumero}{segundonumero}'
#Validação do cpf
if cpf == novocpf:
    print(f'{cpf} é Valido')
else:
    print(f'{cpf} invalido')