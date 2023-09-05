from random import randint
from time import sleep
cpu = randint (1, 10)
print ('-=-' *30)
print ('       -Jogo do acerto-')
print ('tente adivinhar o numero que pensei')
print ('-=-'*30)
player = int(input('Digite um numero: '))
print ('Processando...')
sleep (2)
if player == cpu:
    print('-=-' * 30)
    print ('PARABENS VOCE ACERTOU!')
    print('-=-' * 30)
else:
    print('-=-' * 30)
    print ('HA HA HA VOCE PERDEU!')
    print('-=-' * 30)