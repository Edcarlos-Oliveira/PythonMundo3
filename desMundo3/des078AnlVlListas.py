print('¨'*6, '\033[35mANALISANDO VALORES LISTAS\033[m', '¨'*6)
l = list()
mai = 0
men = 0
for c in range(0,5):
    l.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0: # Primeiro valor lido.
        mai = men = l[c] # Lista na posição 'c'
    else:
        if l[c] > mai: # Para achar o maior valor
            mai = l[c]
        if l[c] < men: # Para achar o menor valor
            men = l[c]
print(f'A lista digitada foi: \033[32m{l}\033[m', end='')
print(f'\nO maior valor digitado foi \033[36m{mai}\033[m nas posições: ', end='')
for p, v in enumerate(l): # 'p' Posição.
    if v == mai:
        print(f'\033[33m{p}...\033[m', end='')
print()
print(f'O menor valor digitado foi: \033[31m{men}\033[m nas posições: ', end='')
for p, v in enumerate(l):
    if v == men:
        print(f'\033[33m{p}...\033[m', end='')
print()






























