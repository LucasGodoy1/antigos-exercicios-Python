#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34629922#questions
cpf = '74682489070'
print (f'Verificando {cpf}')
nove_digitos = cpf[:9]
contador = 10
contador2 = 11
res = 0
res2 = 0
for d in nove_digitos:
    res += int(d) * contador
    contador -= 1
digito = (res*10) % 11
if digito <=9:
    digito = digito
else: digito = 0
dez_d = nove_digitos + str(digito)
res2 = 0
for d in dez_d:
    res2 += int(d) *contador2
    contador2 -= 1
digito2 = res2 * 10 % 11
if digito <=9:
    digito = digito
else: digito = 0
cpf1 = dez_d + str(digito2)
if cpf == cpf1:
    print ('Esse Cpf é valido')
else: print ('Esse Cpf Não é Valido!')
