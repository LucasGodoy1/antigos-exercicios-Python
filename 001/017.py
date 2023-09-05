print ('-=-' *30)
print ('Vamos verificar se voce seria multado?')
print ('-=-' *30)
velo = float(input('Qual é sua velocidade atual ?: '))
if velo >60.0:
    mult = (velo - 60) *9
    print('-=-' * 30)
    print ('voce foi multado em R${:.2f}'.format(mult))
    print('-=-' * 30)
else:
    print('-=-' * 30)
    print ('parabens voce está no limite da pista!')
    print ('-=-' *30)