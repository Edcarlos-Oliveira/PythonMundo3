def metade(n=0, sit=False):
    if sit is False:
        return n/2
    else:
        return formate(n / 2,)

def dobro(n=0, sit=False):
    if sit is False:
        return n * 2
    else:
        return formate(n * 2)

def aumentar(n=0, sit=False):
    if sit is False:
        return n+(n * 10/100)
    else:
        return formate(n + (n * 10/100))

def diminuir(n=0, sit=False):
    if sit is False:
        return n-(n * 13/100)
    else:
        return formate(n-(n * 13/100))

def formate(n=0, abrev='R$', sit=False):
    if sit:
        return n
    else:
        return f'{abrev}{n:.2f}'.replace('.', ',')
# SOLUÇÃO CURSO EM VIDEO:
# Poderia ser substituido:

'''def metade(n=0, sit=False):
    res = n / 2
    return res if sit is False else formate(res)

def dobro(n=0, sit=False):
    res = n * 2
    return res if sit is False else formate(res)

def aumentar(n=0, sit=False):
    res = n+(n * 10/100)
    return res if sit is False else formate(res)

def diminuir(n=0, sit=False):
    res = n-(n * 13/100)
    return res if sit is False else formate (res)

def formate(n=0, abrev='R$', sit=False):
    if sit:
        return n
    else:
        return f'{abrev}{n:.2f}'.replace('.', ',')'''



