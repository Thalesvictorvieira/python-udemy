'''caminho = "C:\\Users\\teste\\Documents\\Programação\\aula150.txt" '''
import os

caminho = os.path.join('\\Users', 'teste', 'Desktop', )

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)