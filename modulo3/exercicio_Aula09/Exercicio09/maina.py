# Exercício - Salve sua classe em JSon
# Salve os dados da sua classe em JSon
# e depois crie novamente as instancias
# da classe com os dados salvos
# FAÇA EM AQUIVOS SEPARADOS UM ARQUIVO .PY COM AS CLASSES UM ARQUIVO JSON COM OS DADOS
# E OUTRO QUE VAI RECEBER OS DADOS SALVOS NO JSON
import json
LocalDoArquivo = 'C:\\Users\\teste\\Documents\\Programação\\Python\\Udemy\\python-udemy\\modulo3\\exercicio_Aula09\\Exercicio09\\Exercicio.json'

class Pessoa:
    def __init__(self,nome,idade,genero,cor):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.cor = cor
        
pessoa1 = Pessoa('Thales',18,'Masculino','Branco')
pessoa2 = Pessoa('Asael',19,'Masculino','Branco')

listaDeArquivo = [vars(pessoa1),vars(pessoa2)]

with open('Exercicio.json','w+',encoding='utf8') as arquivo:
  json.dump(listaDeArquivo,arquivo,ensure_ascii=False,indent=2)
