def metade(n=0, sit=False):
    """
    ⇒ Calcula a metade de um determinado preço, retornando o resultado com ou sem formatação.
    :param n: O valor que quer reajustar
    :param sit: Quer a saída formatada ou não
    :return: O valor reajustado com ou sem formatação.
    """
    if sit is False:
        return n/2
    else:
        return formate(n / 2)

def dobro(n=0, sit=False):
    if sit is False:
        return n * 2
    else:
        return formate(n * 2)

def aumentar(n=0, sit=False):
    if sit is False:
        return n+(n * 20/100)
    else:
        return formate(n + (n * 20/100))

def diminuir(n=0, sit=False):
    if sit is False:
        return n-(n * 12/100)
    else:
        return formate(n-(n * 12/100))

def formate(n=0, abrev='R$', sit=False):
    if sit:
        return n
    else:
        return f'{abrev}{n:.2f}'.replace('.', ',')
def resumo(n=0):
    print('-'*20)
    print('  RESUMO DO VALOR')
    print('-'*20)
    print(f'Preço analisado: {formate(n)}')
    print(f'Dobro do preço:  {formate(dobro(n))}')
    print(f'Metade do preço: {formate(metade(n))}')
    print(f'20% de aumento:  {formate(aumentar(n))}')
    print(f'12% de redução:  {formate(diminuir(n))}')
