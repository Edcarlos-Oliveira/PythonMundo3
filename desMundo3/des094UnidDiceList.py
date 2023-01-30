print('¬'*6, '\033[33mANÁLISE DE DADOS PESSOAS\033[m', '¬'*6)
cad = dict()
ld = list()
m = s = 0 # Soma e média.
# Leitura dos dados:
while True:
    cad.clear()
    cad['n'] = str(input('Nome: ')).strip().upper()
    while True:
        cad['s'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if cad['s'] in 'MF':
            break
        print('\033[31mERRO!, Por favor, digite apenas M ou F.\033[m')
    cad['idade'] = int(input('Idade: '))
    s += cad['idade']
    ld.append(cad.copy())
    while True:
        op = str(input('Quer continuar [S/N]')).strip().upper()[0]
        if op in 'SN':
            break
        print('\033[31mERRO!, Por favor, digite apenas S ou N.\033[m')
    if op == 'N':
        break
print('-='*30)
# Análise dos dados:
print(f'A) Ao todo temos \033[36m{len(ld)}\033[m pessoas cadastradas.')
m = s / len(ld)
print(f'B) A média de idade é de \033[36m{m:0.0f}\033[m anos.')
print('C) As mulheres cadastradas são: ', end='')
for p in ld:
    if p['s'] == 'F':
        print(f'\033[36m{p["n"]}\033[m', end='  ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in ld:
    if p['idade'] >= m:
        print(' ', end='')
        for k, v in p.items():
            print(f'\033[33m{k} = {v}\033[m; ', end='')
        print()
print('\033[31m<<<ANÁLISES CONCLUÍDA>>>\033[m')















