from datetime import date
atual = date.today().year
dado = dict()

while True:
    n1 = str(input('Digite seu Nome: '))
    dado['Nome: '] = n1
    ano = int(input('Ano de nascimento: '))
    idade = atual - ano
    dado ['Idade: '] = idade
    q2 = int(input('Carteira de trabalho: [0 para finalizar] '))
    if q2 =='0':
        break
    else:
        dado['N° de Cta'] = q2
    q3 = int(input('Ano de contratação: '))
    dado['Ano de contratação: '] = q3
    aposen = idade + (q3 + 35) - atual
    dado['Ano de aposentadoria: '] = aposen
    q4 = float(input('Seu salario atual R$: '))
    dado['Salario: '] = q4
    dej = str(input('Deseja sair?[S/N] ')).strip().upper()[0]
    if dej =='S':
        break
    elif dej == 'N':
        continue
    else: 
        print ('Comando invalido')
print ('-'*40)
for k, v in dado.items():
    print (f'{k:<22} {v:<6}')
        
