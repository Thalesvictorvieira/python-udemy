import json

from maina import Pessoa
PastaDoarquivo = 'C:\\Users\\teste\\Documents\\Programação\\Python\\Udemy\\python-udemy\\Exercicio.json'

with open(PastaDoarquivo,'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    print(p1.nome)