print('¨'*6, '\033[35mMATRIZ 3X3 v2\033[m', '¨'*6)
m = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0 # 'spar' soma dos pares, 'mai' maior valor, 'scol' soma da 2ª coluna.
# Para receber os valores digitados pelo usuário
for l in range(0,3):
    for c in range(0,3):
        m[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print(f'A matriz digitada foi: \033[33m{m}\033[m')
# Para mostrar a matriz:
for l in range(0,3):
    for c in range(0,3):
        print(f'\033[32m[\033[m{m[l][c]:^5}\033[32m]\033[m', end='')
        if m[l][c] % 2 == 0: # Para somar os números pares.
            spar += m[l][c]
    print() # Essencial para quebrar as linhas.
print(f'A soma dos valores pares são: \033[34m{spar}\033[m')
for l in range(0,3): # Para manter a contagem da linha de 0,2.
    scol += m[l][2] # Mantem a contagem da linhas, a coluna é fixa.
print(f'A soma dos valores da terceira coluna são: \033[36m{scol}\033[m')
for c in range(0,3):
    if len(m) == 0: # Poderia também ser escrito 'if c == 0:'
        mai = m[1][c]
    elif m[1][c] > mai:
        mai = m[1][c]
print(f'O maior valor da segunda linha é: \033[33m{mai}\033[m')









