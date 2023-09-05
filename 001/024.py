tria = int(input('Qual a largura? (A)'))
trib = int(input('Qual a largura (B)'))
tric = int(input('Qual a altura (C)'))
if tria < trib + tric and trib < tria + tric and tric < tria + trib:
    print ('Isso pode formar um triangulo')
else: print ('Isso não pdoe formar um triangulo!')