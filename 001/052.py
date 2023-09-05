lp = 0
c = 1
s1 = int(input('Digite um numero de soma e [99] para parar'))
while lp != 99:
    s2 = int(input('Digite um numero de soma e [99] para parar'))
    if s2 == 99:
        lp = 99
        break
    s1 = s1 + s2
    c = c + 1
print (' voce digitou {} vezes o resultado da soma deles é de {} '.format(c, s1))
print ('Fim')