nome = []
idade = []
while True:
    while True:
        n1 = str(input('Digite o seu nome: ')).upper()
        if n1 not in nome:
            nome.append(n1)
            break
        else:
            print ('Ja temso esse nome, não vou registrar!')
            continue
    n2 = int(input('Digite a sua idade: '))
    idade.append(n2)
    con = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if con =='S':
        continue
    elif con =='N':
        print('Operação encerrada!')
        break
    else: print ('Comando Invalido! tente novamente...')
print ('Nome:', end= ' ')
for nom in nome:
    print (f'{nom:^10}', end= ' ')
print ()
print ('idade: ', end= ' ')
for ida in idade:
    print (f'{ida:^10}', end= ' ')
