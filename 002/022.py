def helpco(a):
    help(a)


def titulo(msg):
    tam = len(msg)
    print('~'* (tam+4))
    print(f'  {msg}')
    print('~'* (tam+4))

while True:
    titulo('Comando Note')
    titulo('Escreva [fim] para sair')
    he = str(input('O que voce procura? ')).strip().lower()
    if he == 'fim':
        print ('\033[0;31mPrograma encerrado !..\033[m')
        break
    else:
        helpco(he)