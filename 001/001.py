nome = input ('Qual seu nome?')
idade = input ('Qual sua idade?')
altura = float( input ('Qual sua altura?'))
print ('Seu nome é:', nome, 'sua idade é:', idade, 'sua altura é:', altura)
v1 = float( input ('Qual seu salario?'))
v2 = float( input ('Qual a porcentagem deseja receber?:'))
soma = v1 * v2 / 100
res = v1 + soma
print ('voce terá o total de R$:', res)
print ('O valor do {} * {} e / 100 é {}'.format(v1,v2,soma))