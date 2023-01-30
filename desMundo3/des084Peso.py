print('¨'*6, '\033[35mVERIFICANDO MAIOR E MENOR PESO\033[m', '¨'*6)
cad = list() # 'cad' Cadastros
d = list() # 'd' Dados.
maip = menp = 0
while True:
    d.append(str(input('Digite seu Nome: ')).strip().upper())
    d.append(float(input('Digite seu Peso: ')))
    if len(cad) == 0: # A posição do 'if' é importante para o resultado, logo após os dados.
        maip = menp = d[1]
    else:
        if d[1] > maip:
            maip = d[1]
        if d[1] < menp:
            menp = d[1]
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar\033[32m[S/N]\033[m? ')).strip().upper()[0]
    cad.append(d[:])
    d.clear()
    if op == 'N':
        break
print(f'A lista de cadastro é: \033[33m{cad}\033[m')
print(f'Ao todo foram cadastradas \033[32m{len(cad)}\033[m pessoas.')
print(f'O MAIOR peso foi de \033[31m{maip}\033[m kg. Peso de ', end='')
for p in cad:
    if p[1] == maip:
        print(f'[{p[0]}]')
print(f'O MENOR peso foi de \033[34m{menp}\033[m kg. Peso de ', end='')
for p in cad:
    if p[1] == menp:
        print(f'[{p[0]}]')













