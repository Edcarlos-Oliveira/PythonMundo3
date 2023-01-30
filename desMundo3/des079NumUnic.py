print('¨'*6, '\033[35mNÚMERO ÚNICO EM LISTA\033[m', '¨'*6)
num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('\033[36mNúmero adcionado com sucesso.\033[m')
    else:
        print('\033[31mEste número já foi adcionado.\033[m')
    op = ' '
    while op not in 'SN': # Para repetir enquanto o usuário não digitar S ou N.
        op = str(input('Quer continuar\033[32m[S/N]\033[m? ')).strip().upper()[0]
    if op == 'N':
        break
num.sort() # para colocar em ordem.
print(f'Os números adicionados foram: \033[33m{num}\033[m')



