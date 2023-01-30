print('¨'*6, '\033[35mEXTRAINDO DADOS LISTA\033[m', '¨'*6)
l = list()
while True:
    l.append(int(input('Digite um número: ')))
    op = ' ' # essencial o espaço entre as aspas.
    while op not in 'SN':
        op = str(input('Quer continuar\033[32m[S/N]\033[m? ')).strip().upper()[0]
    if op == 'N':
        break
if 5 in l:
    print('\033[34mO valor 5 faz parte da lista.\033[m')
else:
    print('\033[31mO valor 5 não foi encontrado na lista.\033[m')
print(f'Os números digitados foram: \033[32m{l}\033[m')
l.sort(reverse=True)
print(f'Foram digitados \033[36m{len(l)}\033[m números.')
print(f'Os valores em ordem decrescente são: \033[31m{l}\033[m')



















