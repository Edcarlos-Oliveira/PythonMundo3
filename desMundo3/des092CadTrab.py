print('¬'*6, '\033[33m''CADASTRO TRABALHADOR\033[m', '¬'*6)
from datetime import datetime
cad = dict() # Cadastro
cad['n'] = str(input('Nome: ')) # 'n' Nome
an = int(input('Ano de Nascimento\033[33m[4 dígitos]\033[m: ')) # 'an' Ano Nascimento
cad['id'] = datetime.now().year - an # Para pegar o ano atual do sistema, 'an' Ano de Nascimento.
cad['ct'] = int(input('Carteira de Trabalho\033[33m[0 não tem]\033[m: ')) # 'ct' Carteira Trabalho
if cad['ct'] != 0:
    cad['ac'] = int(input('Ano de Contratação\033[33m[4 dígitos]\033[m: '))
    cad['sl'] = float(input('Salário:R$  '))  # 'sl' Salário.
    cad['ap'] = cad['id'] + ((cad['ac'] + 35) - datetime.now().year) # 'ap' aposentadoria
for k, v in cad.items():
    print(f' - {k} é: {v}')
print('\033[33mLEGENDA:\033[m')
print('n = Nome\nid = Idade\nct = Carteira de Trabalho\nac = Ano de Contratação\nsl = Salário\nap = Aposentadoria')


