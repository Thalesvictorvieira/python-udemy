""" 
Formatação de básica de strings 
s = string 
f = float
d = int
.<número de dígitos> f
x ou X = hexadecimal
(caractere)(><^)(quantidade )
> = esquerda
< = Direita
^ = Centro
Sinal - + ou -
Ex.: 0>-100,.1f
conversion flags = !r, !s, !a
"""
variavel = 'ABC'
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:$^10}')
print(f'{100:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')