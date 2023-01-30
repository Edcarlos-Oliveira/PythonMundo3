print('&.'*6, '\033[32mFUNÇÕES PARTE 1\033[m', '&.'*6)
# AULA TEÓRICA:
# - Função
def mostralinha(): # função criada para mostrar linhas, 'def' significa definação da função.
    print('-'*30)

# - Programa Principal:
mostralinha()
print(' '*5, '\033[33mSISTEMA DE ALUNOS\033[m')
mostralinha()

# - Função com mensagem:
def mensagem(msg):
    mostralinha()
    print(' '*5, msg)
    mostralinha()
mensagem('\033[35mAPRENDENDO PYTHON\033[m')

# Funções com números:
def soma(a, b):
    s = a + b
    print('\033[36m',s,'\033[m')
# - Programa Principal:
soma(4,5)
mostralinha()
soma(8,9)
mostralinha()
soma(2,1)

# - Explicitando cada valor da função soma:
def soma1(a, b):
    print(f'A = \033[32m{a}\033[m e B = \033[32m{b}\033[m')
    s = a + b
    print(f'A soma A + B = \033[36m{s}\033[m')

# - Programa Principal
mostralinha()
soma1(4,5) # Nesse caso sem explicitar o 1º valor vai para A e 2º para B
mostralinha()
soma1(b=8,a=9) # Nesse caso o 1º valor vai para B e 2º para A, foi explicitado.
mostralinha()
soma1(2,1)
mostralinha()

# Usando desempacotamento:
def soma2(* val):
    s = 0
    for num2 in val:
        s += num2
    print(f'Somando os valores \033[32m{val}\033[m temos: \033[36m{s}\033[m')
soma2(5,2)
soma2(2, 9, 4)

# Trabalhando com contador:
mostralinha()
def contador(* num): # Nesse caso o Python fica encarregado de ler vários números, usando o '*'
    print('\033[36m',num, '\033[m')
print('RESULTADO FICA EM TUPLAS:')
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
mostralinha()

# Trabalhando com for
def contador1(* num1): # Nesse caso o Python fica encarregado de ler vários números, usando o '*'
    for valor in num1:
        print(f'\033[33m{valor}\033[m ', end='')
    print()
    tam = len(num1) # Mostra a quantidade de números em cada tupla.
    print(f'Recebi os valores \033[33m{num1}\033[m e são ao todo \033[36m{tam}\033[m números.')
contador1(2,1,7)
contador1(8,0)
contador1(4,4,7,6,2)
mostralinha()

# Funções com Listas:
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

# Programa Principal:
valores = [6,3,9,1,0,2]
dobra(valores)
print(f'\033[36m{valores}\033[m')






