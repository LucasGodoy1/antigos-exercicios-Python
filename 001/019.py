km = float(input('Quantos Km voce irá precisar para sua viagem?'))
if km <= 200:
    preco = km * 0.50
else: preco = km * 0.40
print ('Seu valor a pagar será de R${}'.format(preco))