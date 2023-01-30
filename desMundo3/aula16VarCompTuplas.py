print('¨'*6, '\033[33mVARIÁVEIS COMPOSTAS, TUPLAS\033[m', '¨'*6)
print('')
# As tuplas são imutáveis. (Não aceita alterações.)
# Nesse caso (Hamburger é 0, Suco 1, Pizza 2 e Pudim 3)
# Na representação com números negativos (hamburguer é -4, suco -3, pizza -2 e Pudim -1)
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print(lanche) # Mostra todos.
print(lanche[1]) # mostra o suco.
print(lanche[3]) # Mostra o pudim
print(lanche[-2]) # Mostra a Pizza
print(lanche[1:3]) # Mostra suco e pizza pq o último elemento é ignorado.
print(lanche[2:]) # Mostra da Pizza até o Pudim.
print(lanche[:2]) # Mostra do elemento 2 até a Pizza, ignora o último, resultado Hamburger e suco.
print(lanche[-2:]) # Mostra pizza e pudim.
print(lanche[-3]) # Mostra suco, pizza e pudim.
print('')
# Nesse caso abaixo mostra a string para cada comida:
lanche2 = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
for comida in lanche2: # Poderia ser reescrito 'for cont in range(0, len(lanche2)): print(lanche2[cont])'
    print(f'Vou comer {comida}')
print(sorted(lanche2)) # Para ser exibido em ordem.
print('Comi muito...')
print('')
# ideal para ser usado quando quer mostrar a posição:
for cont in range(0, len(lanche2)):
    print(lanche2[cont], end=' ¬')
    print(f' Eu vou comer {lanche2[cont]} na posição: {cont}')
print('')
# Para conseguir enumerar com esse for:
for pos, comida in enumerate(lanche2):
    print(f'Eu vou comer {comida} na posição {pos}')
print('')
# Tuplas com números:
a = (2,5,4)
b = (5,8,1,2)
c = a + b # Nesse caso junta as tuplas, não soma os números.
c2 = b + a # Nesse caso não é a mesma coisa que a + b.
print(c, 'e', c2)
print(len(c)) # Mostra a quantidade de itens, no caso de a e b são 7.
print(c.count(5)) # Para mostrar quantas vezes aparece o número 5 entre a e b.
print(c.index(8) + 1) # Para verificar a posição do 8 entre a e b.
print('')
# Nesse exemplo mostra que a tupla pode receber mais de um dado diferente:
pessoa = ('Edcarlos', '46', 'M')
print(pessoa)





















