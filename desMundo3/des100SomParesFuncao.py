print('&.'*6, '\033[32mSOMANDO VALORES\033[m', '&.'*6)
from random import randint
from time import sleep
numeros = list()
def sorteio():
    num = [randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)]
    print(f'Sorteando \033[34m{len(num)}\033[m valores da lista: ', end='')
    for v in num:
        numeros.append(num[:])
        print(f'\033[33m{v}\033[m', end=' ')
        sleep(0.5)
    print('PRONTO!')
sorteio()
def soma():
    print(f'Somando os valores pares de: \033[32m{numeros[0]}\033[m', end='')
    s = 0
    for i, p in enumerate(numeros[0]):
        if p % 2 == 0:
            s += p
    print(f' temos: \033[36m{s}\033[m', end='')
    print()
soma()
print('-=-'*30)

# Solução Curso em Video
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')
def somaPar(lista):
    s = 0
    for valor in lista:
        if valor % 2 == 0:
            s += valor
    print(f'Somando os valores pares de {lista}, temos {s}')
    
numeros = list()
sorteia(numeros)
somaPar(numeros)




