def contagem (inicio, fim, pulo):
    print (f'Contagem de {inicio} até {fim} pulando de {pulo} em {pulo}')
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print (f' {cont} ', end= '')
            cont += pulo
        print (' Fim')
    elif inicio > fim:
        while cont >=fim:
           print (f' {cont} ', end= '') 
           cont -= pulo
        print (' Fim')


contagem (1, 10, 1)
print ('-'*30)
contagem (10, 1, 1)
print ('-'*30)
print ('Sua Vez')
print ('-'*30)

def usu():
    q1 = int(input('Inicio '))
    print ('-'*30)
    q2 = int(input('fim '))
    print ('-'*30)
    q3 = int(input('pulando '))
    contagem (q1, q2, q3)

usu()

