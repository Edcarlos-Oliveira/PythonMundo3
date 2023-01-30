print('-+-' * 3, '\033[34mINTERACTIVE HELPING SYSTEM IN PYTHON\033[m', '-+-' * 3)
from time import sleep
# Variável cores:
cores = ('\033[m',    # 0 - Sem cor
         '\033[41m',  # 1 - Cor background vermelha
         '\033[42m',  # 2 - Cor background Verde
         '\033[43m',  # 3 - Cor background Amarelo
         '\033[44m',  # 4 - Cor background Azul
         '\033[45m',  # 5 - Cor background Roxa
         '\033[7m'    # 6 - Cor background Branco
         );

def ajuda(op):
    titulo(f'Mostrando o Manual do comando: \'{op}\'', 4)  # As barras colocas as aspas no comando digitado.
    print(cores[6], end='')  # adciona a cor nas letras de fundo quando mostra o manual.
    help(op)
    print(cores[0], end='')  # Deixa o fundo branco quando mostra o manual.
    sleep(2)

def titulo(msg, cor=0):  # Caso nenhuma cor seja digitada fica 0.
    t = len(msg) + 4
    print(cores[cor], end='')  # Inclui as cores.
    print('~' * t)
    print(f'  {msg}')
    print('~' * t)
    print(cores[0], end='')  # Limpa as cores.
    sleep(1)

# Programa Principal
escolha = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    escolha = str(input('Função ou Biblioteca > '))
    if escolha.upper() == 'FIM':  # Encerra o sistema
        break
    else:
        ajuda(escolha)
titulo('ATÉ LOGO!', 1)
