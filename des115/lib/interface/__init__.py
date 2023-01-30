
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número Inteiro válido.\033[m')
            continue # Joga direto para o laço novamente, ou seja, repete 'n'
        else:
            return n


def linha(tam=33):
    return '-' * tam


def titulo(txt):
    print(linha())
    print('\033[34m',txt.center(33),'\033[m') # Para centralizar o texto
    print(linha())


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1 # Contador para numerar as opções
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    op = leiaInt('\033[33mSua Opção: \033[m')
    return op







