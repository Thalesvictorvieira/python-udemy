import json
import os

nome_arquivo ='aula17.json'
caminho_absoluto = os.path.abspath(os.path.join(os.path.dirname(__file__),nome_arquivo))

arquivo_json ={
    "Nome":"teste",
    "idade":"18",
    "nacionalidade":"Brasileiro/a"
}

with open(caminho_absoluto,'w') as arquivo:
    json.dump(arquivo_json,arquivo, ensure_ascii=False, indent=2)

with open(caminho_absoluto,'r') as arquivo:
    dados_do_json = json.load(arquivo)

