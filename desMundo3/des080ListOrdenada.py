print('¨'*6, '\033[35mLISTA ORDENADA\033[m', '¨'*6)
l = list()
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > l[-1]: # Se o número for maior que o último elemento
        l.append(n)
        print('Adicionado no \033[33mFINAL\033[m da lista.')
    else:
        pos = 0 # Posição
        while pos < len(l):
            if n <= l[pos]:
                l.insert(pos, n)
                print(f'Adicionado na posição \033[34m{pos}\033[m da lista.')
                break
            pos += 1
print(f'Os valores digitados em ordem foram: \033[36m{l}\033[m')





