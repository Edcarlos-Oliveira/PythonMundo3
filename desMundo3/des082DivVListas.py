print('¨'*6, '\033[35mDIVIDINDO VALORES EM LISTA\033[m', '¨'*6)
l = list() # 'pa' PARES, 'im' ÍMPARES.
pa = list() # par
im = list() # Impar
while True:
    l.append(int(input('Digite um número: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar\033[32m[S/N]\033[m? ')).strip().upper()[0]
    if op == 'N':
        break
for i, v in enumerate(l): # 'i' índices, 'v' valores.
    if v % 2 == 0:
        pa.append(v) # Adiciona os números na lista dos pares.
    elif v % 2 == 1: # Adciona os números na lista dos ímpares.
        im.append(v)
print(f'A lista completa é: \033[32m{l}\033[m')
print(f'A lista de pares é: \033[36m{pa}\033[m')
print(f'A lista de ímpares é: \033[31m{im}\033[m')















