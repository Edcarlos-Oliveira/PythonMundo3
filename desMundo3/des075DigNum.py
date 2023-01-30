print('¨' * 6, '\033[35mDIGITANDO NÚMEROS\033[m', '¨' * 6)
n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))

print(f'Você digitou os valores: \033[32m{n}\033[m')
print(f'O número \033[35m9\033[m apareceu: \033[35m{n.count(9)}\033[m vez(s).')
if 3 in n:
    print(f'O número \033[34m3\033[m apareceu na: \033[34m{n.index(3) + 1}ª\033[m posição.')
else:
    print('O valor \033[34m3\033[m não foi digitado em nenhuma posição.')
print('Os números pares digitados foram: ', end='')
for p in n:
    if p % 2 == 0:
        print(f' \033[36m{p}\033[m ', end='')









