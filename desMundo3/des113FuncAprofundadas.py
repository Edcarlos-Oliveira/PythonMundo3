print('-*-'*3, '\033[31mFUNÇÕES APROFUNDADAS\033[m', '-*-'*3)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número Inteiro válido.\033[m')
            continue # Joga direto para o laço novamente, ou seja, repete 'ni'
        except KeyboardInterrupt:
            print('\n\033[33mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n
def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO:, por favor digite um número Real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[33mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return f
ni = leiaInt('Digite um número Inteiro: ')
nf = leiaFloat('Digite um número Real: ')
print(f'O valor Inteiro digitado foi {ni} e o valor Real foi {nf}')
