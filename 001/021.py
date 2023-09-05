n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um numero:'))
n3 = int(input('Digite um numero:'))
if n1 <n2 and n1 <n3:
    menor = n1
if n2 <n1 and n2 <n3:
    menor = n2
if n3 <n1 and n3 <n2:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 >n2 and n3 >n1:
    maior = n3
print ('menor numero é: {}'.format(menor))
print ('seu numero maior é: {}'.format(maior))