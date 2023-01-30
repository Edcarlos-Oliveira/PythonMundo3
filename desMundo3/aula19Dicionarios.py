print('¬'*6, '\033[34mAULA SOBRE DICIONÁRIOS\033[m', '¬'*6)
# Aula Teórica:
# Tuplas(), Listas[] e Dicionários{}, sinais usados.
# As declarações podem ser da seguinte forma:
# dados = dict() ou dados = {} são as mesma coisas
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'], end=' ') # Escreve Pedro.
print(dados['idade']) # Escreve Idade.
print()
# Para adcionar um elemento:
dados['sexo'] = 'M'
print(dados['nome'], end=' ')
print(dados['idade'], end=' ')
print(dados['sexo'])
print(dados) # Escreve nome, idade e sexo
print()
# Para apagar:
del dados['idade'] # Apaga o elemento idade.
print(dados) # Escreve nome e sexo.
print()
# Novo exemplos:
filme = {'titulo':'Star Wors', 'ano':1977, 'diretor':'George Lucas'}
# 'titulo, ano e diretor' são os elementos chamados no Python de chaves(keys).
# Existem diferenças de 'valor, chaves e itens' conforme abaixo:
print(filme.values()) # Retorna os valores ({'titulo':'Star Wors', 'ano':1977, 'diretor':'George Lucas'})
print()
print(filme.keys()) # Escreve só as chaves 'titulo, ano e diretor'.
print()
print(filme.items()) # Escreve tanto os valores quanto as chaves.
print()
# Utilizando na estrutura for:
for k, v in filme.items():
    print(f'\033[36m{k} é: {v}\033[m') # Escreve todos os dados do dicionário.
print()
# Incluindo dicionário em listas:
locadora = list()
filme1 = {'titulo':'Star Wors', 'ano':1977, 'diretor':'George Lucas'}
filme2 = {'titulo':'Avangers', 'ano':2012, 'diretor':'Jose Whadon'}
filme3 = {'titulo':'Matrix', 'ano':1999, 'diretor':'Wachowski'}
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)
print(locadora[0]['ano']) # Escreve o no de '1977'.
print(locadora[2]['titulo']) # Escreve 'Matrix'.
print(locadora[1]['diretor']) # Escreve 'Jose Whadon'.
print()
# Aula Prática:
pessoas = {'nome':'Edcarlos', 'sexo':'M', 'idade':46}
pessoas['nome'] = 'heddy' # substitui 'Edcarlos' por 'heddy'.
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') # Importante o uso das aspas dupla.
print()
# Dicionário dentro de lista com for:
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # '.copy' copia os dados de estado.
print(brasil)
print()
print(brasil[0])




