print('¬'*6, '\033[33mMÉDIAS COM DICIONÁRIOS\033[m', '¬'*6)
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().upper()
dados['Média'] = float(input(f'Média de {dados["nome"]}: '))
sit = {'cond1':'Aprovado', 'cond2':'Reprovado','cond3':'Recuperação'}
print(f'O nome é: \033[35m{dados["nome"]}\033[m')
print(f'A Média é: \033[34m{dados["Média"]}\033[m')
if dados['Média'] >= 7:
    print(f'Situação é: \033[36m{sit["cond1"]}\033[m')
    if dados['Média'] >= 9:
        print(f'\033[33mPARABÉNS!!! \033[32m{dados["nome"]}\033[m, Você é um excelente aluno(a).\033[m')
elif 5 <= dados['Média'] < 7:
    print(f'Situação é: \033[33m{sit["cond3"]}\033[m')
else:
    print(f'Situação é: \033[31m{sit["cond2"]}\033[m')
    print(f'\033[31mATENÇÃO! \033[32m{dados["nome"]}\033[m , Você precisa estudar mais.\033[m')

