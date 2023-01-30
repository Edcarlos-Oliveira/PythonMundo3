print('¬'*6, '\033[33mCADASTRO JOGADOR\033[m', '¬'*6)
cad = dict()
lg = list()
cad['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {cad["Nome"]} jogou? '))
for c in range(0, partidas):
    lg.append(int(input(f'Quantos gol(s) na {c + 1}ª partida? ')))
cad['gols'] = lg[:] # Cria uma lista dentro do dicionário.
cad['tot'] = sum(lg) # Soma os valores dentro da lista.
print('-='*25)
print('\033[33m',cad,'\033[m')
print('-='*25)
for k, v in cad.items():
    print(f'O campo \033[32m{k}\033[m tem o valor = \033[36m{v}\033[m')
print('-='*25)
print(f'O jogador \033[32m{cad["Nome"]}\033[m jogou \033[36m{partidas}\033[m partida(s).')
for i, v in enumerate(cad['gols']):
    print(f'   \033[30m=>\033[m Na {i + 1}ª partida, fez \033[34m{v}\033[m gol(s).')
print(f'Foi um total de \033[36m{cad["tot"]}\033[m gols.')





