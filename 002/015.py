print ('-'*30)
print ('-'*30)

def anal (* num):
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

 
anal (2, 9, 4, 5, 7, 1)
anal (4, 7, 0)
anal (1, 2)
anal (6)
anal (0)

