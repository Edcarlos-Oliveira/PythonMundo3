print('-$-'*3, '\033[34mCALCULANDO MOEDAS\033[m', '-$-'*3)
import moeda
p = float(input('Digite o preço R$: '))
print(f'A metade de {moeda.formate(p)} é {moeda.formate(moeda.metade(p))}')
print(f'O dobro de {moeda.formate(p)} é {moeda.formate(moeda.dobro(p))}')
print(f'Aumentando 10% no valor de {moeda.formate(p)} temos {moeda.formate(moeda.aumentar(p))}')
print(f'Diminuindo 13% no valor de {moeda.formate(p)} temos {moeda.formate(moeda.diminuir(p))}')
