print('|'*6, '\033[35mMÓDULOS E PACOTES\033[m', '|'*6)
# AULA TEÓRICA:
def fatorial(n):
    f = 1 # A variável sempre recebe 1 quando é multiplicação.
    for c in range(1,n+1):
        f *= c
    return f
def dobro(n):
    return n*2
def triplo(n):
    return n*3
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é \033[32m{fat}\033[m')
print(f'O dobro de {num} é \033[32m{dobro(num)}\033[m')
print(f'O triplo de {num} é \033[32m{triplo(num)}\033[m')
print('-=-'*25)
# Criando modulos das funções:
import uteis  # Mais indicado, pode ser usado o 'from uteis import fatorial2', porém pode dar conflito.
num2 = int(input('Digite um valor: '))
fat2 = uteis.fatorial2(num2)
print(f'O fatorial de {num2} é \033[33m{fat2}\033[m')
print(f'O dobro de {num2} é \033[33m{uteis.dobro(num2)}\033[m')
print(f'O triplo de {num2} é \033[33m{uteis.triplo(num2)}\033[m')
print('-=-'*25)
# AULA PRÁTICA:
from pct import numeros # Importa o pacote criado com as funções.
num3 = int(input('Digite um valor: '))
fat3 = numeros.fatorial3(num3)
print(f'O fatorial de {num3} é \033[34m{fat3}\033[m')
print(f'O dobro de {num3} é \033[34m{numeros.dobro(num3)}\033[m')
print(f'O triplo de {num3} é \033[34m{numeros.triplo(num3)}\033[m')
