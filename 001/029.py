not1 = float(input('Qual a sua nota em pt '))
not2 = float (input('Qual a sua nota em mat '))
not3 = float(input('Qual a sua nota em cie '))
not4 = float(input('Qual a sua nota em Geo '))
media = (not1 + not2 + not3 + not4) /4
if media >= 8:
    print ('Parabens voce passou de ano')
elif 5 <= media <=7:
    print ('essa foi por pouco, tem que melhorar')
elif media < 5:
    print ('Voce está reprovado')
