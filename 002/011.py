dadostemp = {}
lista = []
while True:
    q1 = str(input('Digite seu nome: '))
    dadostemp['nome'] = q1
    q2 = int(input('Idade: '))
    dadostemp['idade'] = q2
    q3 = str(input('Sexo [M/F]'))
    dadostemp['sexo'] = q3
    lista.append(dadostemp.copy())
    dadostemp.clear()
    dej = str(input('Continue [S/N]')).strip().upper()[0]
    if dej == 'S': continue
    elif dej == 'N': break
    else: print ('COMANDO INVALIDO!')
tabela = "[NOME:]", "[IDADE]", "[SEXO]"
print (f'{tabela[0]:<15} {tabela[1]:<10} {tabela[2]:<10}')
for pessoa in lista:
    print(f'{pessoa["nome"]:<15} {pessoa["idade"]:<10} {pessoa["sexo"]:<10}')