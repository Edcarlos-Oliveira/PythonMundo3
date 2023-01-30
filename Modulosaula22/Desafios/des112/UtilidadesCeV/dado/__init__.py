def leiaDinheiro(msg):
    valido = False
    while not valido:
        ent = str(input(msg)).replace(',', '.').strip()
        if ent.isalpha() or ent == '':
            print(f'\033[31mERRO: \"{ent}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(ent)
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





