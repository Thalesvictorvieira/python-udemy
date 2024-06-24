# Módulos padrão do python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# Inteiro - import nome_modulo
# Vantagens: nomes grandes 

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o nomespace do módulo

# alias 1 - import nome_modulo as apelidos 
# alias 2 - from nome_modulo import objetos as apelido
# Vantagens: Você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: import tudo de um módulo
# Desvantagens: importa tudo em módulo
import sys as asinc #as renomeia o nome do mudulo de sys foi para asinc
print(sys.platform)
print(asinc.platform)