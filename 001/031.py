print ('Vamso descobrir se é um triangulo')
a = int(input('Diga um tamanho para (A) '))
b = int(input('Diga um tamanho para o (B) '))
c = int(input('Diga um tamanho para o (C)'))
if a == b == c:
    print ('Esse é um triangulo EQUILATERO')
elif a == b != c or c == b != a or a == c != b:
    print ('Esse é um triangulo ISOCELES ')
else:
    print ('esse é um triangulo ESCALENO')