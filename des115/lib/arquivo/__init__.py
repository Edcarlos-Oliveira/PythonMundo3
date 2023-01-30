from des115.lib.interface import *
# Para verificar se existe o arquivo ou não.
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # 'rt' leia o arquivo.
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

# Para criar o arquivo caso não exista:
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # O '+' é de suma importância para criação do arquivo.
        a.close()
    except:
        print('\033[31mERRO: Na crição do arquivo\033[m')
    else:
        print(f'\033[36mArquivo {nome} criado com SUCESSO.\033[m')

# Função para ler o arquivo criado:
def lerArquivo(nome):
    try:
        a = open(nome, 'rt') # Nesse caso não usa 'a.close', pois a ideia é ler o arquivo.
    except:
        print('\033[31mERRO ao ler arquivo.\033[m')
    else:
        titulo('PESSOAS CADASTRADAS')
        for lin in a: # 'lin' de linha
            d = lin.split(';') # Utiliza o 'split' para separar o ';'
            d[1] = d[1].replace('\n', '') # Para eliminar a formatação do '\n' colocado na função 'cadastar'.
            print(f'{d[0]:<22}{d[1]:>3} anos') # '<30' alinhamento a esquerda, '>3' alihamento a direita.
    finally:
        a.close() # Fecha o arquivo, hsvendo erro ou não.

# Função para cadastrar as pessoas:
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') # 'at' de append text para adicionar os cadastros.
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um ERRO na hora de escrever os dados!\033[m')
        else:
            print(f'\033[36mNovo regstro de {nome} adcionado com SUCESSO!\033[m')
            a.close() # Fecha o arquivo
