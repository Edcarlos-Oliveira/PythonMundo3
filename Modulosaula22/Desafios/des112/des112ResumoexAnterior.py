print('-$-'*3, '\033[34mCALCULANDO MOEDAS\033[m', '-$-'*3)
from UtilidadesCeV import moeda
from UtilidadesCeV import dado
p = dado.leiaDinheiro('Digite o preço R$: ')
moeda.resumo(p)
