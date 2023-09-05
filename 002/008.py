listam = []
listaf = []
dados = {}
idade = media = soma = c = cf = ac = 0

while True:
    q1 = str(input('Nome: '))
    q3 = int(input('Idade: '))
    q2 = str(input('Sexo [M/F]')).strip().upper()[0]
    if q2 =='M':
        listam.append(q1)
        listam.append(q3)
        listam.append(q2)
        c += 1
        cf += 1
        soma += q3
        

    elif q2 =='F':
        listaf.append(q1)
        listaf.append(q3)
        listaf.append(q2)
        soma += q3
        c += 1
        

    dej = str(input('Deseja Continuar ? [S/N]')).strip().upper()[0]
    if dej =='N':
        dados['Homens'] = listam[:]
        dados['Mulheres'] = listaf[:]
        listam.clear()
        listaf.clear()
        media = soma / c
        break
    elif dej =='S':
        continue
print ('-'* 40)  
print (f'Ao todo temos {c} pessoas Cadastradas')
print (f'A media de idade é {media:.2f}') 
print ('-'* 40) 
for k, v in dados.items():
    print (f'{k} {v}')

