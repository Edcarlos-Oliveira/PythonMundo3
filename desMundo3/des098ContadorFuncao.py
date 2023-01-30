print('&.'*6, '\033[32mCONTADOR PERSONALIZADO\033[m', '&.'*6)
from time import sleep
# Função:
def layout():
    print('-=-'*15)

def cont():
    layout()
    print('Contagem de 1 até de 10 de 1 em 1:')
    for c in range(1,11):
        print('\033[36m',c,'\033[m',end=' ')
        sleep(0.5)
    print('FIM!')
    layout()
    print('Contagem de 10 até 0 de 2 em 2:')
    for c2 in range(10, -1, -2):
        print('\033[31m',c2,'\033[m',end=' ')
        sleep(0.5)
    print('FIM!')
# Contagem pelo usuário:
    layout()
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
# Validação do 0 e números negativos:
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'A contagem de {i} até {f} de {p} em {p}:')
    for c3 in range(i, f + 1, p):
        if i <= f:
            print('\033[32m', c3, '\033[m', end=' ')
            sleep(0.5)
    for c3 in range(i, f - 1, -p):
        if i >= f:
            print('\033[31m',c3,'\033[m', end=' ')
            sleep(0.5)
    print('FIM!')
cont()




