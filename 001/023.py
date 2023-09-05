# ESSE METODO É BOM SE QUISER SABER O VALOR DO AUMENTO SEPARADO DO  TOTAL
#sal = float(input('Qual é seu salario atual?'))
#if sal <= 1250:
#    nov = (sal * 15) /100
#    total = sal + nov
#if sal >1250:
#    nov = (sal * 10) / 100
#    total = sal + nov
# print ('seu aumento será de R$: {:.2f}'.format(nov))
# print('seu novo salario será de R$: {:.2f}'.format(total))
#--------------------
# NOVA SINTAXY
sal = float(input('Qual é seu salario atual?'))
if sal <= 1250:
    novo = sal + (sal *15) / 100
else: novo = sal + (sal * 10) / 100
print ('Seu novo salario é de R$: {:.2f}'.format(novo))