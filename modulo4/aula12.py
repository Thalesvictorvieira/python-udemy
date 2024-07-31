# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretórios de 
# maneitas recursiva.
#Ela gera uma sequencia de tuplas, onde cada tupla possui tres elementos
# o diretotio atual (root), uma lista de subdiretórios (dirs)
#e umalista dos arquivos do diretórios atual (file).

import os
from itertools import count

caminho_destino = os.path.join('c:\\','Users','teste','Documents','Programação')
contador = count()

for root, dirs, files in os.walk(caminho_destino):
  the_couter = next(contador)
  print(the_couter, 'pasta atual ',root)