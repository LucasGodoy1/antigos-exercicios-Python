from datetime import date
atual = date.today().year
nasc = int(input('Quando voce nasceu?'))
idade = atual - nasc
print ('Voce tem {} Anos'.format(idade))
if idade == 9:
    print ('Voce é um atleta mirim')
elif 10 <= idade <= 14:
    print ('Voce é um atleta infatil')
elif 15 <= idade <= 19:
    print ('Voce é um atleta junior')
elif 20 <= idade <= 25:
    print ('Voce é um atleta Senior')
elif idade >= 26:
    print ('Já pode se aposentar!')
