from random import randint
cpu = randint(0, 10)
print (cpu)
tentativas = 1
player = int(input('Qual numero a Cpu escolheu ?'))
if player != cpu:
    print ('Voce errou tente novamente')
    while player != cpu:
        tentativas += 1
        print('-' * 40)
        player = int(input('Qual numero a Cpu escolheu ?'))
        if player > cpu:
            print ('Voce passou!')
            print('-' * 40)
        elif player < cpu:
            print ('Voce ainda está abaixo!')
if tentativas ==1:
    print ('Parabens voce acertou de {}° !'.format(tentativas))
else:
    print ('-'*40)
    print ('Parabens voce acertou com {} tentativas'.format(tentativas))