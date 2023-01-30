print('¨' * 6, '\033[35mLISTA DE PREÇOS\033[m', '¨' * 6)
print('-'*32)
print(' '*6, '\033[33mLISTAGEM DE PREÇOS\033[m')
print('-'*32)
lp = ('Lápis.................R$   1.75''\n') + ('Borracha..............R$   2.00''\n') + ('Caderno...............R$  15.90''\n') + ('Estojo................R$  25.00''\n') + ('Transferidor..........R$   4.20''\n') + ('Compasso..............R$   9.99''\n') + ('Mochila...............R$ 120.00''\n') + ('Canetas...............R$  22.30''\n') + ('Livro.................R$  34.90')
print(lp)
# Poderia ser reescrito dessa forma:
'''print('-' * 40)
print(f'{"Listagem de Preços" :^40}')
print('-' * 40)
lp = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
      'Compasso', 9.99, 'Mochila', 120.00, 'Canetas', 22.30, 'Livro', 34.9)
for pos in range(0, len(lp)):
    if pos % 2 == 0:
        print(f'{lp[pos]:.<30}', end='')
    else:
        print(f'R${lp[pos]:>7.2f}')
print('-' * 40)'''
