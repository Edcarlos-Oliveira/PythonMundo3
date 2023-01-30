print('¨'*6, '\033[35mLISTA PARES E IMPARES\033[m', '¨'*6)
lpi = [[],[]] # Importante os colchetes para separar as listas.
v = 0
for c in range(1,8):
    v = int(input(f'Digite o {c}º valor: '))
    if v % 2 == 0:
        lpi[0].append(v) # 'lpi 0' Coloca os pares no primeiro colchete.
    else:
        lpi[1].append(v) # 'lpi 1' Coloca os impares no segundo colchete
lpi[0].sort() # Organiza só os pares.
lpi[1].sort() # Organiza só os impares.
print(f'A lista de números é: \033[32m{lpi}\033[m')
print(f'Os valores pares digitados foram: \033[36m{lpi[0]}\033[m.')
print(f'Os valores ímpares digitados foram: \033[31m{lpi[1]}\033[m.')






