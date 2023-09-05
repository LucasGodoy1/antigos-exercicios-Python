n1 = str(input('Digite o nome do jogador'))
g1 = str(input('Quantos gols na partida ?'))

def registro(a, b):
    if b.isnumeric():
        b = int(b)
    else:
        b = 0
    if a.strip() == '':
        a = '<Jogador desconhecido>'
    print (f'O jogador {a} fez {b} Gols')

registro(n1, g1)