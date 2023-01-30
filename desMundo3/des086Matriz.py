print('¨'*6, '\033[35mMATRIZ 3X3\033[m', '¨'*6)
m = [[0,0,0],[0,0,0],[0,0,0]]
# Para receber os valores:
for l in range(0,3):
    for c in range(0,3):
        m[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# Para mostrar a matriz:
for l in range(0,3):
    for c in range(0,3):
        print(f'[{m[l][c]:^5}]', end='') # ':^5' para centralizar e espaçar por 5 vezes.
    print() # para quebrar uma linha







