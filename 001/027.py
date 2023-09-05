print ('vAMOS ANALISAR QUAL NUMERO É MAIOR!')
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
if n1 > n2:
    print ('o maior numero é {}'.format(n1))
elif n2 > n1:
    print ('o maior numero é {}'.format(n2))
else: print ('o numero {} e o numero {} são iguais por tanto Nenhum numero é maior'.format(n1, n2))