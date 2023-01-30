print('-$-'*3, '\033[34mCALCULANDO MOEDAS\033[m', '-$-'*3)
import moeda
p = float(input('Digite o preço R$: '))
print(f'A metade de {moeda.formate(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.formate(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% no valor de {moeda.formate(p)} temos {moeda.aumentar(p, True)}')
print(f'Diminuindo 13% no valor de {moeda.formate(p)} temos {moeda.diminuir(p, True)}')
