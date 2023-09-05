emp = float(input('Qual o valor da casa ?'))
sal = float(input('Qual é o seu salario?'))
ano = float(input('Em quantos anos deseja pagar?'))
meses = ano * 12
valor = emp / meses
porc = sal * 30 / 100
if valor > porc:
    print ('Voce não foi aprovado')
else: print ('voce foi aprovado')
print ('o calculo do seu emrpestimo é de {:.0f}vezes e no valor de R${:.2f}'.format(meses,valor))



