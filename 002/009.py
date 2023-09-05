#https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/dicionarios-em-python/modulos/exercicio-94-unindo-dicionarios-e-listas/

dados = {}
lista = []
soma = media = 0
print ('-'*40)
print ('Registro de Pessoas')
print ('-'*40)
while True:
    dados['nome:'] = str(input('Nome: '))
    while True:
        dados['sexo:'] = str(input('Sexo: ')).strip().upper()[0]
        if dados['sexo:'] == 'M' or dados['sexo:'] == 'F':
            break
        else: print ('Erro! Digite Apenas M ou F')
    dados['idade:'] = int(input('Idade: '))
    soma += dados['idade:']
    lista.append(dados.copy())
    dados.clear()
    dej = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if dej =='N':
        break
    elif dej == 'S':
        continue
    else: print ('Erro! Digite apenas S ou N')
print ('*'*40)
print (f'Ao Todo Temos {len(lista)} cadastradas!')
media = soma / len(lista)
print (f'Ao todo a media de idade é {media:.1f}')
print ('As Mulheres cadrastadas São ', end='')
for pessoa in lista:
    if pessoa['sexo:'] =='F':
        print (f'{pessoa["nome:"]}', end=' ')
print ()
print ('Pessoas que estão acima da media!', end='')
for pessoa in lista:
    if pessoa['idade:'] >= media:
        print (f'{pessoa["nome:"]}', end=' ')
        print (f'{pessoa["idade:"]}')


