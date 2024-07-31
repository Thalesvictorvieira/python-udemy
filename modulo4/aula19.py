# csv.render e csv.Dictreader
# csv.reader lê o CSV em formato de lista
# csv.Dicreader lê o CSV em formato de dicionario
import csv
from pathlib import Path

caminho_csv = Path(__file__).parent / 'aula19.csv'
with open(caminho_csv,'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha[0])
        