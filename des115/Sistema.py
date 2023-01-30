print('-*-'*3, '\033[31mSISTEMA CADASTRO\033[m', '-*-'*3)
from des115.lib.interface import * # Importa todos os arquivos.
from des115.lib.arquivo import *
from time import sleep

# Programa Principal:
arq = 'Cadastro.txt' # Nome do arquivo a ser criado
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    try:
        r = menu(['\033[34mMostrar Pessoas Cadastradas\033[m', '\033[32mCadastrar Pessoas\033[m', '\033[31mSair do Sistema\033[m'])
        if r == 1:
            # Ler o arquivo de cadastro:
            lerArquivo(arq)
        elif r == 2:
            # Opção para cadastrar uma Pessoa:
            titulo('NOVO CADASTRO')
            nome = str(input('Nome: ')).strip().upper()
            idade = leiaInt('Idade: ')
            cadastrar(arq, nome, idade)
        elif r == 3:
            titulo('\033[35mSaíndo do Sistema...Até logo!\033[m') # Nessa caso coloca as configurações da função titulo.
            break
        else:
            print('\033[31mERRO: Digite uma opção válida.\033[m')
        sleep(1)
    except KeyboardInterrupt:
        print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
        print('\033[36mVolte Sempre!\033[m')
        break









