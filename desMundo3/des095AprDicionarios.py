print('¬'*6, '\033[33mAPRIMORANDO DICIONÁRIOS\033[m', '¬'*6)
cad = dict() # cadastro
lg = list() # Lista de gols
lgn = list() # lista de gols e nome
# Lendo os dados dos jogadores:
while True:
    cad.clear()
    cad['nome'] = str(input('Nome do Jogador: ')).strip().upper()
    part = int(input(f'Quantas partidas \033[34m{cad["nome"]}\033[m jogou? '))
    lg.clear()
    for c in range(0,part):
        lg.append(int(input(f'Quantos gols na \033[34m{c + 1}ª\033[m partida? ')))
    cad['gols'] = lg[:]
    cad['tot'] = sum(lg)
    lgn.append(cad.copy())
    while True:
        op = str(input('Quer continuar\033[32m[S/N]\033[m? ')).strip().upper()[0]
        if op in 'SN':
            break
        print('\033[31mERRO! Responda apenas S ou N.\033[m')
    if op == 'N':
        break
print('-='*25)
# Análise dos dados:
print('cod ', end='')
for i in cad.keys(): # Escreve os valores dos 'cod'
    print(f'{i:<15}', end='')
print()
print('-='*25)
for k, v in enumerate(lgn): # Escreve os dados da lista.
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    esc = int(input("Mostrar dados de qual jogador\033[33m[999 encerra]\033[m? "))
    if esc == 999:
        break
    if esc >= len(lgn):
        print(f'\033[31mERRO! Não existe jogador com código\033[m {esc}!')
    else:
        print(f' -- \033[32mLEVANTAMENTO DO JOGADOR\033[m {lgn[esc]["nome"]}:')
        for i, g in enumerate(lgn[esc]["gols"]):
            print(f'    No jogo \033[36m{i +1}\033[m fez \033[36m{g}\033[m gols.')
print('\033[34m<< OBRIGADO POR USAR NOSSA ANÁLISE DE DADOS >>\033[m')











