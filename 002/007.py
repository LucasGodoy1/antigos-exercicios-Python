dados = {}
gols = []
tot = 0
print ('*'*40)
print ('Registro de Partida!')
print ('*'*40)
dados['Nome: '] = str(input('Digite o Nome do Jogador: '))
q1 = int(input(f'Quantas Partidas {dados["Nome: "]} Jogou ?'))
for i in range (q1):
    q2 = int(input(f'Quantos Gols na {i+1}° Patida? '))
    tot += q2
    gols.append(q2)
dados['Gols'] = gols[:] 
dados['Total de Gols'] = tot
print ('*'*40)
print (f'O campo Nome tem o Valor: {dados["Nome: "]}')
print (f'O campo Gols tem o Valor: {dados["Gols"]}')
print (f'O campo Total de Gols tem o Valor: {dados["Total de Gols"]}')
print ('*'*40)
print (f'O jogador {dados["Nome: "]} Jogou {q1} Partidas')
for i, v in enumerate (dados["Gols"]):
    print (f'Na Partida {i+1} Fez {v} Gols ')


