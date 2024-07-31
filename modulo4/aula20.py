import csv
from pathlib import Path

caminho_csv = Path(__file__).parent / 'aula20.csv'

lista_clientes = [
    {'Nome': 'teste', 'Endereco': 'rua jararaca'},
    {'Nome': 'zezin', 'Endereco': 'canada'},
    {'Nome': 'Maria ', 'Endereco': 'chicaco'},
]

# with open(caminho_csv,'w') as arquivo:
#     colunas = lista_clientes[0].keys()
#     escritor = csv.writer(arquivo)
#     escritor.writerow(colunas)
#     for cliente in lista_clientes:
        
#         escritor.writerow(cliente)

with open(caminho_csv,'w') as arquivo:
    Nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(arquivo,fieldnames=Nome_colunas); escritor.writeheader()
    escritor.writeheader()
    for clientes in lista_clientes:
        escritor.writerow(clientes)
   