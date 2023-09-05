print ('-'*30)
print ('-'*30)

def anali (* num):
    contador = maior = 0
    print ('Analisando Valores')
    for n in num:
        print (f' {n} ', end= '')
    if contador == 0:
        maior = n
    else:
        if n > maior:
            maior = n
    contador +=1
    print (f'Foram informados {contador} valores')
    print (f'O maior valor informado foi {maior}')   

 
anali (2, 9, 4, 5, 7, 1)
anali (4, 7, 0)
anali (1, 2)
anali (6)
anali (0)

