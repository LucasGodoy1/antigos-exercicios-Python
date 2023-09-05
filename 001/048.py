s = 0
velho = float('-inf')
ida = 0
mnome = ''
fsex = 0
msex = 0
for lp in range (1,5):
    print ('------------{}--------------'.format(lp))
    nome = str(input('Qual é seu nome ?'))
    idade = int(input('Qual a sua idade?'))
    sexo = str(input('Qual é seu sexo? [M] ou [F]')).upper()

    s = s + idade
    if idade > ida:
        ida = idade
        mnome = nome
    if sexo == 'F' and idade < 20:
       fsex += 1

media = s / 4

print ('Maior idade é {} e o nome da pessoa é {}'.format(ida, mnome))
print ('Quantidade de mulheres abaixo de 20 anos é {}'.format(fsex))


