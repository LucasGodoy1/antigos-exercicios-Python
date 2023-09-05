from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1,6),
'Jogador2': randint(1,6), 
'Jogador3': randint(1,6), 
'Jogador4': randint(1,6)}
rank = dict()
for k, v in jogo.items():
    print (f'{k} tirou o {v} no dado.')
    sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate (rank):
    print (f'{i+1}° lugar - {v[0]} com {v[1]} ')