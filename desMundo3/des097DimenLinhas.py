'''print('&.'*6, '\033[32mDIMENSIONANDO LINHAS\033[m', '&.'*6)
# Função:
def mens(txt):
    def escreva():
        print('~' * len(txt))
    escreva()
    print(f'{txt}')
    escreva()
mens('\033[36mEDCARLOS OLIVEIRA\033[m')
mens('\033[34mCurso de Python no Curso em Vídeo\033[m')
mens('\033[32mAprendendo\033[m')'''

# SOLUÇÃO DO DESAFIO PELO CURSO EM VIDEO.
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

escreva('\033[36mEDCARLOS OLIVEIRA\033[m')
escreva('\033[34mCurso de Python no Curso em Vídeo\033[m')
escreva('\033[32mAprendendo\033[m')


