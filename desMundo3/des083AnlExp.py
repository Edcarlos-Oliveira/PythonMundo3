print('¨'*6, '\033[35mVALIDANDO EXPRESSÕES\033[m', '¨'*6)
exp = str(input('Digite uma expressão: ')) # 'exp' expressão.
lex = list() # 'lex' lista das expressões.
for s in exp: # 's' símbolos na expressão
    if s == '(':
        lex.append('(')
    elif s == ')':
        if len(lex) > 0: # Se 'lex' tem um dado.
            lex.pop() # Apaga o último elemento.
        else:
            lex.append(')')
            break
if len(lex) == 0: # Verifica se todos os parenteses foram fechados.
    print('Sua expressão é \033[36mVÁLIDA!\033[m')
else:
    print('Sua expressão está \033[31mERRADA!\033[m')



