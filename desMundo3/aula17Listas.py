print('¨'*6, '\033[35mCRIANDO LISTAS\033[m', '¨'*6)
print('\033[33mPARTE TEÓRICA AULA 17\033[m')
print('-'*30)
l = [5, 4, 8, 20, 10, 7]
# Métodos para ADCIONAR itens em uma lista:
l[3] = 15 # Adciona o número 15 no lugar do 20, 3ª posição.
l.append(21) # Adiciona o 21 no final da lista.
l.insert(0,6) # adciona o 6 antes do 5 que está na posição 0.
# Métodos para APAGAR itens de uma lista:
del l[3] # Apaga o 3º item da nova lista [6, 5, 4, 8, 15, 10, 7, 21] com as inserções acima, nesse caso o nº 8.
l.pop(3) # Nesse caso apaga também o 3º item da lista [6, 5, 4, 15, 10, 7, 21], o nº 15.
l.remove(10) # Nesse método também pode ser escrito por extenso o item que quer remover. Remove o nº 10 da lista.
l.pop() # Elimina o último elemento da lista nesse caso o nº 21, [6, 5, 4, 7, 21]
# Obs: Caso tente remover algo sem estar na lista vai dar erro o sistema, para evitar isso faz conforme ex. abaixo:
'''if 10 in l:
     l.remove(10)'''
print(l)
print('')
# Criando lista com 'list':
v = list(range(4,11)) # Cria uma lista de 4 até 10, o 'range' cria os valores ordenados.
v2 = [8,2,5,4,9,3,0] # Nesse caso os valores foram digitados desordenados.
v2.sort() # ordena os valores [0, 2, 3, 4, 5, 8, 9].
v2.sort(reverse=True) # Deixa os valores na ordem reversa 'decrescente' [9, 8, 5, 4, 3, 2, 0].
print(len(v)) # Para achar quantos elementos tem nas respectivas listas, nesse caso são 7.
print(len(v2))
print(v,'\n',v2)
print('-'*30)
print('\033[33mPARTE PRÁTICA DA AULA 17\033[m')
n = [2,5,9,1]
n[2] = 3 # Inclui o 3 na posição do 9 da lista [2, 5, 3, 1].
n.append(7) # Inclui o 7 depois do 1, final da lista [2, 5, 3, 1, 7].
n.sort(reverse=True) # Coloca a lista em ordem decrescente [7, 5, 3, 2, 1].
n.insert(2, 0) # Insere o 0 depois do 5 na posição 2 [7, 5, 0, 3, 2, 1].
n.insert(2,2) # [7, 5, 2, 0, 3, 2, 1]
# Obs: Caso haja dois elementos iguais na mesma lista o 'remove' remove apenas o 1º elemento encontrado:
n.remove(2) # Remove o 1º 2 encontrado os demais permanecem [7, 5, 0, 3, 2, 1].
# Quando um elemento não existe na lista:
if 4 in n: # Caso o elemento indicado esteja na lista remove normalmente.
    n.remove(4)
else:
    print('Não encontrei o número 4 na lista.')
print(len(n)) # Conta quantos elementos tem a lista.
print(n)
print('-'*30)
print('\033[32mMostrando Listas de outra forma\033[m')
v3 = list()
v3.append(5)
v3.append(9)
v3.append(4)
for lv in v3: # 'lv' Lista nova.
    print(f'{lv}...', end='')
print('')
for c, lv in enumerate(v3): # Para achar a posição que cada valor está.
    print(f'Na posição {c} encontrei o valor {lv}!')
print('Cheguei ao final da lista')
print('')
# Para colocar valores em lista digitados pelo usuário:
v4 = list()
for du in range(0,5): # Será pedido 5 valores, 'du' digitado pelo usuário.
    v4.append(int(input('Digite um valor: ')))
for c, lnv in enumerate(v4):  # Para achar a posição que cada valor está.
    print(f'Na posição {c} encontrei o valor: {lnv}') # 'lnv' Lista Novo Valores.
print('Cheguei ao final da lista digitada pelo usuário')
print('')
print('\033[33mPECULIARIEDADE DO PYTOHON\033[m')
print('')
l2 = [2,3,4,7]
l3 = l2 # Fazendo uma ligação entre l3 e l2.
# l3 = l2[:] # Nesse caso cria uma cópia de l2, altera apenas o l3, Lista L3: [2, 3, 8, 7].
l3[2] = 8 # Nesse exemplo cria uma ligação entre as duas listas l2 e l3, alterando ambas, ou seja, o 4 ficaria 8 Lista L2: [2, 3, 8, 7], Lista L3: [2, 3, 8, 7].
print(f'Lista L2: {l2}')
print(f'Lista L3: {l3}')













