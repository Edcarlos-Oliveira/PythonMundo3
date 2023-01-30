print('-+-'*3, '\033[34mFICHA JOGADOR\33[m', '-+-'*3)
def ficha(nome ='<desconhecido>', gol = 0):
    print(f'O jogador \033[33m{nome}\033[m fez \033[36m{gol}\033[m gol(s) no campeonato.')
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric(): # Verifica se pode ser um número ou não.
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)


