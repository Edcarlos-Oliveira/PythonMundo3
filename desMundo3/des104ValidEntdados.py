print('-+-'*3, '\033[34mVALIDANDO ENTRADA DE DADOS\033[m', '-+-'*3)
def leiaInt(msg):
    validador = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            validador = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if validador:
            break
    return valor

# Programa Principal:
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')





