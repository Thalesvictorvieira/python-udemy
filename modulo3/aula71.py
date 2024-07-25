from collections import namedtuple

Carta = namedtuple('Carta',['valor','naipe'],
                   defaults=['VALOR','NAIPE'])
as_espada = Carta('A', '♠')
print(as_espada.naipe)
print(as_espada.valor)