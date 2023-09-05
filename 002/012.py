print ('Calculo de Terreno!')
largura = float(input('Digite a largura [m]'))
comprimento = float(input('Digite o comprimento [m]'))

def area (a, b):
    res = a * b
    print (f'A area de um terreno {a} x {b} é de {res}')

area(largura, comprimento)