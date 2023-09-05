import random
import time
print ('=-'*30)
print ('Vamos Jogar!')
print ('=-'*30)
print ('''Faça a sua escolha
[1] Pedra
[2] papel
[3] Tesoura
''')
player = int(input('Escolha a sua Opção'))
print('Jo')
time.sleep(2)
print('Ken')
time.sleep(1)
print('PO')
time.sleep(0.5)
itens = ('pedra', 'papel', 'tesoura')
cpu = random.randint(0,2)
if player == 1 and cpu == 1:
    player = str('pedra')
    print ('Voce perdeu')
elif player == 2 and cpu == 2:
    player = str('papel')
    print('Voce perdeu')
elif player == 3 and cpu == 0:
    player = str('Tesoura')
    print('Voce perdeu')
elif player == 1 and cpu == 0:
    player = str('pedra')
    print ('Voce empatou')
elif player == 2 and cpu == 1:
    player = str('papel')
    print ('Voce empatou')
elif player == 3 and cpu == 2:
    player = str('Tesoura')
    print ('Voce empatou')
else: print ('Voce Ganhou!')

print ('=-'*30)
print('Voce escolheu {}'.format(player))
print ('CPU escolheu {}'.format(itens[cpu]))
print ('=-'*30)

