main = float(input('Qual é seu salario atual ?'))
ano = float(input('Quantos anos de empresa?'))
porc = (main * ano) / 100
nov = main + porc
print ('Seu novo salario terá o aumento no valor de R$: {}'.format(porc))
print ('Total a receber de R$:{:.2f}'.format(nov))