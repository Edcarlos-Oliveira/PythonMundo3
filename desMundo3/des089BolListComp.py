print('¨'*6, '\033[35mBOLETIM LISTAS COMPOSTAS\033[m', '¨'*6)
ln = list()
# Coleta e mostra os dados:
while True:
    n = str(input('Nome: ')).strip().upper()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2)/2 # Cálculo da média.
    ln.append([n, [n1, n2], m])
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar\033[32m[S/N]\033[m? ')).strip().upper()[0]
    if op == 'N':
        break
print('-='*30)
print(f'\033[33m{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}\033[m') # Organizar em tabela.
print('-'*30)
for i, a in enumerate(ln): # 'i' indice, 'a' aluno, 'a[0]' nome, 'a[1]' média.
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}') # Organizar resultado em tabela.
    print(i)
# Para o usuário escolher os dados que quer ver:
while True:
    print('-='*30)
    esc = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if esc == 999: # Para interromper o programa.
        print('\033[31mFINALIZANDO....\033[m')
        break
    if esc <= len(ln) - 1:
        print(f'Notas de \033[36m{ln[esc][0]}\033[m são \033[36m{ln[esc][1]}\033[m') # Mostra a nota e nome do aluno.
print('<<< \033[34mVOLTE SEMPRE\033[m >>>')














