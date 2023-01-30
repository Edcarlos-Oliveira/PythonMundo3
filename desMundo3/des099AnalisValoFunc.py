print('&.'*6, '\033[32mANALISANDO VALORES\033[m', '&.'*6)
from time import sleep
# Funções:
def linh():
    print('-=-'*20)
def maior(* n):
    linh()
    c = mai = 0
    print('Analisando valores passados...')
    for v in n:
        print(f'\033[32m{v}\033[m ', end=' ')
        sleep(0.5)
        if c == 0:
            mai = v
        else:
            if v > mai:
                mai = v
        c += 1
    print(f'Foram informados \033[34m{c}\033[m valores ao todo.')
    print(f'O maior valor informado foi \033[36m{mai}\033[m.')

# Programa Principal:
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()









