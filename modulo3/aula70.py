from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int
    enderecos: list[str]

p1 = Pessoa('teste','silva',50)
print(p1)