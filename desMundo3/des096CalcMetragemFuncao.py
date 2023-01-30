print('&.' * 6, '\033[34mMETRAGEM COM FUNÇÃO\033[m', '&.' * 6)
print(' '*5, 'ARÉA DE UM TERRENO')
print('-'*40)
# Função:
def area(lar, comp):
    a = lar * comp
    print(f'A área de um terreno \033[32m{lar} x {comp}\033[m é de \033[36m{a:.0f} m².\033[m')

# Programa Principal:
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

