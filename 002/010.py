dadostemp = {}
lista = []
lgols = []
tot = 0
while True:
    dadostemp['Jogador'] = str(input('Nome: '))
    q1 = int(input(f'Quantas Partidas {dadostemp["Jogador"]} Jogou ?'))
    for c in range (q1):
        q2 = int(input(f'Quantos Gols na {c+1}° Partida??: '))
        tot = tot + q2
        lgols.append(q2)
    dadostemp['Gols'] = lgols[:]
    dadostemp['Total'] = tot
    lista.append(dadostemp.copy())
    dadostemp.clear()
    lgols.clear()
    tot = 0
    dej = str(input('Deseja Continaur? [S/N]')).strip().upper()[0]
    if dej =='S': continue 
    elif dej =='N': break
    else: print ('COMANDO INVALIDO!')
dadostemp = lista[:]
# rever manipulação de dados
for k, v in dadostemp.items():
    print (f'{k} {v}')