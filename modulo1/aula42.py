# Split e join com list e str 
# split - divivde uma str 
# join 0 une uma string 
Frase = ' frase com espaços '
Frase_sem_espaços = Frase.split(';')# se vc colocar ';' Ele cai colocar ; entre os espaços

for i, frase in enumerate(Frase_sem_espaços):
    print(Frase_sem_espaços[i].strip())

print(Frase_sem_espaços)