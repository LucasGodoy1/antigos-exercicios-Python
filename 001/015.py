print ('*'* 30)
print ('*        Calculo da média!   *')
print ('*'*30)
n1 = float(input('Qual a sua 1° nota ?:'))
n2 = float(input('Qual a sua 2° Nota? :'))
n3 = float(input('Qual a sua 3° Nota? :'))
n4 = float(input('Qual a sua 4° Nota? :'))
m = (n1 + n2 + n3 + n4) /4
print ('Sua média é {}'.format(m))
if m >= 10.0:
    print ('Parabens voce é  exemplat!')
else: m <= 7.0
print ('essa foi por pouco!')