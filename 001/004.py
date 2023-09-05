print ('-' * 30)
print (' Vamos calcular o Desconto ')
print ('-' * 30)
produto = int (input ('Qual o valor do produto?'))
desc = int (input ('Qual a procentagem do desconto que deseja ?'))
valor = produto * desc / 100
total = produto - valor
print ('Seu valor ha ser pago é: ', total, ' seu desconto foi de: ', valor)