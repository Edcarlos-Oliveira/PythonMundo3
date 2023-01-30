print('¨' * 6, '\033[33mTUPLA LENDO NÚMEROS\033[m', '¨' * 6)
nx = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
      'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezanove', 'Vinte')

for c in range(0, len(nx)):
    n = int(input('Digite um número entre \033[32m0 e 20\033[m: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número: \033[36m{nx[n]}\033[m')

# Poderia ser reescrito com 'while True:
'''while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ',end='')
print(f'Você digitou o número: \033[36m{nx[n]}\033[m')'''





