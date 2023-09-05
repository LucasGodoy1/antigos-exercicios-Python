from datetime import date
hj = date.today().year
nasc = int(input('Quando voce nasceu ?'))
ida = hj - nasc
print ('Se voce nasceu em {} voce tem {} anos'.format(nasc, ida))
if ida == 18:
    print ('Voce terá que se alistar esse ano {}'.format(hj))
elif ida < 18:
    ida = 18 - ida
    ano = hj + ida
    print ('falta {} anos para voce se alistar, seu alistamento será em {}'.format(ida, ano))
else:
    ano = ida - 18
    at = hj - ano
    print ('voce deveria ter se alistado em {} anos atras em {}'.format(ano, at))

