from time import sleep
escolha = 0

n1 = int(input('Digite o Primeiro Valor:'))
n2 = int(input('Digite o segundo Valor'))
while escolha != 5:
    print ('-'*40)
    escolha = int(input('''Escolha a alternativa desejada
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Numeros
    [5] sair do Programa'''))
    print('-' * 40)
    if escolha == 1:
        soma = n1 + n2
        print ('A soma entre {} + {} tem o resultado em {}'.format(n1, n2, soma))
        print('-' * 40)
    elif escolha ==2:
        mult = n1 * n2
        print ('A multiplicação entre {} * {} tem o resultado em {}'.format(n1, n2, mult))
        print('-' * 40)
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
            print('O maior numero entre {} e {} é {}'.format(n1, n2, maior))
        elif n1 == n2:
            print ('não existe numero maior os dois são iguais')
        print('-' * 40)
    elif escolha == 4:
        n1 = int(input('Digite o Primeiro Valor:'))
        n2 = int(input('Digite o segundo Valor'))
        print('-' * 40)
    sleep (2.5)
print ('Obrigado por usar')



