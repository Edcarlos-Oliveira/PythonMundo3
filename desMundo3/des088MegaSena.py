print('¨'*6, '\033[35mSORTEANDO NÚMEROS\033[m', '¨'*6)
print('-'*30)
print(' '*5,'\033[32mJOGA NA MEGA SENA\033[m')
print('-'*30)
from random import randint
from time import sleep
lp = list() # Lista de palpites.
p = list() # Palpites
qtd = int(input('Quantos jogos você quer sortear? ')) # 'qtd' quantidade de jogos.
t = 1 # Total
while t <= qtd:
    c = 0 # Contador
    while True:
        n = randint(1,60) # Sorteia os números de 1 até 60
        if n not in lp:
            lp.append(n)
            c += 1
        if c >= 6: # Bloqueia quando 6 números forem sorteados.
            break
    lp.sort()
    p.append(lp[:])
    lp.clear()
    t += 1 # Evita o looping infinito.
print('-='*3, f'\033[32mSORTEANDO\033[m {qtd} \033[32mJOGOS\033[m', '-='*3)
for i, l in enumerate(p):
    print(f'Jogo {i+1}: {l}') # 'i+1' Pega o indice apartir do 1
    sleep(1)
print('-='*5, '\033[36mBOA SORTE!\033[m', '-='*5)










