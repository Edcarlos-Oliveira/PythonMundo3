print('-+-'*3, '\033[34mFUNÇÃO PARA FATORIAL\033[m', '-+-'*3)
def fatorial(n, show=False):
    """
    => Calcula o fatorial de algum número.
    :param n: Número a ser calculado.
    :param show: [Opcional] Mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show: # Mostra a conta do fatorial e o total
            print(c, end='')
            if c > 1: # Para incluir o 'x' antes do 1
                print(' x ', end='')
            else:
                print(' = ', end='') # Inclui o '=' depois do 1
        f *= c
    return f
print('Resultado SEM o "show=True": \033[33m',fatorial(5),'\033[m') # Dessa maneira mostra apenas o total do fatorial
print('Resultado COM o "show=True":', end=' ')
print(f'\033[36m{fatorial(5, show=True)}\033[m') # Com a utilização do 'show=True' mostra a conta do fatorial
print('------ \033[33mHELP DO FATORIAL\033[m -----')
help(fatorial)

