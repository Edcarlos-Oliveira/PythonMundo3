print('¬' * 6, '\033[33mJOGANDO DADOS\033[m', '¬' * 6)
from random import randint
from time import sleep
from operator import itemgetter # Biblioteca para organizar as chaves 1(números sorteados)
jogadores = {'jog1': randint(1, 6), 'jog2': randint(1, 6),
             'jog3': randint(1, 6), 'jog4': randint(1, 6)}
rk = list() # 'rk' de ranking, necessário para colocar em ordem
print('\033[33mValores Sorteados:\033[m')
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(2)
rk = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # Necessário para colocar os dados (0 e 1) em ordem e do maior para o menor.
print()
print('\033[32mRanking dos Jogadores:\033[m')
for i, v in enumerate(rk): # Utilizado porque 'rk' é uma lista.
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')




