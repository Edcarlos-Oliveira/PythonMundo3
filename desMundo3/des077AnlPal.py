print('¨' * 6, '\033[35mACHANDO AS VOGAIS\033[m', '¨' * 6)
t = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
     'PROGRAMADOR', 'FUTURO')
for anl in t:  # 'anl' de análise em tupla.
    print(f'\nNa palavra \033[32m{anl.upper()}\033[m temos as vogais: ', end='')
    for vg in anl:  # 'vg' Vogais em 'analise'.
        if vg.lower() in 'aeiou':  # 'vg.lower()' vogais em minusculas.
            print('\033[36m',vg,'\033[m', end=' ')
