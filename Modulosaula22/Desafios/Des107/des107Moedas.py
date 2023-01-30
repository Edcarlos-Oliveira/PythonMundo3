print('-$-'*3, '\033[34mCALCULANDO MOEDAS\033[m', '-$-'*3)
import moeda # Biblioteca criada para o desafio 107.
p = float(input('Digite o preço R$: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% no valor de {p}, temos {moeda.aumentar(p)}')
print(f'Diminuindo 13% no valor de {p}, temos {moeda.diminuir(p)}')
