print('-+-'*3, '\033[34mANALISANDO E GERANDO DICIONÁRIO\033[m', '-+-'*3)
def notas(* n, sit=False):
    """
    => Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicado se deve ou não adcionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    dados = dict()
    mai = men = s = 0
    dados['Total'] = len(n)
    for c in range(len(n)):
        if c == 0:
            mai = men = n[c]
        else:
            if n[c] > mai:
                mai = n[c]
            if n[c] < men:
                men = n[c]
    dados['Maior'] = mai
    dados['Menor'] = men
    for v in n:
        s += v
        m = s / len(n)
        dados['Média'] = f'{m:.2f}'
        if sit:
            if m < 5:
                dados['Situação'] = 'RUIM'
            elif 5 <= m < 7:
                dados['Situação'] = 'RAZOÁVEL'
            else:
                dados['Situação'] = 'BOA'
    print(dados)
notas(5.5, 2.5, 1.5, sit=True)
help(notas) # Mostra as docsstrings
print('-=-'*25)
# SOLUÇÃO CURSO EM VIDEO:
def notas(* n, sit=False):
    """
    => Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicado se deve ou não adcionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r
# Programa Principal
resp = notas(10,2,6,8, sit=True)
print(resp)
help(notas)






