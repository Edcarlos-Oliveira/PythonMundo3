print('&.'*6, '\033[32mFUNÇÕES PARTE 2\033[m', '&.'*6)
# AULA TEÓRICA:
# Usando 'interactive help'
print('\033[32mClica em Python Console na barra abaixo e digita help()\033[m')
# Outra maneira de utilizar o 'interactive help'
help(print)
print('\033[33mDocumentação do input com __doc__:\033[m')
print(input.__doc__) # Mostra a documentação do input.
print('\033[34mDocumentação do input com help:\033[m')
help(input) # Outra maneira de mostrar a documentação do input.
# Usando 'docstrings':
print('\033[35mUSANDO AS DOCSTRINGS\033[m')
def contador(i, f, p):
    """
    ⇒ Faz a contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')
help(contador) # Mostra a docstring criada.
print('\033[34mPARÂMETROS OPCIONAIS\033[m')
# Parâmetros opcionais:
def somar(a, b, c=0): # 'c=0' parâmetro opcional caso c não receba nenhum valor.
    s = a + b + c
    print(f'A soma vale {s}')
somar(3,2,5)
somar(8,4)
print('\033[33mSituação 2:\033[m')
def somar2(a=0, b=0, c=0): # Também pode ser usado parametros em todos
    s = a + b + c
    print(f'A soma vale {s}')
somar2(3,2,5)
somar2(8,4)
somar2()
print('\033[36mESCOPO DE VaRIÁVEIS\033[m')
# Escopo de variáveis:
def teste():
    x = 8 # Variável Local.
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x} ')

# Programa Principal:
n = 2 # Variável global
print(f'No programa principal, n vale {n}')
teste()
# print(f'No programa principal, x vale {x}') # Vai dar erro, pois x é uma variável local.
print('\033[31mTESTE 2:\033[m')
def teste2():
    n2 = 2 # Escopo Local
    print(f'N2 dentro vale {n2}')
n2 = 4 # Escopo Global
teste2()
print(f'N2 fora vale {n2}')
print('\033[30mTESTE 3:\033[m')
def teste3():
    global n1 # Nesse caso elimina o N1 global e torna o n1 local como global. Escreve 'N1 dentro e fora vale 2.
    n1 = 2
    print(f'N1 dentro vale {n1}')
n1 = 4
teste3()
print(f'N1 fora vale {n1}')
print('\033[36mRETORNO DE VALORES\033[m')
# Usando retorno de valores:
def somar3(a=0, b=0, c=0): # 'c=0' parâmetro opcional caso c não receba nenhum valor.
    s = a + b + c
    return s # Mostra o resultado em um print com todas as somas.

r1 = somar3(3,2,5)
r2 = somar3(8,4)
r3 = somar3(6)
print(f'Meus calculos deram {r1}, {r2} e {r3}.')
print()
# AULA PRÁTICA:
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f # Pode ser usado para valores lógicos também.
n = int(input('Digite um número: '))
print(f'O fatorial de \033[34m{n}\033[m é igual a: \033[36m{fatorial(n)}\033[m')
print()
# Outra maneira de mostrar o resultado:
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: \033[33m{f1}, {f2} e {f3}\033[m')
print()
print('\033[32mUsando "return" para valores lógicos\033[m')
def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False
n = int(input('Digite um número: '))
print(par(n), end=' ')
print()
if par(n):
    print('É par.')
else:
    print('Não é Par.')

