print('-$-'*3, '\033[34mCALCULANDO MOEDAS\033[m', '-$-'*3)
import moeda
p = float(input('Digite o preço R$: '))
moeda.resumo(p)
