print('¨'*6, '\033[33m 20 PRIMEIROS COLOCADOS BRASILEIRÃO 2022\033[m', '¨'*6)
t = ('Palmeiras', 'Internacional', 'Fluminesse', 'Corinthians', 'Flamengo', 'Athletico Pr', 'Fortaleza', 'Sao Paulo', 'America MG',
     'Botafogo', 'Santos', 'Goias', 'Bragantino', 'Coritiba', 'Cuiaba', 'Ceara', 'Atletico Go', 'Avai', 'Juventude')
print(f'\033[4mLista de times do Brasileirão:\033[m \033[32m{t}\033[m')
print(f'\033[4mOs 5 primeiros são:\033[m \033[34m{t[:5]}\033[m')
print(f'\033[4mOs 4 últimos são:\033[m \033[31m{t[15:]}\033[m')
print('\033[4mTimes em ordem alfabética:\033[m \033[35m',sorted(t),'\033[m')
print(f'O \033[36mSao Paulo\033[m está na \033[36m{t.index("Sao Paulo")+1}ª\033[m posição.') # Importante o uso das aspas duplas.










