estoque = []
print('Bem vindo ao sistema de armazenamento')
while True:
    opção = input('Você pode\n[A]adicionar item no estoque\n[D]Deletar items do estoque\n[V]Ver itens no estoque ')
    op =opção.upper()
    if op == 'A':
        iten_a = input('O que Você quer adicionar no estoque ? ')
        estoque.append(iten_a)
        print(f'Você adicopnou ({iten_a}) no estoque ')
    elif op == 'D':
        iten_deleter = input(f'Oque você oque vc quer deletar do estoque?\n {estoque} no estoque ')
        try:
            item_inteiro = int(iten_deleter)
            del estoque[item_inteiro]
        except :
            print('Ocorreu algum erro ')
    elif op == 'V':
        print(estoque)
    else:
        print('Voce so pode escolher [A] [D] [V]')