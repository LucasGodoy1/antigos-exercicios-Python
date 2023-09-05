print ('-=-' *30)
print ('Vamso analisar o numero:' )
print ('-=-' *30)
num = int(input('Digite um numero: '))
res = num % 2
if res == 0:
    print ('seu numero é {} e ele se classifica como par'.format(num))
else: print ('Seu numero é {} e ele se calssifica como impar'.format(num))