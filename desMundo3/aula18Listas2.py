print('¨'*6, '\033[35mLISTAS 2\033[m', '¨'*6)
# AULA TEÓRICA:
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados) # Escreve pedro 25.
print(dados[0]) # Escreve Pedro
print(dados[1]) # Escreve 25
print()
# Listas dentro de listas:
pessoas = list()
pessoas.append(dados[:]) # Cria uma cópia de dados.
print(pessoas) # Escreve Pedro 25
print()
# Outro modelo de lista
pessoas2 = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas2) # Escreve todos da lista pessoas2
print(pessoas2[0][0]) # Escreve o item 0 'Pedro'.
print(pessoas2[1][1]) # Escreve o item 1 '19'
print(pessoas2[2][0]) # Escreve o item 2, 'João'
print(pessoas2[1]) # Escreve 'Maria 19
print()
# AULA PRÁTICA:
teste = list()
teste.append('Edcarlos')
teste.append(46)
galera = list()
print(teste)
galera.append(teste[:]) # Mostra o que está dentro de teste, usando [:] cria uma cópia.
teste[0] = 'Maria' # altera 'Edcarlos' para 'Maria' e '46' para '22'.
teste[1] = 22
galera.append(teste[:])
print(galera)
print()
# Também poderia ser criada da seguinte forma:
galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera2) # Escreve toda a lista.
print(galera2[0][0]) # Escreve 'João'
print(galera2[2][1]) # Escreve '13' do Joaquim.
print()
# Utilizando for:
for p in galera2: # Para cada pessoa em galera escreva pessoa.
    print(p) # Escreve toda a lista
    print(p[0]) # Escreve só os nomes de galera2.
print()
galera3 = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:]) # para jogar os dados digitados na variável galera3.
    dado.clear() # Para limpar os dados.
for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é o maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é o menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')










