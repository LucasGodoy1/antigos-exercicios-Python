lista = []
print ('-'*30)
print ('Lista de Compras!')
print ('-'*30)
print ('*' *30 )
while True:
    print ('Selecione uma opção:')
    op = str(input('[i]inserir [a]Apagar [l]Listar')).strip().upper()[0]
    if op == 'I':
        n1 = str(input('Digite o que deseja adicioanr a lista: '))
        lista.append(n1)
    elif op == 'A':
        while True:
            try:
                n2 = int(input('Escolha um Indice para apagar: '))
                del lista[n2]
                break
            except ValueError:
                print ('*' *42)
                print ('         Atenção!')
                print ('Não foi possivel Apagar, Digite um Numero!')
                print ('*' *42)
            except IndexError:
                print ('*' *42)
                print ('         Atenção!')
                print ('Não existe nada nesse indice')
                print ('*' *42)
                break

    elif op == 'L':
        for item in enumerate(lista):
            print (item)