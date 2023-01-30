print('¨'*6, '\033[35mNÚMEROS ALEATÓRIOS C/ TUPLA\033[m', '¨'*6)
from random import randint
al = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in al: # 'n' números, 'al' aleatórios.
    print(f'\033[32m{n}\033[m ', end='') # indentação é importante.
print(f'\nO \033[36mmaior\033[m valor sorteado foi: \033[36m{max(al)}\033[m')
print(f'O \033[36mmenor\033[m valor sorteado foi: \033[36m{min(al)}\033[m')














