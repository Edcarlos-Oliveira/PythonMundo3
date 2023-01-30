print('-+-'*3, '\033[34mANÁLISE DE VOTAÇÃO\033[m', '-+-'*3)
from datetime import date
def voto():
    """
    ⇒ Recebe os dados e mostra na tela.
    an ⇒ Ano de Nascimento.
    aa ⇒ Ano atual capturado pelo sistema, utilizando a biblioteca 'datetime'.
    :return: Sem retorno.
    """

    an = int(input('Em que ano você nasceu \033[32m[4 dígitos]\033[m? '))
    aa = date.today().year - an
    if 18 <= aa <= 65:
        print(f'Com \033[34m{aa}\033[m anos: \033[36mVOTO OBRIGATÓRIO.\033[m')
    elif 16 <= aa < 18 or aa > 65:
        print(f'Com \033[34m{aa}\033[m anos: \033[32mVOTO FACULTATIVO.\033[m')
    else:
        print(f'Com \033[34m{aa}\033[m anos: \033[31mNÃO VOTA.\033[m')
voto()
help(voto)
print('-=-'*25)
# Solução Curso em Video:
def voto(ano):
    from datetime import date # Nesse caso dentro da função economiza espaço.
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))



