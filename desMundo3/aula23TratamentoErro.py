print('-*-'*3, '\033[31mTRATAMENTO DE ERROS\033[m', '-*-'*3)
# AULA TEÓRICA
# EXCEÇÕES:
'''primt(x) # Apresenta erro de sintaxe, trocou o 'n' por 'm', 'NameError'.
print('')
print(x) # Apresenta erro de semantico, não declarou a váriavel 'x', 'NameError'
n = int(input('Numero: ')) # Tecnicamente certo, porém ao digitar um número por extenso apresenta 'ValueError'
print(f'Você digitou o número {n}')
print()
a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a/b
print(f'O resultado é {r}') # Tecnicamente não há erro, mas ao dividir 'a' e 'b', sendo 'b' = 0, apresenta o erro 'ZeroDivisionErro'
r = 2 / '2' # Apresenta um erro: 'TypeErro'
lst = list[3,6,4]
print(lst[3]) # Apresenta erro: 'IndexError, pois na lista temos os indices 0,1 e 2, para os dicionários seria 'KeyError'
import uteis # Caso o modulo 'uteis' não seja encontrada apresenta o erro: "ModuleNotFoundError"
'''
# AULA PRÁTICA:
# CORRINGINDO OS ERROS:
try: # Tente
    a2 = int(input('Numerador: '))
    b2 = int(input('Denominador: '))
    r2 = a2/b2
except (ValueError, TypeError): # Escreve o print caso os erros sejam esse.
    print('Tivemos um problema com os tipos de dados que você digitou!')
except ZeroDivisionError: # Escreve o print caso os erros sejam esse.
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt: # Escreve o print caso os erros sejam esse.
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}') # Mostra a causa do erro
else:
    print(f'O resultado é {r2}') # Caso não haja erro mostra o resultado de 'r2'
finally: # Vai ser executado independente se houve erro ou não.
    print('Volte sempre! Muito Obrigado!')



